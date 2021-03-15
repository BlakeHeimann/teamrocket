import math as math
import numpy as numpy

def mass_flow(s):
    if s.burn_time == 0:
        return 0
    else:
        mass_flow = s.propellant_mass/s.burn_time
        return mass_flow

def delta_v(s):
    if s.burn_time == 0:
        return 0
    else:
        deltaV = s.isp * 9.81 * math.log(s.combined_mass/(s.combined_mass - s.propellant_mass))
        return deltaV

def drag_force(vX,vY,rho,A,altitude,aero):
    vTotal = math.sqrt(vX**2 + vY**2)
    
    if altitude>= 0 and altitude< 11000:
        temp = -.0065*altitude+ 288.15
    elif altitude>= 11000 and altitude< 20000:
        temp = 216.65
    elif altitude>= 20000 and altitude< 32000:
        temp = 0.001*altitude+ 196.7
    elif altitude>= 32000 and altitude< 48000:
        temp = 0.0026*altitude+ 145.21
    elif altitude>= 48000 and altitude< 51000:
        temp = 270.35
    elif altitude>= 51000 and altitude< 85000:
        temp = -.0025*altitude+ 393.97
    elif altitude>= 85000:
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
    aero = numpy.append(aero, [[M, dynamicp]], axis = 0)
    return drag, aero

def find_rho(altitude):
    #I think this rho = 0 is necessary or Matlab has weird error about not
    #defining the variable
    rho = 0
    # BLAKE SECTION
    if altitude >= 0 and altitude < 8000:
        rho = -9E-5*altitude + 1.1914
    elif altitude >= 8000 and altitude < 13000:
        rho = -5E-5*altitude+ .9028
    elif altitude>= 13000 and altitude< 18000:
        rho = -3E-5*altitude+ 0.6844
    elif altitude>= 18000 and altitude< 30000:
        rho = -8E-6*altitude+ 0.2563
    elif altitude>= 30000 and altitude< 40000:
        rho = 1.8965*math.exp(-2E-4*altitude)
    elif altitude>= 40000 and altitude< 50000:
        rho = -3E-7*altitude+ 0.0159
    elif altitude>= 50000 and altitude< 70000:
        rho = 2E-12*altitude**2 -3E-7*altitude+ 0.0111
    elif altitude>=70000 and altitude< 85000:
        rho = -6E-9*altitude+ 0.0005
    elif altitude>= 85000:
        rho = 0.000001
    return rho


def propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass):
    aero = numpy.array([[0,0]])

    # Calculations

    #taking into account the gravity turn

    #these were the original, I changed them to account for gravity turn
    # stage1.burnRotation = numpy.linspace(90,40,stage1.burn_time)
    # stage1.coastRotation = numpy.linspace(40,40,stage1.coastTime)
    # stage2.burnRotation = numpy.linspace(40,40,stage2.burn_time)
    # stage2.coastRotation = numpy.linspace(40,0,stage2.coastTime)
    # stage3.burnRotation = numpy.linspace(0,-1.5, stage3.burn_time)

    # stage1.burnRotation = numpy.linspace(90,50,stage1.burn_time)
    # stage1.coastRotation = numpy.linspace(50,40,stage1.coastTime)
    # stage2.burnRotation = numpy.linspace(40,20,stage2.burn_time)
    # stage2.coastRotation = numpy.linspace(20,0,stage2.coastTime)
    # stage3.burnRotation = numpy.linspace(0,-1.5, stage3.burn_time)
    # orientation = numpy.concatenate((stage1.burnRotation,stage1.coastRotation,stage2.burnRotation,stage2.coastRotation,stage3.burnRotation))

    totalburn_time = stage1.burn_time + stage2.burn_time + stage3.burn_time
    totalCoastTime = stage1.coastTime + stage2.coastTime
    totalTime = totalburn_time + totalCoastTime

    stage1.burnRotation = numpy.linspace(90,42,stage1.burn_time)
    gravity_turn_rotation = numpy.linspace(42,0,totalTime - stage1.burn_time)
    orientation = numpy.concatenate((stage1.burnRotation,gravity_turn_rotation))

    velocityX = numpy.zeros((totalTime,1))
    velocityY = numpy.zeros((totalTime,1))
    accelerationX = numpy.zeros((totalTime,1))
    accelerationY = numpy.zeros((totalTime,1))
    positionX = numpy.zeros((totalTime,1))
    positionY = numpy.zeros((totalTime,1))

    A = (stage3.outside_radius**2)*math.pi

    for t in range(totalTime):
        if(t == 0):
            positionX[t] = 0
            positionY[t] = 0
            
        else:
            positionY[t] = positionY[t-1] + velocityY[t-1] + .5 * accelerationY[t-1]
            positionX[t] = positionX[t-1] + velocityX[t-1] + .5 * accelerationX[t-1]
        currentRho = find_rho(positionY[t])
        
        if(t == 0):
            velocityX[t] = 0
            velocityY[t] = 0

            accelerationY[t] = math.sin(math.radians(orientation[t]))*((stage1.thrust/((stage1.mass + stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage1.mass_flow*(t-1)))-9.81)
            accelerationX[t] = math.cos(math.radians(orientation[t]))*(stage1.thrust/((stage1.mass + stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage1.mass_flow*(t-1)))
        elif(t < stage1.burn_time):
            velocityX[t] = velocityX[t-1] + accelerationX[t-1]
            velocityY[t] = velocityY[t-1] + accelerationY[t-1]
            
            dragForce, aero = drag_force(velocityX[t], velocityY[t],currentRho,A,positionY[t],aero)
                
            accelerationY[t] = math.sin(math.radians(orientation[t]))*(((stage1.thrust+dragForce)/((stage1.mass + stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage1.mass_flow*(t-1)))-9.81)
            accelerationX[t] = math.cos(math.radians(orientation[t]))*((stage1.thrust+dragForce)/((stage1.mass + stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage1.mass_flow*(t-1)))
        elif(t < stage1.burn_time+stage1.coastTime):
            velocityX[t] = velocityX[t-1] + accelerationX[t-1]
            velocityY[t] = velocityY[t-1] + accelerationY[t-1]
            
            dragForce, aero = drag_force(velocityX[t], velocityY[t],currentRho,A,positionY[t],aero)

            accelerationY[t] = math.sin(math.radians(orientation[t]*dragForce))-9.81
            accelerationX[t] = math.cos(math.radians(orientation[t]*dragForce))
        elif(t < stage1.burn_time + stage1.coastTime + stage2.burn_time):
            velocityX[t] = velocityX[t-1] + accelerationX[t-1]
            velocityY[t] = velocityY[t-1] + accelerationY[t-1]
            
            dragForce, aero = drag_force(velocityX[t], velocityY[t],currentRho,A,positionY[t],aero)
            
            accelerationY[t] = math.sin(math.radians(orientation[t]))*(((stage2.thrust+dragForce)/((stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage2.mass_flow*(t-stage1.burn_time-stage1.coastTime-1)))-9.81)
            accelerationX[t] = math.cos(math.radians(orientation[t]))*((stage2.thrust+dragForce)/((stage2.mass + stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage2.mass_flow*(t-stage1.coastTime-stage1.burn_time-1)))
        elif(t < stage1.burn_time+stage1.coastTime+stage2.burn_time+stage2.coastTime):
            velocityX[t] = velocityX[t-1] + accelerationX[t-1]
            velocityY[t] = velocityY[t-1] + accelerationY[t-1]
            
            dragForce, aero = drag_force(velocityX[t], velocityY[t],currentRho,A,positionY[t],aero)
            
            accelerationY[t] = math.sin(math.radians(orientation[t]*dragForce))-9.81
            accelerationX[t] = math.cos(math.radians(orientation[t]*dragForce))
        else:
            velocityX[t] = velocityX[t-1] + accelerationX[t-1]
            velocityY[t] = velocityY[t-1] + accelerationY[t-1]
            
            dragForce, aero = drag_force(velocityX[t], velocityY[t],currentRho,A,positionY[t],aero)
            
            accelerationY[t] = math.sin(math.radians(orientation[t]))*(((stage3.thrust+dragForce)/((stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage3.mass_flow*(t-stage1.burn_time-stage1.coastTime-stage2.burn_time-stage2.coastTime-1)))-9.81)
            accelerationX[t] = math.cos(math.radians(orientation[t]))*((stage3.thrust+dragForce)/((stage3.mass + payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass) - stage3.mass_flow*(t-stage1.coastTime-stage1.burn_time-stage2.burn_time-stage2.coastTime-1)))
    mach_array = aero[:,0]
    dynamic_pressure_array = aero[:,1]
    max_dynamic_pressure = numpy.amax(dynamic_pressure_array)
    time_of_max_dynamic_pressure = numpy.argmax(dynamic_pressure_array)
    absolute_val_array = numpy.absolute(mach_array - 1)
    time_of_supersonic = absolute_val_array.argmin()
    return(positionX,positionY,velocityX,velocityY,accelerationX,accelerationY,mach_array,dynamic_pressure_array,orientation,max_dynamic_pressure,time_of_max_dynamic_pressure,time_of_supersonic)
        
        