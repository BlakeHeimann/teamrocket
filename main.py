from stage import Stage
from structure import skin_density, stiffener_density
from propulsion import delta_v, propulsion_analysis
from configuration import payload_housing_mass, skin_thickness, center_of_mass, center_of_pressure, dynamic_center_of_mass_center_of_pressure
import numpy as numpy

# INPUTS
outside_diameter = 1.405        #m
stage1_height = 7.5             #m
stage2_height = 3.35            #m
stage3_height = 2.1             #m
payload_fairing_height = 1      #m
payload_mass = 5                #kg

stage1_propellant_mass = 15000  #kg
stage1_engine_mass = 1779       #kg
stage1_thrust = 469054 #N
stage1_burnTime = 74 #s
stage1_isp = 2314/9.81 #1/2

stage2_propellant_mass = 5080   #kg
stage2_engine_mass = 527        #kg
stage2_thrust = 220345 #N
stage2_burnTime = 64 #s
stage2_isp = 2776/9.81 #1/2

stage3_propellant_mass = 1760   #kg
stage3_engine_mass = 189        #kg
stage3_thrust = 106212 #N
stage3_burnTime = 46 #s
stage3_isp = 2776/9.81 #1/2


#necessary to calculate structure for the payload fairing stage. Also had to make these equal to one to avoid a division by zero error, but they aren't used so it won't affect anything
payload_fairing_propellant_mass = 1     
payload_fairing_engine_mass = 1
payload_fairing_thrust = 1
payload_fairing_burnTime = 1
payload_fairing_isp = 1

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

#This can be made an INPUT
stage1.coastTime = 51 #s
stage2.coastTime = 164 #s

(dynamic_mass,dynamic_cop) = dynamic_center_of_mass_center_of_pressure(stage1,stage2,stage3,payload_fairing,fin_mass,nosecone_mass,payload_mass,slv_cop_from_nose,slv_cop_from_nose_minus_stage_1)

#doing this avoids an annoying error that pops up when trying to find the max value of the dynamic pressure array, not sure why but it gives the correct value so 
numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)

(positionX,positionY,velocityX,velocityY,accelerationX,accelerationY,mach_array,dynamic_pressure_array) = propulsion_analysis(stage1,stage2,stage3,payload_fairing,payload_mass,payload_housing_mass,nosecone_mass)

print('The altitude at the end of the flight is:', round(*positionY[len(positionY)-1],2), 'm')

max_dynamic_pressure = numpy.amax(dynamic_pressure_array)
time_of_max_dynamic_pressure = numpy.argmax(dynamic_pressure_array)
absolute_val_array = numpy.absolute(mach_array - 1)
time_of_supersonic = absolute_val_array.argmin()
print('The maximum dynamic pressure felt on the vehicle is:', round(*max_dynamic_pressure,2), 'Pa at ', time_of_max_dynamic_pressure, 'seconds')
print('The time when the rocket will reach supersonic flight is ',time_of_supersonic,'seconds')
#print(positionY)