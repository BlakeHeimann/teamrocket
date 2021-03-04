import math as math

class skin:
    def __init__(self,height,inside_radius,outside_radius,skin_density):
        self.inside_volume = math.pi*height*inside_radius**2
        self.outside_volume = math.pi*height*outside_radius**2
        self.total_volume = self.outside_volume - self.inside_volume
        self.mass = self.total_volume*skin_density

class stiffener:
    def __init__(self,height,stiffener_radius,stiffener_density,number_of_stiffeners):
        self.volume = math.pi*height*stiffener_radius**2
        self.mass = number_of_stiffeners*self.volume*stiffener_density

class circular_rib:
    def __init__(self,mass_of_rib,number_of_ribs):
        self.mass = number_of_ribs*mass_of_rib

class stage:
    def __init__(self,height,inside_radius,outside_radius,stiffener_radius,skin_density,stiffener_density,circular_rib_mass,number_of_ribs,number_of_stiffeners,engine_mass):
        self.skin = skin(height,inside_radius,outside_radius,skin_density)
        self.stiffener = stiffener(height,stiffener_radius,stiffener_density,number_of_stiffeners)
        self.circular_rib = circular_rib(circular_rib_mass,number_of_ribs)
        self.structure_mass = self.skin.mass + self.stiffener.mass + self.circular_rib.mass
        self.Pcrit = (buckling_coefficient*math.pi**2*elastic_modulus*moment_of_inertia)/(height**2)
        self.height = height
        self.engine_mass = engine_mass
        self.mass = self.engine_mass + self.structure_mass

# INPUTS
outside_diameter = 1.405        #m
inside_diameter = 1.4           #m
skin_density = 2710             #kg/m^3
stiffener_density = 4700        #kg/m^3
elastic_modulus = 69000000000   #Pa
buckling_coefficient = 0.25     
stiffener_radius = 0.0025       #m
stage1_height = 7.5             #m
stage2_height = 3.35            #m
stage3_height = 2.1             #m
fairing_height = 1              #m
number_of_stiffeners = 16
circular_rib_mass = 0.40661 #kg
stage1_ribs = 5
stage2_ribs = 3
stage3_ribs = 3
fairing_ribs = 1

stage1_engine_mass = 16779
stage2_engine_mass = 5607
stage3_engine_mass = 1949
fairing_engine_mass = 0

inside_radius = inside_diameter/2
outside_radius = outside_diameter/2

#Moment of Inertia
moment_of_inertia = math.pi*(outside_diameter**4-inside_diameter**4)/64

#Creating Stages
stage1 = stage(stage1_height,inside_radius,outside_radius,stiffener_radius,skin_density,stiffener_density,circular_rib_mass,stage1_ribs,number_of_stiffeners, stage1_engine_mass)
stage2 = stage(stage2_height,inside_radius,outside_radius,stiffener_radius,skin_density,stiffener_density,circular_rib_mass,stage2_ribs,number_of_stiffeners, stage2_engine_mass)
stage3 = stage(stage3_height,inside_radius,outside_radius,stiffener_radius,skin_density,stiffener_density,circular_rib_mass,stage3_ribs,number_of_stiffeners, stage3_engine_mass)
fairing = stage(fairing_height,inside_radius,outside_radius,stiffener_radius,skin_density,stiffener_density,circular_rib_mass,fairing_ribs,number_of_stiffeners, fairing_engine_mass)

#Adding Masses
skin_mass_total = stage1.skin.mass + stage2.skin.mass + stage3.skin.mass + fairing.skin.mass
stiffener_mass_total = stage1.stiffener.mass + stage2.stiffener.mass + stage3.stiffener.mass + fairing.stiffener.mass
circular_rib_mass_total = stage1.circular_rib.mass + stage2.circular_rib.mass + stage3.circular_rib.mass + fairing.circular_rib.mass
total_structure_mass = stage1.structure_mass + stage2.structure_mass + stage3.structure_mass + fairing.structure_mass

# print('moment of inertia:', round(moment_of_inertia,4), 'm^4')
# print('stage1 Pcritical:', round(stage1.Pcrit,2), 'N')
# print('stage2 Pcritical:', round(stage2.Pcrit,2), 'N')
# print('stage3 Pcritical:', round(stage3.Pcrit,2), 'N')
# print('fairing Pcritical:', round(fairing.Pcrit,2), 'N')

# print('total skin mass:', round(skin_mass_total,2), 'kg')
# print('total stiffer mass:', round(stiffener_mass_total,2), 'kg')
# print('total circular rib mass:', round(circular_rib_mass_total,2), 'kg')

# print('stage 1 total mass:', round(stage1.structure_mass,2), 'kg')
# print('stage 2 total mass:', round(stage2.structure_mass,2), 'kg')
# print('stage 3 total mass:', round(stage3.structure_mass,2), 'kg')
# print('fairing total mass:', round(fairing.structure_mass,2), 'kg')

# print('total structure mass:', round(total_structure_mass,2), 'kg')