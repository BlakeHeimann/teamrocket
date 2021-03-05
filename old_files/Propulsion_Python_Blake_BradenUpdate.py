import math as math
import numpy as numpy

aero = numpy.array([[0,0]])

class structtype():
    pass

def mass_flow(s):
    massFlow = s.pMass/s.burnTime
    return massFlow

def delta_v(s):
    deltaV = s.isp * 9.81 * math.log(s.cMass/(s.cMass - s.pMass))
    return deltaV

def drag_force(vX,vY,rho,A,h):
    vTotal = math.sqrt(vX**2 + vY**2)
    
    if h >= 0 and h < 11000:
        temp = -.0065*h + 288.15
    elif h >= 11000 and h < 20000:
        temp = 216.65
    elif h >= 20000 and h < 32000:
        temp = 0.001*h + 196.7
    elif h >= 32000 and h < 48000:
        temp = 0.0026*h + 145.21
    elif h >= 48000 and h < 51000:
        temp = 270.35
    elif h >= 51000 and h < 85000:
        temp = -.0025*h + 393.97
    elif h >= 85000:
        temp = 185
    
    M = vTotal/math.sqrt(1.4*287*temp)
    
    if M >= 0 and M < 0.7:
        Cd = 0.1546*M**2 + 0.111*M + 0.0501
    elif M >= 0.7 and M<1.35:
        Cd = -0.9157*M**2 + 2.3847*M - 1.0297
    elif M >= 1.35 and M <2.05:
        Cd = -0.0446*M**2 + 0.0636*M + 0.5161
    elif M >= 2.05 and M <2.35:
        Cd = -0.1063*M + 0.6764
    elif M >= 2.35 and M <2.65:
        Cd = 0.2204*M**2 - 1.1635*M + 1.9436
    elif M >= 2.65 and M <2.9:
        Cd = -0.3626*M**2 + 1.9607*M - 2.2412
    elif M >= 2.9 and M <3.2:
        Cd = 0.0121*M + 0.3594
    elif M >= 3.2 and M <4.2:
        Cd = .0004*M**2 - 0.0018*M + 0.4001
    elif M > 4.2:
        Cd = 0.39
    
    dynamicp = .5*rho*vTotal**2
    drag = -.5*rho*Cd*A*vTotal**2
    global aero
    aero = numpy.append(aero, [[M, dynamicp]], axis = 0)
    return drag

def find_rho(h):
    #I think this rho = 0 is necessary or Matlab has weird error about not
    #defining the variable
    rho = 0
    # BLAKE SECTION
    if h >= 0 and h < 8000:
        rho = -9E-5*h + 1.1914
    elif h >= 8000 and h < 13000:
        rho = -5E-5*h + .9028
    elif h >= 13000 and h < 18000:
        rho = -3E-5*h + 0.6844
    elif h >= 18000 and h < 30000:
        rho = -8E-6*h + 0.2563
    elif h >= 30000 and h < 40000:
        rho = 1.8965*math.exp(-2E-4*h)
    elif h >= 40000 and h < 50000:
        rho = -3E-7*h + 0.0159
    elif h >= 50000 and h < 70000:
        rho = 2E-12*h**2 -3E-7*h + 0.0111
    elif h >=70000 and h < 85000:
        rho = -6E-9*h + 0.0005
    elif h >= 85000:
        rho = 0.000001
    return rho

    
# Payload stage
payload = structtype()
payload.mass = 5 #kg
payload.struct = 143.75 #kg
payload.tMass = payload.mass+payload.struct

# Stage three
stage3 = structtype()
stage3.pMass = 1760 #kg
stage3.eMass = 189 #kg
stage3.thrust = 106212 #N
stage3.burnTime = 46 #s
stage3.isp = 2776/9.81 #1/2
stage3.struct = 139.8 #kg
stage3.tMass = stage3.eMass + stage3.pMass + stage3.struct
stage3.cMass = stage3.tMass + payload.tMass
stage3.dv = delta_v(stage3)
stage3.massFlow = mass_flow(stage3)

# Stage two
stage2 = structtype()
stage2.pMass = 5080 #kg
stage2.eMass = 527 #kg
stage2.thrust = 220345 #N
stage2.burnTime = 64 #s
stage2.isp = 2776/9.81 #1/2
stage2.struct = 222 #kg
stage2.tMass = stage2.eMass + stage2.pMass + stage2.struct
stage2.cMass = stage2.tMass + stage3.cMass
stage2.dv = delta_v(stage2)
stage2.massFlow = mass_flow(stage2)

# Stage one
stage1 = structtype()
stage1.pMass = 15000 #kg
stage1.eMass = 1779 #kg
stage1.thrust = 469054 #N
stage1.burnTime = 74 #s
stage1.isp = 2314/9.81 #1/2
stage1.struct = 998 #kg
stage1.tMass = stage1.eMass + stage1.pMass + stage1.struct
stage1.cMass = stage1.tMass + stage2.cMass
stage1.dv = delta_v(stage1)
stage1.massFlow = mass_flow(stage1)

# Calculations
stage1.coastTime = 51 #s
stage2.coastTime = 164 #s
stage1.burnRotation = numpy.linspace(90,40,stage1.burnTime)
stage1.coastRotation = numpy.linspace(40,40,stage1.coastTime)
stage2.burnRotation = numpy.linspace(40,40,stage2.burnTime)
stage2.coastRotation = numpy.linspace(40,0,stage2.coastTime)
stage3.burnRotation = numpy.linspace(0,-1.5, stage3.burnTime)

totalBurnTime = stage1.burnTime + stage2.burnTime + stage3.burnTime
totalCoastTime = stage1.coastTime + stage2.coastTime
totalTime = totalBurnTime + totalCoastTime

rocket = structtype()
rocket.velocityX = numpy.zeros((totalTime,1))
rocket.velocityY = numpy.zeros((totalTime,1))
rocket.accelerationX = numpy.zeros((totalTime,1))
rocket.accelerationY = numpy.zeros((totalTime,1))
rocket.positionX = numpy.zeros((totalTime,1))
rocket.positionY = numpy.zeros((totalTime,1))

A = 1.55

for t in range(totalTime):
    if(t == 0):
        rocket.positionX[t] = 0
        rocket.positionY[t] = 0
    else:
        rocket.positionY[t] = rocket.positionY[t-1] + rocket.velocityY[t-1] + .5 * rocket.accelerationY[t-1]
        rocket.positionX[t] = rocket.positionX[t-1] + rocket.velocityX[t-1] + .5 * rocket.accelerationX[t-1]
    currentRho = find_rho(rocket.positionY[t])
    
    if(t == 0):
        rocket.velocityX[t] = 0
        rocket.velocityY[t] = 0

        rocket.accelerationY[t] = math.sin(math.radians(stage1.burnRotation[t]))*((stage1.thrust/(stage1.cMass - stage1.massFlow*(t-1)))-9.81)
        rocket.accelerationX[t] = math.cos(math.radians(stage1.burnRotation[t]))*(stage1.thrust/(stage1.cMass - stage1.massFlow*(t-1)))
    elif(t < stage1.burnTime):
        rocket.velocityX[t] = rocket.velocityX[t-1] + rocket.accelerationX[t-1]
        rocket.velocityY[t] = rocket.velocityY[t-1] + rocket.accelerationY[t-1]
        
        dragForce = drag_force(rocket.velocityX[t], rocket.velocityY[t],currentRho,A,rocket.positionY[t])
            
        rocket.accelerationY[t] = math.sin(math.radians(stage1.burnRotation[t]))*(((stage1.thrust+dragForce)/(stage1.cMass - stage1.massFlow*(t-1)))-9.81)
        rocket.accelerationX[t] = math.cos(math.radians(stage1.burnRotation[t]))*((stage1.thrust+dragForce)/(stage1.cMass - stage1.massFlow*(t-1)))
    elif(t < stage1.burnTime+stage1.coastTime):
        rocket.velocityX[t] = rocket.velocityX[t-1] + rocket.accelerationX[t-1]
        rocket.velocityY[t] = rocket.velocityY[t-1] + rocket.accelerationY[t-1]
        
        dragForce = drag_force(rocket.velocityX[t], rocket.velocityY[t],currentRho,A,rocket.positionY[t])

        rocket.accelerationY[t] = math.sin(math.radians(stage1.coastRotation[t-stage1.burnTime]*dragForce))-9.81
        rocket.accelerationX[t] = math.cos(math.radians(stage1.coastRotation[t-stage1.burnTime]*dragForce))
    elif(t < stage1.burnTime + stage1.coastTime + stage2.burnTime):
        rocket.velocityX[t] = rocket.velocityX[t-1] + rocket.accelerationX[t-1]
        rocket.velocityY[t] = rocket.velocityY[t-1] + rocket.accelerationY[t-1]
        
        dragForce = drag_force(rocket.velocityX[t], rocket.velocityY[t],currentRho,A,rocket.positionY[t])
        
        rocket.accelerationY[t] = math.sin(math.radians(stage2.burnRotation[t-stage1.coastTime-stage1.burnTime]))*(((stage2.thrust+dragForce)/(stage2.cMass - stage2.massFlow*(t-stage1.burnTime-stage1.coastTime-1)))-9.81)
        rocket.accelerationX[t] = math.cos(math.radians(stage2.burnRotation[t-stage1.coastTime-stage1.burnTime]))*((stage2.thrust+dragForce)/(stage2.cMass - stage2.massFlow*(t-stage1.coastTime-stage1.burnTime-1)))
    elif(t < stage1.burnTime+stage1.coastTime+stage2.burnTime+stage2.coastTime):
        rocket.velocityX[t] = rocket.velocityX[t-1] + rocket.accelerationX[t-1]
        rocket.velocityY[t] = rocket.velocityY[t-1] + rocket.accelerationY[t-1]
        
        dragForce = drag_force(rocket.velocityX[t], rocket.velocityY[t],currentRho,A,rocket.positionY[t])
        
        rocket.accelerationY[t] = math.sin(math.radians(stage2.coastRotation[t-stage1.burnTime-stage1.coastTime-stage2.burnTime]*dragForce))-9.81
        rocket.accelerationX[t] = math.cos(math.radians(stage2.coastRotation[t-stage1.burnTime-stage1.coastTime-stage2.burnTime]*dragForce))
    else:
        rocket.velocityX[t] = rocket.velocityX[t-1] + rocket.accelerationX[t-1]
        rocket.velocityY[t] = rocket.velocityY[t-1] + rocket.accelerationY[t-1]
        
        dragForce = drag_force(rocket.velocityX[t], rocket.velocityY[t],currentRho,A,rocket.positionY[t])
        
        rocket.accelerationY[t] = math.sin(math.radians(stage3.burnRotation[t-stage1.coastTime-stage1.burnTime-stage2.burnTime-stage2.coastTime]))*(((stage3.thrust+dragForce)/(stage3.cMass - stage3.massFlow*(t-stage1.burnTime-stage1.coastTime-stage2.burnTime-stage2.coastTime-1)))-9.81)
        rocket.accelerationX[t] = math.cos(math.radians(stage3.burnRotation[t-stage1.coastTime-stage1.burnTime-stage2.burnTime-stage2.coastTime]))*((stage3.thrust+dragForce)/(stage3.cMass - stage3.massFlow*(t-stage1.coastTime-stage1.burnTime-stage2.burnTime-stage2.coastTime-1)))


#print('The altitude at the end of the flight is:', round(*rocket.positionY[len(rocket.positionY)-1],2), 'm')
#print('The maximum dynamic pressure felt on the vehicle is:')
mach_array = aero[:,0]
dynamic_pressure_array = aero[:,1]
#print(numpy.amax(dynamic_pressure_array))

absolute_val_array = numpy.absolute(mach_array - 1)
#print(absolute_val_array)
smallest_difference_index = absolute_val_array.argmin()
print(smallest_difference_index)
#print(numpy.where(aero[:,0] > .999 and aero[:,0] < 1.01))
#print(aero)
#print(aero[154,1])

# subplot(2,2,1)
# plot(0:totalTime-1, rocket.accelerationY)
# hold on
# plot(0:totalTime-1, rocket.accelerationX)
# title('Acceleration')
# xlabel('Time (s)')
# ylabel('Acceleration (m/s^2)')
# hold off
# subplot(2,2,2)
# plot(0:totalTime-1, rocket.velocityY)
# hold on
# plot(0:totalTime-1, rocket.velocityX)
# xlabel('Time (s)')
# ylabel('Velocity (m/s)')
# title('Velocity')
# hold off
# subplot(2,2,3)
# plot(0:totalTime-1, rocket.positionY/1000)
# hold on
# title('Altitude')
# xlabel('Time (s)')
# ylabel('Altitude (km)')
# hold off
# subplot(2,2,4)
# plot(0:totalTime-1,rocket.positionX/1000)
# hold on
# title('Position')
# xlabel('Time (s)')
# ylabel('Position (km)')
# hold off

# fprintf('Stage 3 dv = %f\n',stage3.dv)
# fprintf('Stage 3 TWR = %f\n',stage3.thrust/(stage3.cMass*9.81))
# fprintf('Stage 2 dv = %f\n',stage2.dv)
# fprintf('Stage 2 TWR = %f\n',stage2.thrust/(stage2.cMass*9.81))
# fprintf('Stage 1 dv = %f\n',stage1.dv)
# fprintf('Stage 1 TWR = %f\n',stage1.thrust/(stage1.cMass*9.81))
