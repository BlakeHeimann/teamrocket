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

def Area_Moment_of_Inertia(outside_diameter,inside_diameter):
    return math.pi*(outside_diameter**4-inside_diameter**4)/64

def Pcritical(buckling_coefficient,elastic_modulus,outside_radius,inside_radius,height):
    try:
        return (buckling_coefficient*math.pi**2*elastic_modulus*Area_Moment_of_Inertia(outside_radius*2,inside_radius*2))/(height**2)
    except:
        return 0
    
#Constants
skin_density = 2710             #kg/m^3  #Al-Li 2195
stiffener_density = 4700        #kg/m^3  #Ti-4Al-4Mo-2Sn
buckling_coefficient = 0.25
elastic_modulus = 69000000000   #Pa