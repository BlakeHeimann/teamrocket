import numpy
import math
from propulsion import find_rho

def environmental_torque_calculation(stage1,stage2,stage3,payload_fairing,positionY,orientation,rocket_height,nosecone_height,total_center_of_mass,drag_array):

    totalburn_time = stage1.burn_time + stage2.burn_time + stage3.burn_time
    totalCoastTime = stage1.coastTime + stage2.coastTime
    totalTime = totalburn_time + totalCoastTime

    Radius_Earth = 6367e3 # %m 
    mu = 3.986e14 # m^3/s^2

    Moment_of_Inertia_Stage_1 = (1/4)*stage1.combined_mass*stage1.outside_radius**2 + (1/12)*stage1.combined_mass*rocket_height**2
    Moment_of_Inertia_Stage_2 = (1/4)*stage2.combined_mass*stage2.outside_radius**2 + (1/12)*stage2.combined_mass*(rocket_height-stage1.height)**2
    Moment_of_Inertia_Stage_3 = (1/4)*stage3.combined_mass*stage3.outside_radius**2 + (1/12)*stage3.combined_mass*(rocket_height-stage1.height -stage2.height)**2

    zero_angle_area = stage1.height*stage1.outside_radius*2 + stage2.height*stage2.outside_radius*2 + stage3.height*stage3.outside_radius + payload_fairing.height*payload_fairing.outside_radius*2 + nosecone_height*payload_fairing.outside_radius
    Area_Illuminated = numpy.linspace(zero_angle_area,stage3.outside_radius**2*math.pi,91) # Surface Area Illuminated by Sun # f(angle)

    x_cp = numpy.linspace(((stage1.height+stage2.height+stage3.height+payload_fairing.height)/2 + nosecone_height/3),0,91) # Correlating Center of Pressure for Area_Illuminated # also f(angle)
    x_cm = total_center_of_mass # Vehicle Center of Mass
    # Solar Radiation Pressure Values
    Solar_Constant = 1358 # W/m^2
    c = 3e8 # m/s (speed of light)
    r = 0.916 # Surface reflectance
    

    #CHANGES BASED ON LAUNCH LOCATION
    SunAngle = 20 # Angle Sun to Earth


    # Magnetic Torque Values
    B_E = 30e-6 # Magnetic Field Earth Strength
    D = 0.1 # Vehicle Dipole # Used as a typical value, real values determined through testing
    Torque_Magnetic = numpy.empty(totalTime) # Initialize Torque_Magnetic
    Torque_Magnetic[0:totalTime] = D*B_E # Magnetic Torque is constant
    timeVec = numpy.arange(0,totalTime) # Vector of time from 0 to totalTime i.e. [0, 1, 2 ... totalTime]
    # Initialize Force/Torque Vectors
    Torque_Gravitation = numpy.empty(totalTime)
    Force_SolarRadiation = numpy.empty(totalTime)
    Torque_SolarRadiation = numpy.empty(totalTime)
    Torque_Drag = numpy.empty(totalTime)
    Torque_Total = numpy.empty(totalTime)

    Force_Drag = drag_array

    for i in timeVec:
        # Gravitational Torque
        if i < (stage1.burn_time + stage1.coastTime):
            Torque_Gravitation[i] = (3*mu/(2*(Radius_Earth+positionY[i])**3))*Moment_of_Inertia_Stage_1*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))
        elif i < (stage1.burn_time + stage1.coastTime + stage2.burn_time + stage2.coastTime):
            Torque_Gravitation[i] = (3*mu/(2*(Radius_Earth+positionY[i])**3))*Moment_of_Inertia_Stage_2*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))
        else:
            Torque_Gravitation[i] = (3*mu/(2*(Radius_Earth+positionY[i])**3))*Moment_of_Inertia_Stage_3*numpy.sin(numpy.deg2rad(2*(90-orientation[i])))

        # Solar Radiation
        Force_SolarRadiation[i] = (Solar_Constant/c)*Area_Illuminated[int(numpy.ceil(numpy.abs(orientation[i])))]*(1+r)*numpy.cos(numpy.deg2rad(90-orientation[i]+SunAngle))
        Torque_SolarRadiation[i] = Force_SolarRadiation[i]*(x_cp[int(numpy.ceil(numpy.abs(orientation[i])))]-x_cm)

        # Force_Drag[i] = 0.5*AirDensity*Windspeed**2*C_d*Area_Illuminated[int(90-numpy.ceil(numpy.abs(orientation[i])))]
        Torque_Drag[i] = Force_Drag[i]*(x_cp[int(numpy.ceil(numpy.abs(orientation[i])))] - x_cm)
        Torque_Total[i] = Torque_Magnetic[i] + Torque_Gravitation[i] + Torque_SolarRadiation[i] + Torque_Drag[i]

    return(Torque_Total)

def fin_actuator_calculation(velocityX,velocityY,stage1,positionY,total_center_of_mass):
    AngleOfAttack = numpy.deg2rad(3) # Using 3 degrees for capability testing
    #AirDensity = 1.225 # kg/m^3
    x_cm = total_center_of_mass # Vehicle Center of Mass (Vertical)
    x_cm_cs = 0.01 # Center of Mass of Control Surface (Vertical)
    #FinArea = 0.001
    FinArea = (stage1.outside_radius/2)*(3/2)*stage1.outside_radius # Area of Control Surface
    CoefficientOfLift = 2*numpy.pi*AngleOfAttack # Coefficient of Lift of Control Surface
    Torque = numpy.zeros((len(velocityY),1))

    for i in range(len(velocityY)):
        Airspeed = numpy.sqrt(numpy.square(velocityY[i]) + numpy.square(velocityX[i]))
        Lift = CoefficientOfLift*find_rho(positionY[i])*FinArea*numpy.square(Airspeed)/2 # Lift Generated by Control Surface
        Torque[i] = 2*Lift*(x_cm-x_cm_cs)*numpy.sin(numpy.deg2rad(90)) # Torque Generated by Lifting Force
    return(Torque)
