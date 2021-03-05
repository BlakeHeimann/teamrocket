from structure import Skin, Stiffener, Circular_Rib, Moment_of_Inertia, buckling_coefficient, elastic_modulus
import math as math
from propulsion import mass_flow

class Stage:
    def __init__(self,height,inside_radius,outside_radius,skin_density,stiffener_density,propellant_mass,engine_mass, thrust, burn_time,isp):
        self.propellant_mass = propellant_mass
        self.engine_mass = engine_mass
        self.burn_time = burn_time
        self.isp = isp
        self.thrust = thrust
        self.inside_radius = inside_radius
        self.outside_radius = outside_radius
        self.skin = Skin(height,inside_radius,outside_radius,skin_density)
        self.stiffener = Stiffener(height,stiffener_density)
        self.circular_rib = Circular_Rib(height,outside_radius)
        self.structure_mass = self.skin.mass + self.stiffener.mass + self.circular_rib.mass
        self.Pcrit = (buckling_coefficient*math.pi**2*elastic_modulus*Moment_of_Inertia(outside_radius*2,inside_radius*2))/(height**2)
        self.height = height       
        self.mass = self.engine_mass + self.propellant_mass+ self.structure_mass
        self.mass_flow = mass_flow(self)