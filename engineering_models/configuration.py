import math as math
import numpy as numpy
from lib.structure import skin_density


def center_of_mass(stage1,stage2,stage3,payload_fairing,payload_mass,outside_diameter):
    payload_distance = payload_fairing.height/2
    payload_housing_distance = payload_fairing.height/2

    #assuming 4 fins
    stage1_fin_lower_volume = 4*fin_thickness*(outside_diameter/2)*outside_diameter
    stage1_fin_upper_volume = stage1_fin_lower_volume/2

    stage1_fin_lower_mass = skin_density*stage1_fin_lower_volume
    stage1_fin_upper_mass = skin_density*stage1_fin_upper_volume
    fin_mass = stage1_fin_lower_mass + stage1_fin_upper_mass

    stage1_fin_lower_distance = outside_diameter/4
    stage1_fin_upper_distance = outside_diameter*(2/3)

    nosecone_fineness_ratio = 1.741714286
    nosecone_height = outside_diameter*nosecone_fineness_ratio
    nosecone_lower_height = .75*nosecone_height
    nosecone_upper_height = .25*nosecone_height
    nosecone_lower_radius = outside_diameter/2
    nosecone_upper_radius = outside_diameter/6

    nosecone_lower_volume = (1/3)*math.pi*nosecone_lower_height*(nosecone_upper_radius**2 + nosecone_upper_radius*nosecone_lower_radius + nosecone_lower_radius**2) - (1/3)*math.pi*nosecone_lower_height*((nosecone_upper_radius-skin_thickness)**2 + (nosecone_upper_radius-skin_thickness)*(nosecone_lower_radius-skin_thickness) + (nosecone_lower_radius-skin_thickness)**2)
    nosecone_upper_volume = (1/3)*math.pi*nosecone_upper_height*((nosecone_upper_radius)**2 - (nosecone_upper_radius - skin_thickness)**2)
    nosecone_lower_mass = skin_density*nosecone_lower_volume
    nosecone_upper_mass = skin_density*nosecone_upper_volume
    nosecone_mass = nosecone_upper_mass + nosecone_lower_mass

    nosecone_upper_distance = nosecone_upper_height/3
    nosecone_lower_distance = nosecone_lower_height/3

    rocket_height = stage1.height + stage2.height + stage3.height + payload_fairing.height + nosecone_height

    stage1_center_of_mass = (stage1.structure_mass*(stage1.height/2) + stage1.stiffener.mass*(stage1.height/2) + stage1.circular_rib.mass*(stage1.height/2) + stage1.engine_mass*(stage1.height/2) + stage1.propellant_mass*(stage1.height/2) + stage1_fin_upper_mass*stage1_fin_upper_distance + stage1_fin_lower_mass*stage1_fin_lower_distance)/(stage1.mass + stage1_fin_lower_mass + stage1_fin_upper_mass)
    try:
        stage2_center_of_mass = stage1.height + (stage2.structure_mass*(stage2.height/2) + stage2.stiffener.mass*(stage2.height/2) + stage2.circular_rib.mass*(stage2.height/2) + stage2.engine_mass*(stage2.height/2) + stage2.propellant_mass*(stage2.height/2))/(stage2.mass)
    except ZeroDivisionError:
        stage2_center_of_mass = 0
    try:
        stage3_center_of_mass = stage1.height + stage2.height + (stage3.structure_mass*(stage3.height/2) + stage3.stiffener.mass*(stage3.height/2) + stage3.circular_rib.mass*(stage3.height/2) + stage3.engine_mass*(stage3.height/2) + stage3.propellant_mass*(stage3.height/2))/(stage3.mass)
    except ZeroDivisionError:
        stage3_center_of_mass = 0
    payload_fairing_center_of_mass = stage1.height + stage2.height + stage3.height + (payload_fairing.structure_mass*(payload_fairing.height/2) + payload_fairing.stiffener.mass*(payload_fairing.height/2) + payload_fairing.circular_rib.mass*(payload_fairing.height/2) + payload_fairing.engine_mass*(payload_fairing.height/2) +payload_mass*payload_distance + payload_housing_mass*payload_housing_distance)/(payload_fairing.mass + payload_mass + payload_housing_mass)
    nosecone_center_of_mass = stage1.height + stage2.height + stage3.height + payload_fairing.height + (nosecone_lower_mass*nosecone_lower_distance + nosecone_upper_mass*nosecone_upper_distance)/(nosecone_lower_mass + nosecone_upper_mass)

    total_center_of_mass = (stage1_center_of_mass*(stage1.mass + stage1_fin_lower_mass + stage1_fin_upper_mass) + stage2_center_of_mass*stage2.mass + stage3_center_of_mass*stage3.mass + payload_fairing_center_of_mass*(payload_fairing.mass + payload_mass + payload_housing_mass) + nosecone_center_of_mass*(nosecone_lower_mass + nosecone_upper_mass))/((stage1.mass + stage1_fin_lower_mass + stage1_fin_upper_mass) + stage2.mass + stage3.mass + (payload_fairing.mass + payload_mass + payload_housing_mass) + (nosecone_lower_mass + nosecone_upper_mass))

    return (total_center_of_mass,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height,nosecone_mass,fin_mass,stage1_center_of_mass,stage2_center_of_mass,stage3_center_of_mass,payload_fairing_center_of_mass,nosecone_center_of_mass)
def center_of_pressure(outside_diameter,outside_radius,nosecone_upper_height,nosecone_lower_height,nosecone_upper_radius,nosecone_lower_radius,rocket_height):
    span_length_chord_fins = math.sqrt((outside_diameter)**2 + (outside_radius+(outside_radius/2)-(outside_radius))**2)

    nosecone_upper_normal = 2
    nosecone_upper_cop = (2/3)*nosecone_upper_height

    nosecone_lower_normal = 2*((nosecone_lower_radius/nosecone_upper_radius)**2 - (nosecone_upper_radius/nosecone_upper_radius)**2)
    nosecone_lower_cop = nosecone_upper_height + (nosecone_lower_height/3)*(1+((1-(nosecone_upper_radius/nosecone_lower_radius))/(1-(nosecone_upper_radius/nosecone_lower_radius)**2)))

    body_interference_factor = 1+(nosecone_upper_radius)/(outside_diameter + nosecone_upper_radius)
    fin_normal_force = (16*(outside_diameter/(nosecone_upper_radius*2))**2)/(1+math.sqrt(1+((2*span_length_chord_fins)/(outside_diameter+outside_radius))**2))
    fin_normal_force_with_body = body_interference_factor*fin_normal_force
    fin_cop = (rocket_height-outside_radius) + (((outside_radius*(outside_diameter + 2*outside_radius)))/(3*(outside_radius + outside_diameter)))+(1/6*(outside_diameter+outside_radius-((outside_radius*outside_diameter)/(outside_diameter+outside_radius))))

    slv_normal_force_minus_stage_1 = nosecone_upper_normal + nosecone_lower_normal
    slv_cop_from_nose_minus_stage_1 = ((nosecone_upper_normal*nosecone_upper_cop)+(nosecone_lower_normal*nosecone_lower_cop))/(slv_normal_force_minus_stage_1)
    slv_cop_from_origin_minus_stage_1 = rocket_height - slv_cop_from_nose_minus_stage_1

    slv_normal_force = nosecone_upper_normal + nosecone_lower_normal + fin_normal_force_with_body
    slv_cop_from_nose = ((nosecone_upper_normal*nosecone_upper_cop)+(nosecone_lower_normal*nosecone_lower_cop)+(fin_normal_force_with_body*fin_cop))/(slv_normal_force)
    slv_cop_from_origin = rocket_height - slv_cop_from_nose
    return(slv_cop_from_nose,slv_cop_from_origin,slv_cop_from_nose_minus_stage_1,slv_cop_from_origin_minus_stage_1)

def dynamic_center_of_mass_center_of_pressure(stage1,stage2,stage3,fin_mass,nosecone_mass,payload_mass,slv_cop_from_nose,slv_cop_from_nose_minus_stage_1,stage1_center_of_mass,stage2_center_of_mass,stage3_center_of_mass,payload_fairing_center_of_mass,nosecone_center_of_mass):
    totalburn_time = stage1.burn_time + stage2.burn_time + stage3.burn_time
    totalCoastTime = stage1.coastTime + stage2.coastTime + stage3.coastTime
    totalTime = totalburn_time + totalCoastTime

    dynamic_mass = numpy.zeros(totalTime)
    dynamic_com = numpy.zeros(totalTime)
    dynamic_cop = numpy.zeros(totalTime)



    for t in range(totalTime):
        if(t == 0):
            dynamic_mass[t] = stage1.mass + stage2.mass + stage3.mass + fin_mass + nosecone_mass + payload_mass + payload_housing_mass
            dynamic_com[t] = (stage1.mass*stage1_center_of_mass + stage2.mass*stage2_center_of_mass + stage3.mass*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]
            dynamic_cop[t] = slv_cop_from_nose
        elif(t < stage1.burn_time):
            dynamic_mass[t] = stage1.mass + stage2.mass + stage3.mass + fin_mass + nosecone_mass + payload_mass + payload_housing_mass - 202.7*t
            dynamic_com[t] = ((stage1.mass- 202.7*t)*stage1_center_of_mass + stage2.mass*stage2_center_of_mass + stage3.mass*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]
            dynamic_cop[t] = slv_cop_from_nose
        elif(t < stage1.burn_time+stage1.coastTime):
            dynamic_mass[t] = stage2.mass + stage3.mass + nosecone_mass + payload_mass + payload_housing_mass
            dynamic_com[t] = (stage2.mass*stage2_center_of_mass + stage3.mass*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]           
            dynamic_cop[t] = slv_cop_from_nose_minus_stage_1
        elif(t < stage1.burn_time + stage1.coastTime + stage2.burn_time):
            dynamic_mass[t] = stage2.mass + stage3.mass + nosecone_mass + payload_mass + payload_housing_mass - 79.38*(t-stage1.burn_time - stage1.coastTime)
            dynamic_com[t] = ((stage2.mass - 79.38*(t-stage1.burn_time - stage1.coastTime))*stage2_center_of_mass + stage3.mass*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]           
            dynamic_cop[t] = slv_cop_from_nose_minus_stage_1
        elif(t < stage1.burn_time+stage1.coastTime+stage2.burn_time+stage2.coastTime):
            dynamic_mass[t] = stage3.mass + nosecone_mass + payload_mass + payload_housing_mass
            dynamic_com[t] = (stage3.mass*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]            
            dynamic_cop[t] = slv_cop_from_nose_minus_stage_1
        elif(t < stage1.burn_time+stage1.coastTime+stage2.burn_time+stage2.coastTime + stage3.burn_time):
            dynamic_mass[t] = stage3.mass + nosecone_mass + payload_mass + payload_housing_mass - 38.3*(t-stage1.burn_time - stage1.coastTime - stage2.burn_time - stage2.coastTime)
            dynamic_com[t] = ((stage3.mass-38.3*(t-stage1.burn_time - stage1.coastTime - stage2.burn_time - stage2.coastTime))*stage3_center_of_mass + nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]              
            dynamic_cop[t] = slv_cop_from_nose_minus_stage_1
        else:
            dynamic_mass[t] = nosecone_mass + payload_mass + payload_housing_mass
            dynamic_com[t] = (nosecone_mass*nosecone_center_of_mass + (payload_mass + payload_housing_mass)*payload_fairing_center_of_mass)/dynamic_mass[t]              
            dynamic_cop[t] = slv_cop_from_nose_minus_stage_1
    return(dynamic_mass,dynamic_com,dynamic_cop)

#assuming 0.03 meter thick fins
fin_thickness = 0.03 #m

#assuming 0.0025 meters for all vehicle skin thickness
skin_thickness = 0.0025

payload_housing_mass = 48 #kg
