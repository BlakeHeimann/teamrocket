from engineering_models.structure import Skin, Stiffener, Circular_Rib, Pcritical
from engineering_models.propulsion import mass_flow

#Stage class that contains all the information needed to create a stage
class Stage:
    def __init__(self,height,inside_radius,outside_radius,propellant_mass,engine_mass, thrust, burn_time,isp):
        self.height = height   
        self.propellant_mass = propellant_mass
        self.engine_mass = engine_mass
        self.burn_time = burn_time
        self.isp = isp
        self.thrust = thrust
        self.inside_radius = inside_radius
        self.outside_radius = outside_radius
        self.skin = Skin(height,inside_radius,outside_radius)
        self.stiffener = Stiffener(height)
        self.circular_rib = Circular_Rib(height,outside_radius)
        self.structure_mass = self.skin.mass + self.stiffener.mass + self.circular_rib.mass
        self.Pcrit = Pcritical(outside_radius,inside_radius,height)    
        self.mass = self.engine_mass + self.propellant_mass+ self.structure_mass
        self.mass_flow = mass_flow(self)