import math as math
from Structures_Python_Blake import *

wing_thickness = 0.03 #m
skin_thickness = 0.0025

payload_mass = 5 #kg
payload_housing_mass = 48 #kg

payload_distance = fairing_height/2
payload_housing_distance = fairing_height/2

stage1_wing_lower_volume = 4*wing_thickness*(outside_diameter/2)*outside_diameter
stage1_wing_upper_volume = stage1_wing_lower_volume/2

stage1_wing_lower_mass = skin_density*stage1_wing_lower_volume
stage1_wing_upper_mass = skin_density*stage1_wing_upper_volume

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

nosecone_upper_distance = nosecone_upper_height/3
nosecone_lower_distance = nosecone_lower_height/3

stage1_center_of_mass = (stage1.structure_mass*(stage1.height/2) + stage1.stiffener.mass*(stage1.height/2) + stage1.circular_rib.mass*(stage1.height/2) + stage1.engine_mass*(stage1.height/2) + stage1_wing_upper_mass*stage1_wing_upper_distance + stage1_wing_lower_mass*stage1_wing_lower_distance)/(stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass)
stage2_center_of_mass = stage1.height + (stage2.structure_mass*(stage2.height/2) + stage2.stiffener.mass*(stage2.height/2) + stage2.circular_rib.mass*(stage2.height/2) + stage2.engine_mass*(stage2.height/2) )/(stage2.mass)
stage3_center_of_mass = stage1.height + stage2.height + (stage3.structure_mass*(stage3.height/2) + stage3.stiffener.mass*(stage3.height/2) + stage3.circular_rib.mass*(stage3.height/2) + stage3.engine_mass*(stage3.height/2) )/(stage3.mass)
fairing_center_of_mass = stage1.height + stage2.height + stage3.height + (fairing.structure_mass*(fairing.height/2) + fairing.stiffener.mass*(fairing.height/2) + fairing.circular_rib.mass*(fairing.height/2) + fairing.engine_mass*(fairing.height/2) +payload_mass*payload_distance + payload_housing_mass*payload_housing_distance)/(fairing.mass + payload_mass + payload_housing_mass)
nosecone_center_of_mass = stage1.height + stage2.height + stage3.height + fairing.height + (nosecone_lower_mass*nosecone_lower_distance + nosecone_upper_mass*nosecone_upper_distance)/(nosecone_lower_mass + nosecone_upper_mass)

print(stage1_center_of_mass)
print(stage2_center_of_mass)
print(stage3_center_of_mass)
print(fairing_center_of_mass)
print(nosecone_center_of_mass)

total_center_of_mass = (stage1_center_of_mass*(stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass) + stage2_center_of_mass*stage2.mass + stage3_center_of_mass*stage3.mass + fairing_center_of_mass*(fairing.mass + payload_mass + payload_housing_mass) + nosecone_center_of_mass*(nosecone_lower_mass + nosecone_upper_mass))/((stage1.mass + stage1_wing_lower_mass + stage1_wing_upper_mass) + stage2.mass + stage3.mass + (fairing.mass + payload_mass + payload_housing_mass) + (nosecone_lower_mass + nosecone_upper_mass))
print(total_center_of_mass)
