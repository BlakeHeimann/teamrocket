import math as math
import numpy as numpy
from Structures_Python_Blake import stage1,stage2,stage3,fairing,outside_radius,outside_diameter,skin_density
from Propulsion_Python_Blake_BradenUpdate import totalTime
from Propulsion_Python_Blake_BradenUpdate import stage1 as stage_one_prop
from Propulsion_Python_Blake_BradenUpdate import stage2 as stage_two_prop
from Propulsion_Python_Blake_BradenUpdate import stage3 as stage_three_prop


wing_thickness = 0.03 #m
skin_thickness = 0.0025

payload_mass = 5 #kg
payload_housing_mass = 48 #kg

payload_distance = fairing.height/2
payload_housing_distance = fairing.height/2

stage1_wing_lower_volume = 4*wing_thickness*(outside_diameter/2)*outside_diameter
stage1_wing_upper_volume = stage1_wing_lower_volume/2

stage1_wing_lower_mass = skin_density*stage1_wing_lower_volume
stage1_wing_upper_mass = skin_density*stage1_wing_upper_volume
wing_mass = stage1_wing_lower_mass + stage1_wing_upper_mass

stage1_wing_lower_distance = outside_diameter/4
stage1_wing_upper_distance = outside_diameter*(2/3)

nosecone_height_factor = 1.741714286
nosecone_height = outside_diameter*nosecone_height_factor
nosecone_lower_height = .75*nosecone_height
nosecone_upper_height = .25*nosecone_height
nosecone_lower_radius = outside_radius
nosecone_upper_radius = outside_radius/3

nosecone_lower_volume = (1/3)*math.pi*nosecone_lower_height*(nosecone_upper_radius**2 + nosecone_upper_radius*nosecone_lower_radius + nosecone_lower_radius**2) - (1/3)*math.pi*nosecone_lower_height*((nosecone_upper_radius-skin_thickness)**2 + (nosecone_upper_radius-skin_thickness)*(nosecone_lower_radius-skin_thickness) + (nosecone_lower_radius-skin_thickness)**2)
nosecone_upper_volume = (1/3)*math.pi*nosecone_upper_height*((nosecone_upper_radius)**2 - (nosecone_upper_radius - skin_thickness)**2)
nosecone_lower_mass = skin_density*nosecone_lower_volume
nosecone_upper_mass = skin_density*nosecone_upper_volume
nosecone_mass = nosecone_lower_mass + nosecone_upper_mass

nosecone_upper_distance = nosecone_upper_height/3
nosecone_lower_distance = nosecone_lower_height/3

rocket_height = stage1.height + stage2.height + stage3.height + fairing.height + nosecone_height

stage1_center_of_mass = (stage1.structure_mass*(stage1.height/2) + stage1.stiffener.mass*(stage1.height/2) + stage1.circular_rib.mass*(stage1.height/2) + stage1.engine_mass*(stage1.height/2) + stage1_wing_upper_mass*stage1_wing_upper_distance + stage1_wing_lower_mass*stage1_wing_lower_distance)/(stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass)
stage2_center_of_mass = stage1.height + (stage2.structure_mass*(stage2.height/2) + stage2.stiffener.mass*(stage2.height/2) + stage2.circular_rib.mass*(stage2.height/2) + stage2.engine_mass*(stage2.height/2) )/(stage2.mass)
stage3_center_of_mass = stage1.height + stage2.height + (stage3.structure_mass*(stage3.height/2) + stage3.stiffener.mass*(stage3.height/2) + stage3.circular_rib.mass*(stage3.height/2) + stage3.engine_mass*(stage3.height/2) )/(stage3.mass)
fairing_center_of_mass = stage1.height + stage2.height + stage3.height + (fairing.structure_mass*(fairing.height/2) + fairing.stiffener.mass*(fairing.height/2) + fairing.circular_rib.mass*(fairing.height/2) + fairing.engine_mass*(fairing.height/2) +payload_mass*payload_distance + payload_housing_mass*payload_housing_distance)/(fairing.mass + payload_mass + payload_housing_mass)
nosecone_center_of_mass = stage1.height + stage2.height + stage3.height + fairing.height + (nosecone_lower_mass*nosecone_lower_distance + nosecone_upper_mass*nosecone_upper_distance)/(nosecone_lower_mass + nosecone_upper_mass)


total_center_of_mass = (stage1_center_of_mass*(stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass) + stage2_center_of_mass*stage2.mass + stage3_center_of_mass*stage3.mass + fairing_center_of_mass*(fairing.mass + payload_mass + payload_housing_mass) + nosecone_center_of_mass*(nosecone_lower_mass + nosecone_upper_mass))/((stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass) + stage2.mass + stage3.mass + (fairing.mass + payload_mass + payload_housing_mass) + (nosecone_lower_mass + nosecone_upper_mass))

# print(stage1_center_of_mass)
# print(stage2_center_of_mass)
# print(stage3_center_of_mass)
# print(fairing_center_of_mass)
# print(nosecone_center_of_mass)
# print(total_center_of_mass)

span_length_chord_fins = math.sqrt((outside_diameter)**2 + (outside_radius+(outside_radius/2)-(outside_radius))**2)

nosecone_upper_normal = 2
nosecone_upper_cop = (2/3)*nosecone_upper_height

nosecone_lower_normal = 2*((nosecone_lower_radius/nosecone_upper_radius)**2 - (nosecone_upper_radius/nosecone_upper_radius)**2)
nosecone_lower_cop = nosecone_upper_height + (nosecone_lower_height/3)*(1+((1-(nosecone_upper_radius/nosecone_lower_radius))/(1-(nosecone_upper_radius/nosecone_lower_radius)**2)))

body_interference_factor = 1+(nosecone_upper_radius)/(outside_diameter + nosecone_upper_radius)
fin_normal_force = (16*(outside_diameter/(nosecone_upper_radius*2))**2)/(1+math.sqrt(1+((2*span_length_chord_fins)/(outside_diameter+outside_radius))**2))
fin_normal_force_with_body = body_interference_factor*fin_normal_force
fin_cop = (rocket_height-outside_radius) + (((outside_radius*(outside_diameter + 2*outside_radius)))/(3*(outside_radius + outside_diameter)))+(1/6*(outside_diameter+outside_radius-((outside_radius*outside_diameter)/(outside_diameter+outside_radius))))

# SLV_minus_stage_1_fin_cop = (rocket_height-stage1.height) + (((outside_radius*(outside_diameter + 2*outside_radius)))/(3*(outside_radius + outside_diameter)))+(1/6*(outside_diameter+outside_radius-((outside_radius*outside_diameter)/(outside_diameter+outside_radius))))
# SLV_minus_stage_1_and_2_fin_cop = (rocket_height-stage1.height-stage2.height) + (((outside_radius*(outside_diameter + 2*outside_radius)))/(3*(outside_radius + outside_diameter)))+(1/6*(outside_diameter+outside_radius-((outside_radius*outside_diameter)/(outside_diameter+outside_radius))))
# SLV_minus_stage_1_and_2_and_3_fin_cop = (rocket_height-stage1.height-stage2.height-stage3.height) + (((outside_radius*(outside_diameter + 2*outside_radius)))/(3*(outside_radius + outside_diameter)))+(1/6*(outside_diameter+outside_radius-((outside_radius*outside_diameter)/(outside_diameter+outside_radius))))

slv_normal_force_minus_stage_1 = nosecone_upper_normal + nosecone_lower_normal
slv_cop_from_nose_minus_stage_1 = ((nosecone_upper_normal*nosecone_upper_cop)+(nosecone_lower_normal*nosecone_lower_cop))/(slv_normal_force_minus_stage_1)
slv_cop_from_origin_minus_stage_1 = rocket_height - slv_cop_from_nose_minus_stage_1

slv_normal_force = nosecone_upper_normal + nosecone_lower_normal + fin_normal_force_with_body
slv_cop_from_nose = ((nosecone_upper_normal*nosecone_upper_cop)+(nosecone_lower_normal*nosecone_lower_cop)+(fin_normal_force_with_body*fin_cop))/(slv_normal_force)
slv_cop_from_origin = rocket_height - slv_cop_from_nose
# print(slv_normal_force_minus_stage_1)
# print(slv_cop_from_nose_minus_stage_1)
# print(slv_cop_from_origin_minus_stage_1)

##Dynamic Mass section
dynamic_mass = numpy.zeros((totalTime,2))
dynamic_cop = numpy.zeros((totalTime,2))

dynamic_mass[:,0] = numpy.arange(0,totalTime)
dynamic_cop[:,0] = numpy.arange(0,totalTime)


for t in range(totalTime):
    if(t == 0):
        dynamic_mass[t,1] = stage1.mass + stage2.mass + stage3.mass + wing_mass + nosecone_mass + payload_mass + payload_housing_mass
        dynamic_cop[t,1] = slv_cop_from_nose
    elif(t < stage_one_prop.burnTime):
        dynamic_mass[t,1] = stage1.mass + stage2.mass + stage3.mass + wing_mass + nosecone_mass + payload_mass + payload_housing_mass - 202.7*t
        dynamic_cop[t,1] = slv_cop_from_nose
    elif(t < stage_one_prop.burnTime+stage_one_prop.coastTime):
        dynamic_mass[t,1] = stage2.mass + stage3.mass + nosecone_mass + payload_mass + payload_housing_mass
        dynamic_cop[t,1] = slv_cop_from_nose_minus_stage_1
    elif(t < stage_one_prop.burnTime + stage_one_prop.coastTime + stage_two_prop.burnTime):
        dynamic_mass[t,1] = stage2.mass + stage3.mass + nosecone_mass + payload_mass + payload_housing_mass - 79.38*(t-stage_one_prop.burnTime - stage_one_prop.coastTime)
        dynamic_cop[t,1] = slv_cop_from_nose_minus_stage_1
    elif(t < stage_one_prop.burnTime+stage_one_prop.coastTime+stage_two_prop.burnTime+stage_two_prop.coastTime):
        dynamic_mass[t,1] = stage3.mass + nosecone_mass + payload_mass + payload_housing_mass
        dynamic_cop[t,1] = slv_cop_from_nose_minus_stage_1
    elif(t < stage_one_prop.burnTime+stage_one_prop.coastTime+stage_two_prop.burnTime+stage_two_prop.coastTime + stage_three_prop.burnTime):
        dynamic_mass[t,1] = stage3.mass + nosecone_mass + payload_mass + payload_housing_mass - 38.3*(t-stage_one_prop.burnTime - stage_one_prop.coastTime - stage_two_prop.burnTime - stage_two_prop.coastTime)
        dynamic_cop[t,1] = slv_cop_from_nose_minus_stage_1
    else:
        dynamic_mass[t,1] = nosecone_mass + payload_mass + payload_housing_mass
        dynamic_cop[t,1] = slv_cop_from_nose_minus_stage_1

# print(dynamic_mass)
# print(dynamic_cop)

# print(stage1.mass)
# print(stage2.mass)
# print(stage3.mass) 
# print(wing_mass)
# print(nosecone_mass)
# print(payload_mass)
# print(payload_housing_mass)