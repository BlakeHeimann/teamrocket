import numpy

def environmental_torque_calculation(stage1,stage2,stage3,positionY,orientation):

    totalburn_time = stage1.burn_time + stage2.burn_time + stage3.burn_time
    totalCoastTime = stage1.coastTime + stage2.coastTime
    totalTime = totalburn_time + totalCoastTime

    R_E = 6367e3 # %m 
    mu = 3.986e14 # m^3/s^2
    I_1 = 204.778 # kg*m^2
    I_2 = 94.6823 # kg*m^2
    I_3 = 45.5062 # kg*m^2
    A_s = numpy.linspace(24.9,1.606,91)
    x_cp = numpy.linspace(6.77,0,91)
    x_cm = 5.6315
    # Solar Radiation Pressure Values
    F_s = 1358 # W/m^2
    c = 3e8 # m/s (speed of light)
    r = 0.916 # Surface reflectance
    SunAngle = 20 # Angle Sun to Earth
    # Magnetic Torque Values
    B_E = 30e-6
    D = 0.1 # Used as a typical value, real values determined through testing
    T_m = numpy.empty(totalTime)
    T_m[0:totalTime] = D*B_E # Magnetic Torque is constant
    # Aerodynamic Drag
    AirDensity = 1.225
    C_d = 0.2 # Estimated value used, C_d determined through testing
    Windspeed = 2.2352 # m/s ~5 mph

    timeVec = numpy.arange(0,totalTime)

    # Initialize Force/Torque Vectors
    T_g = numpy.empty(totalTime)
    F_SR = numpy.empty(totalTime)
    T_SR = numpy.empty(totalTime)
    F_drag = numpy.empty(totalTime)
    T_drag = numpy.empty(totalTime)
    T_total = numpy.empty(totalTime)


    for i in timeVec:
        if i < (stage1.burn_time + stage1.coastTime):
            T_g[i] = (3*mu/(2*(R_E+positionY[i])**3))*I_1*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))
        elif i < (stage1.burn_time + stage1.coastTime + stage2.burn_time + stage2.coastTime):
            T_g[i] = (3*mu/(2*(R_E+positionY[i])**3))*I_2*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))
        else:
            T_g[i] = (3*mu/(2*(R_E+positionY[i])**3))*I_3*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))

        # Solar Radiation
        F_SR[i] = (F_s/c)*A_s[int(numpy.ceil(numpy.abs(orientation[i])))]*(1+r)*numpy.cos(numpy.deg2rad(90-orientation[i]+SunAngle))
        T_SR[i] = F_SR[i]*(x_cp[int(numpy.ceil(numpy.abs(orientation[i])))]-x_cm)

        # Aerodynamic Drag/Wind Variation
        F_drag[i] = 0.5*AirDensity*Windspeed**2*C_d*A_s[int(90-numpy.ceil(numpy.abs(orientation[i])))]
        T_drag[i] = F_drag[i]*(x_cp[int(numpy.ceil(numpy.abs(orientation[i])))] - x_cm)

        T_total[i] = T_m[i] + T_g[i] + T_SR[i] + T_drag[i]

    return(T_total)

def fin_actuator_calculation(velocityX,velocityY,stage1):
    AngleOfAttack = numpy.deg2rad(3)
    AirDensity = 1.225
    VehicleCenterOfGravity = [5.6315, 0, 0]
    ControlSurfaceCenterOfGravity = 0.01
    FinArea = 0.001
    # MomentOfInertia = 204.778; # Stage 1 MOI
    Airspeed = numpy.sqrt(numpy.square(velocityY[0:stage1.burn_time]) + numpy.square(velocityX[0:74]))


    ## Calculations
    CoefficientOfLift = 2*numpy.pi*AngleOfAttack
    Lift = CoefficientOfLift*AirDensity*FinArea*numpy.square(Airspeed)/2
    Torque = 2*Lift*(VehicleCenterOfGravity[0]-ControlSurfaceCenterOfGravity)*numpy.sin(numpy.deg2rad(90))

    return(Torque)