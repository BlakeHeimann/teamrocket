import math as math

class Skin:
    def __init__(self,height,inside_radius,outside_radius,skin_density):
        self.total_volume = math.pi*height*outside_radius**2 - math.pi*height*inside_radius**2
        self.mass = self.total_volume*skin_density

class Stiffener:
    def __init__(self,height,stiffener_density):
        #assuming stiffener radius of .0025
        self.volume = math.pi*height*0.0025**2
        #assuming 16 stiffeners
        self.mass = 16*self.volume*stiffener_density

class Circular_Rib:
    def __init__(self,height,outside_radius):
        # Our original circular rib mass was 0.40661, we are using this number as our constant to deal with scaling up and down
        self.circular_rib_mass = 0.57880427*outside_radius #kg
        #Here I'm assuming roughly for every meter in the structure there will be a rib. This results in one more rib than we had in our design though
        self.number_of_ribs = math.floor(height)
        self.mass = self.number_of_ribs*self.circular_rib_mass

def Moment_of_Inertia(outside_diameter,inside_diameter):
    return math.pi*(outside_diameter**4-inside_diameter**4)/64

#Constants
skin_density = 2710             #kg/m^3  #Al-Li 2195
stiffener_density = 4700        #kg/m^3  #Ti-4Al-4Mo-2Sn
buckling_coefficient = 0.25
elastic_modulus = 69000000000   #Pa

#Adding Masses
# skin_mass_total = stage1.skin.mass + stage2.skin.mass + stage3.skin.mass + fairing.skin.mass
# stiffener_mass_total = stage1.stiffener.mass + stage2.stiffener.mass + stage3.stiffener.mass + fairing.stiffener.mass
# circular_rib_mass_total = stage1.circular_rib.mass + stage2.circular_rib.mass + stage3.circular_rib.mass + fairing.circular_rib.mass
# total_structure_mass = stage1.structure_mass + stage2.structure_mass + stage3.structure_mass + fairing.structure_mass

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