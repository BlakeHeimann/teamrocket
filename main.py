from stage import Stage
from INPUT import *
from structure import skin_density, stiffener_density
from propulsion import delta_v, propulsion_analysis
from configuration import payload_housing_mass, skin_thickness, center_of_mass, center_of_pressure, dynamic_center_of_mass_center_of_pressure
from adcs import environmental_torque_calculation, fin_actuator_calculation
from power_thermal import power_thermal_calculation
import numpy as numpy
import csv

#necessary to calculate structure for the payload fairing stage. 
#Also had to make these equal to one to avoid a division by zero error, but they aren't used so it won't affect anything
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

#center of mass and center of pressure
(total_center_of_mass,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height,nosecone_mass,fin_mass) = center_of_mass(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,outside_diameter)
(slv_cop_from_nose,slv_cop_from_origin,slv_cop_from_nose_minus_stage_1,slv_cop_from_origin_minus_stage_1) = center_of_pressure(outside_diameter,outside_radius,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height) # pylint: disable=unbalanced-tuple-unpacking

#This needs to be done outside of creating the stages as the combined masses depend on the masses of other stages 
payload_fairing.combined_mass = payload_fairing.mass + payload_mass + payload_housing_mass + nosecone_mass
stage3.combined_mass = stage3.mass + payload_fairing.combined_mass
stage2.combined_mass = stage2.mass + stage3.combined_mass
stage1.combined_mass = stage1.mass + stage2.combined_mass

#delta v is based on the combined masses so this also needs to be separate
stage1.delta_v = delta_v(stage1)
stage2.delta_v = delta_v(stage2)
stage3.delta_v = delta_v(stage3)

#need to fix this
stage1.coastTime = stage1_coastTime #s
stage2.coastTime = stage2_coastTime #s

(dynamic_mass,dynamic_cop) = dynamic_center_of_mass_center_of_pressure(stage1,stage2,stage3,payload_fairing,fin_mass,nosecone_mass,payload_mass,slv_cop_from_nose,slv_cop_from_nose_minus_stage_1)

#doing this avoids an annoying error that pops up when trying to find the max value of the dynamic pressure array, not sure why but it gives the correct value so 
numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)

(positionX,positionY,velocityX,velocityY,accelerationX,accelerationY,mach_array,dynamic_pressure_array,orientation) = propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass)

#ADCS
environmental_torques = environmental_torque_calculation(stage1,stage2,stage3,positionY,orientation)
fin_actuator_torque = fin_actuator_calculation(velocityX,velocityY)

#Thermal/Power
(real_battery_capacity,heat_generated_per_second) = power_thermal_calculation(stage1,stage2,stage3)
print("Real required battery capacity: "+str(real_battery_capacity)+" Wh")
print("Battery cell heat generation: "+str(heat_generated_per_second)+" J/s")


print('The altitude at the end of the flight is:', round(*positionY[len(positionY)-1],2), 'm')

max_dynamic_pressure = numpy.amax(dynamic_pressure_array)
time_of_max_dynamic_pressure = numpy.argmax(dynamic_pressure_array)
absolute_val_array = numpy.absolute(mach_array - 1)
time_of_supersonic = absolute_val_array.argmin()
print('The maximum dynamic pressure felt on the vehicle is:', round(*max_dynamic_pressure,2), 'Pa at ', time_of_max_dynamic_pressure, 'seconds')
print('The time when the rocket will reach supersonic flight is ',time_of_supersonic,'seconds')


output_dictionary = {'rocket center of mass' : total_center_of_mass, 'center of pressure measured from nose' : slv_cop_from_nose, 'time of supersonic flight' : time_of_supersonic, 'max dynamic pressure' : max_dynamic_pressure, 
'time of max dynamic pressure' : time_of_max_dynamic_pressure, 'stage 1 total mass' : stage1.mass,'stage 2 total mass': stage2.mass, 'stage 3 total mass' : stage3.mass, 'payload fairing total mass' : payload_fairing.combined_mass - nosecone_mass,
 'nosecone total mass' : nosecone_mass, 'stage 1 delta v' : stage1.delta_v, 'stage 2 delta v' : stage2.delta_v, 'stage 3 delta v' : stage3.delta_v, 'fin actuator torque' : fin_actuator_torque, 
 'battery capacity' : real_battery_capacity, 'battery heat generation per second' : heat_generated_per_second, 'altitude at the end of flight' : round(*positionY[len(positionY)-1],2)}

with open('OUTPUT.csv','w') as output_file:
    w = csv.writer(output_file)
    for key, val in output_dictionary.items():
        w.writerow([key,val])

    