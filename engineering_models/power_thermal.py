
def power_thermal_calculation(stage1,stage2,stage3,input_voltage):

    # This software can suggest a SAFT VL51ES battery cell configuration based on user voltage input. Source 
    # Link: https://www.saftbatteries.com/products-solutions/products/vl51es-battery 
    # Note: If suggested capacity isn't sufficient, up to 12 cells can be\nwired in parallel to increase
    # capacity without affecting voltage

    #Adding in factor of safety to voltage requirements
    voltage = input_voltage*factor_of_safety

    #heat output of battery over time without cooling
    heat_generated_per_second = battery_cells*(current**2*resistance+current*initial_temperature*dudt)

    if voltage <= 21.6:
        Capacity= 1092
        Mass= 6.48 
    elif voltage > 21.6 and voltage <= 25.2:
        Capacity=1274 
        Mass=7.56 
    elif voltage > 25.2 and voltage <= 28.8:
        Capacity=1456 
        Mass=8.64 
    elif voltage > 28.8 and voltage <= 32.4:
        Capacity=1638 
        Mass=9.72 
    elif voltage > 32.4 and voltage <= 36:
        Capacity=1820 
        Mass=10.8 
    elif voltage > 36 and voltage <= 39.6:
        Capacity=2002 
        Mass=11.88 
    elif voltage > 39.6 and voltage <= 43.2:
        Capacity=2184 
        Mass=12.96 
    elif voltage > 43.2 and voltage <= 46.8:
        Capacity=23.66 
        Mass=14.04 
    elif voltage > 46.8 and voltage <= 50.4:
        Capacity=2548 
        Mass=15.12 
    elif voltage > 50.4 and voltage <= 54:
        Capacity=2730 
        Mass=16.2 
    elif voltage > 54 and voltage <= 57.6:
        Capacity=2912 
        Mass=17.28 
    elif voltage > 57.6 and voltage <= 61.2:
        Capacity=3094 
        Mass=18.36 
    elif voltage > 61.2 and voltage <= 64.8:
        Capacity=3276 
        Mass=19.44 
    elif voltage > 64.8 and voltage <= 68.4:
        Capacity=3458 
        Mass=20.52 
    elif voltage > 68.4 and voltage <= 72:
        Capacity=3640 
        Mass=21.6 
    elif voltage > 72 and voltage <= 75.6:
        Capacity=3822 
        Mass=22.68 
    elif voltage > 75.6 and voltage <= 79.2:
        Capacity=4004 
        Mass=23.76 
    elif voltage > 79.2 and voltage <= 82.8:
        Capacity=4186 
        Mass=24.84 
    elif voltage > 82.8 and voltage <= 86.4:
        Capacity=4368 
        Mass=25.92 
    elif voltage > 86.4 and voltage <= 90:
        Capacity=4550 
        Mass=27 
    elif voltage > 90 and voltage <= 93.6:
        Capacity=4732 
        Mass=28.08 
    elif voltage > 93.6 and voltage <= 97.2:
        Capacity=4914 
        Mass=29.16 
    elif voltage > 97.2 and voltage <= 100.8:
        Capacity=5096 
        Mass=30.24 
    elif voltage > 100.8 and voltage <= 104.4:
        Capacity=5278 
        Mass=31.32 
    elif voltage > 104.4 and voltage <= 108:
        Capacity=5460 
        Mass=32.4 
    elif voltage > 108 and voltage <= 111.6:
        Capacity=5642 
        Mass=33.48 
    elif voltage > 111.6 and voltage <= 115.2:
        Capacity=5824 
        Mass=34.56 
    elif voltage > 115.2 and voltage <= 118.8:
        Capacity=6006 
        Mass=35.64 
    elif voltage > 118.8 and voltage <= 122.4:
        Capacity=6188 
        Mass=36.72 
    elif voltage > 122.4 and voltage <= 126:
        Capacity=6370 
        Mass=37.8 
    elif voltage > 126:
        Capacity=6552 
        Mass=38.88 
    else:
        Capacity=6552 
        Mass=38.88 
        print('Voltage out of range')
    
    #Using cooling plate solution
    cooling_plate_mass = 4.63 #kg
    cooling_per_second = 450 #J/s
    Mass = Mass + cooling_plate_mass
    heat_generated_per_second = heat_generated_per_second - cooling_per_second
    
    return(Capacity,heat_generated_per_second,Mass)

#CONSTANTS
initial_temperature = 289.15 #K
#Change in internal energy over time
dudt = .00025  #Assumption based off of reference data
battery_cells = 8
#Current assumption based on an estimate of electrical systems needs
current = 35.52
#Resistance assumption based on data found looking at specific SAFT battery
resistance = 0.06
factor_of_safety = 1.2