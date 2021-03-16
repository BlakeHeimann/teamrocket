from stage import Stage
from structure import skin_density, stiffener_density
from propulsion import delta_v, propulsion_analysis
from configuration import payload_housing_mass, skin_thickness, center_of_mass, center_of_pressure, dynamic_center_of_mass_center_of_pressure
from adcs import environmental_torque_calculation, fin_actuator_calculation
from power_thermal import power_thermal_calculation
import numpy as numpy
import csv

def main():
    input_array = numpy.char.rstrip(numpy.char.lstrip(numpy.loadtxt('INPUT.py',delimiter = '=',dtype = 'str')))
    input_keys = input_array[:,0]
    input_values = input_array[:,1]
    inputs = dict(zip(input_keys,input_values))

    #units of time are defined as integers not float
    payload_mass = float(inputs.get('payload_mass'))
    payload_fairing_height = float(inputs.get('payload_fairing_height'))
    stage1_height = float(inputs.get('stage1_height'))
    stage1_burnTime = int(inputs.get('stage1_burnTime'))
    stage1_propellant_mass = float(inputs.get('stage1_propellant_mass'))
    stage1_engine_mass = float(inputs.get('stage1_engine_mass'))
    stage1_thrust = float(inputs.get('stage1_thrust'))
    stage1_isp = float(inputs.get('stage1_isp'))
    stage1_coastTime = int(inputs.get('stage1_coastTime'))
    stage2_height = float(inputs.get('stage2_height'))
    stage2_burnTime = int(inputs.get('stage2_burnTime'))
    stage2_propellant_mass = float(inputs.get('stage2_propellant_mass'))
    stage2_engine_mass = float(inputs.get('stage2_engine_mass'))
    stage2_thrust = float(inputs.get('stage2_thrust'))
    stage2_isp = float(inputs.get('stage2_isp'))
    stage2_coastTime = int(inputs.get('stage2_coastTime'))
    stage3_height = float(inputs.get('stage3_height'))
    stage3_burnTime = int(inputs.get('stage3_burnTime'))
    stage3_propellant_mass = float(inputs.get('stage3_propellant_mass'))
    stage3_engine_mass = float(inputs.get('stage3_engine_mass'))
    stage3_thrust = float(inputs.get('stage3_thrust'))
    stage3_isp = float(inputs.get('stage3_isp'))
    outside_diameter = float(inputs.get('outside_diameter'))
    propulsion_modifier = float(inputs.get('propulsion_modifier'))

    #necessary to calculate structure for the payload fairing stage. 
    payload_fairing_propellant_mass = 0
    payload_fairing_engine_mass = 0
    payload_fairing_thrust = 0
    payload_fairing_burnTime = 0
    payload_fairing_isp = 0

    inside_diameter = outside_diameter - skin_thickness

    inside_radius = inside_diameter/2
    outside_radius = outside_diameter/2

    #Creating Stages
    stage1 = Stage(stage1_height,inside_radius,outside_radius,skin_density,stiffener_density, stage1_propellant_mass, stage1_engine_mass,stage1_thrust,stage1_burnTime,stage1_isp)
    stage2 = Stage(stage2_height,inside_radius,outside_radius,skin_density,stiffener_density, stage2_propellant_mass, stage2_engine_mass,stage2_thrust,stage2_burnTime,stage2_isp)
    stage3 = Stage(stage3_height,inside_radius,outside_radius,skin_density,stiffener_density, stage3_propellant_mass, stage3_engine_mass,stage3_thrust,stage3_burnTime,stage3_isp)
    payload_fairing = Stage(payload_fairing_height,inside_radius,outside_radius,skin_density,stiffener_density, payload_fairing_propellant_mass, payload_fairing_engine_mass,payload_fairing_thrust,payload_fairing_burnTime,payload_fairing_isp)

    #Adding coast time to stages
    stage1.coastTime = stage1_coastTime #s
    stage2.coastTime = stage2_coastTime #s

    #Thermal/Power
    (real_battery_capacity,heat_generated_per_second,battery_mass) = power_thermal_calculation(stage1,stage2,stage3)

    #Adding in battery mass to payload fairing
    payload_fairing.mass = payload_fairing.mass + battery_mass

    #center of mass and center of pressure
    (total_center_of_mass,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height,nosecone_mass,fin_mass) = center_of_mass(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,outside_diameter)
    (slv_cop_from_nose,slv_cop_from_origin,slv_cop_from_nose_minus_stage_1,_slv_cop_from_origin_minus_stage_1) = center_of_pressure(outside_diameter,outside_radius,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height) # pylint: disable=unbalanced-tuple-unpacking
    nosecone_height = nosecone_lower_height + nosecone_lower_height

    #adding in fin_mass to stage1.mass
    stage1.mass = stage1.mass + fin_mass

    #This needs to be done outside of creating the stages as the combined masses depend on the masses of other stages 
    payload_fairing.combined_mass = payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass
    stage3.combined_mass = stage3.mass + payload_fairing.combined_mass
    stage2.combined_mass = stage2.mass + stage3.combined_mass
    stage1.combined_mass = stage1.mass + stage2.combined_mass

    #delta v is based on the combined masses so this also needs to be separate
    stage1.delta_v = delta_v(stage1)
    stage2.delta_v = delta_v(stage2)
    stage3.delta_v = delta_v(stage3)

    #dynamic mass and center of pressure arrays
    (dynamic_mass,dynamic_cop) = dynamic_center_of_mass_center_of_pressure(stage1,stage2,stage3,payload_fairing,fin_mass,nosecone_mass,payload_mass,slv_cop_from_nose,slv_cop_from_nose_minus_stage_1)

    #doing this avoids an annoying error that pops up when trying to find the max value of the dynamic pressure array, some weird warning with numpy ndarray 
    numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)

    #nominal propulsion calculation
    (_positionX,positionY,velocityX,velocityY,_accelerationX,_accelerationY,_mach_array,_dynamic_pressure_array,orientation,max_dynamic_pressure,time_of_max_dynamic_pressure,time_of_supersonic,drag_array) = propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass)

    #redoing propulsion calculation for increased modifier
    stage1.burn_time = round(stage1.burn_time*(1+propulsion_modifier))
    stage2.burn_time = round(stage2.burn_time*(1+propulsion_modifier))
    stage3.burn_time = round(stage3.burn_time*(1+propulsion_modifier))
    (_positionX_large,positionY_large,velocityX_large,velocityY_large,_accelerationX_large,_accelerationY_large,_mach_array_large,_dynamic_pressure_array_large,_orientation_large,_max_dynamic_pressure_large,_time_of_max_dynamic_pressure_large,_time_of_supersonic_large,_drag_array_large) = propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass)

    #redoing propulsion calculation for decreased modifier
    stage1.burn_time = round(stage1.burn_time*((1-propulsion_modifier)/(1+propulsion_modifier)))
    stage2.burn_time = round(stage2.burn_time*((1-propulsion_modifier)/(1+propulsion_modifier)))
    stage3.burn_time = round(stage3.burn_time*((1-propulsion_modifier)/(1+propulsion_modifier)))
    (_positionX_small,positionY_small,velocityX_small,velocityY_small,_accelerationX_small,_accelerationY_small,_mach_array_small,_dynamic_pressure_array_small,_orientation_small,_max_dynamic_pressure_small,_time_of_max_dynamic_pressure_small,_time_of_supersonic_small,_drag_array_small) = propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass)

    #ADCS
    environmental_torques = environmental_torque_calculation(stage1,stage2,stage3,payload_fairing,positionY,orientation,rocket_height,nosecone_height,total_center_of_mass,drag_array)
    fin_actuator_torque = fin_actuator_calculation(velocityX,velocityY,stage1,positionY,total_center_of_mass)

    print('The altitude at the end of the flight is (nominal):', round(*positionY[len(positionY)-1],2), 'm')
    print('The altitude at the end of the flight is (high):   ', round(*positionY_large[len(positionY_large)-1],2), 'm')
    print('The altitude at the end of the flight is (low):    ', round(*positionY_small[len(positionY_small)-1],2), 'm')

    print('The maximum dynamic pressure felt on the vehicle:  ', round(*max_dynamic_pressure,2), 'Pa at ', time_of_max_dynamic_pressure, 'seconds')
    print('Time when rocket will reach supersonic flight:     ',time_of_supersonic,'seconds')

    output_dictionary = {'rocket height (m)' : rocket_height,
    'total rocket mass (kg)' : stage1.combined_mass,
    'rocket center of mass from base(m)' : total_center_of_mass, 
    'rocket center of pressure from base (m)' : slv_cop_from_origin, 
    'stage 1 total mass (kg)' : stage1.mass,
    'stage 2 total mass (kg)': stage2.mass, 
    'stage 3 total mass (kg)' : stage3.mass, 
    'payload fairing total mass (kg)' : payload_fairing.combined_mass - nosecone_mass,
    'nosecone total mass (kg)' : nosecone_mass, 
    'battery capacity (Wh)' : real_battery_capacity, 
    'battery heat generation (J/s)' : heat_generated_per_second, 
    'stage 1 delta v (m/s)' : stage1.delta_v, 
    'stage 2 delta v (m/s)' : stage2.delta_v, 
    'stage 3 delta v (m/s)' : stage3.delta_v, 
    'time of supersonic flight (s)' : time_of_supersonic, 
    'max dynamic pressure (Pa)' : max_dynamic_pressure, 
    'time of max dynamic pressure (s)' : time_of_max_dynamic_pressure,

    'LOW END UNCERTAINTY horizontal velocity at the end of flight (m/s)' : round(*velocityX_small[len(velocityX_small)-1],3),
    'LOW END UNCERTAINTY vertical velocity at the end of flight (m/s)' : round(*velocityY_small[len(velocityY_small)-1],3),
    'LOW END UNCERTAINTY altitude at the end of flight (m)' : round(*positionY_small[len(positionY_small)-1],3),

    'HIGH END UNCERTAINTY horizontal velocity at the end of flight (m/s)' : round(*velocityX_large[len(velocityX_large)-1],3),
    'HIGH END UNCERTAINTY vertical velocity at the end of flight (m/s)' : round(*velocityY_large[len(velocityY_large)-1],3),
    'HIGH END UNCERTAINTY altitude at the end of flight (m)' : round(*positionY_large[len(positionY_large)-1],3),

    'NOMINAL horizontal velocity at the end of flight (m/s)' : round(*velocityX[len(velocityX)-1],3),
    'NOMINAL vertical velocity at the end of flight (m/s)' : round(*velocityY[len(velocityY)-1],3),
    'NOMINAL altitude at the end of flight (m)' : round(*positionY[len(positionY)-1],3),

    #Long Raw Data Arrays
    'dynamic center of mass from origin (m)' : dynamic_mass,
    'dynamic center of pressure from nose (m)' : dynamic_cop,
    'fin actuator torque (N*m)' : fin_actuator_torque, 
    'environmental torque (N*m)' : environmental_torques,
    }

    # other_output_dictionary = {'center of pressure from origin without stage 1 (m)' : slv_cop_from_origin_minus_stage_1,
    # 'NOMINAL horizontal distance array(m)' : positionX,
    # 'NOMINAL horizontal acceleration (m/s^2)' : accelerationX,
    # 'NOMINAL vertical acceleration (m/s^2)' : accelerationY,
    # 'HIGH END horizontal distance (m)' : positionX_large,
    # 'HIGH END horizontal acceleration (m/s^2)' : accelerationX_large,
    # 'HIGH END vertical acceleration (m/s^2)' : accelerationY_large,
    # 'HIGH END mach array' : mach_array_large,
    # 'HIGH END dynamic pressure array' : dynamic_pressure_array_large,
    # 'HIGH END orientation array' : orientation_large,
    # 'LOW END horizontal distance (m)' : positionX_small,
    # 'LOW END horizontal acceleration (m/s^2)' : accelerationX_small,
    # 'LOW END vertical acceleration (m/s^2)' : accelerationY_small,
    # 'LOW END mach array' : mach_array_small,
    # 'LOW END dynamic pressure array' : dynamic_pressure_array_small,
    # 'LOW END orientation array' : orientation_small,
    # }

    with open('OUTPUT.csv','w') as output_file:
        w = csv.writer(output_file)
        for key, val in output_dictionary.items():
            if type(val) == numpy.ndarray:
                val = numpy.round(val, 4)
            else:
                val = round(val,3)
            w.writerow([key,val])

    # with open('OTHER_OUTPUT.csv','w') as other_output_file:
    #     v = csv.writer(other_output_file)
    #     for key, val in other_output_dictionary.items():
    #         v.writerow([key,val])
    #return(positionY, totalTime, rocket_height)

if __name__ == '__main__':
    main()