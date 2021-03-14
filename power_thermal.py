
def power_thermal_calculation(stage1,stage2,stage3):
    totalburn_time = stage1.burn_time + stage2.burn_time + stage3.burn_time
    totalCoastTime = stage1.coastTime + stage2.coastTime
    totalTime = totalburn_time + totalCoastTime

    #INPUTS
    voltage = 28.8
    current = 42.4
    factor_of_safety = 1.2
    resistance = 0.06
    initial_temperature = 289.15
    dudt = .00025  #Assumption based off of reference data
    battery_cells = 8

    battery_capacity = voltage*current*(totalTime/3600) #Watt-hours
    real_battery_capacity = battery_capacity*factor_of_safety #Watt-hours
    #change in internal energy of battery over the change in time
    heat_generated_per_second = battery_cells*(current**2*resistance+current*initial_temperature*dudt)

    print("\nThis software can suggest a SAFT VL51ES battery cell configuration based on user voltage input.\nSource "+
        "Link: https://www.saftbatteries.com/products-solutions/products/vl51es-battery"+"\n\n"+"Note: If"+
        " suggested capacity isn't sufficient, up to 12 cells can be\nwired in parallel to increase"+
        " capacity without affecting voltage.\n")

    if V <= 21.6:
        Capacity= 1092 
        
        Mass= 6.48 
    elif V > 21.6 and V <= 25.2:
        Capacity=1274 
        
        Mass=7.56 
    elif V > 25.2 and V <= 28.8:
        Capacity=1456 
        
        Mass=8.64 
    elif V > 28.8 and V <= 32.4:
        Capacity=1638 
        
        Mass=9.72 
    elif V > 32.4 and V <= 36:
        Capacity=1820 
        
        Mass=10.8 
    elif V > 36 and V <= 39.6:
        Capacity=2002 
        
        Mass=11.88 
    elif V > 39.6 and V <= 43.2:
        Capacity=2184 
        
        Mass=12.96 
    elif V > 43.2 and V <= 46.8:
        Capacity=23.66 
        
        Mass=14.04 
    elif V > 46.8 and V <= 50.4:
        Capacity=2548 
        
        Mass=15.12 
    elif V > 50.4 and V <= 54:
        Capacity=2730 
        
        Mass=16.2 
    elif V > 54 and V <= 57.6:
        Capacity=2912 
        
        Mass=17.28 
    elif V > 57.6 and V <= 61.2:
        Capacity=3094 
        
        Mass=18.36 
    elif V > 61.2 and V <= 64.8:
        Capacity=3276 
        
        Mass=19.44 
    elif V > 64.8 and V <= 68.4:
        Capacity=3458 
        
        Mass=20.52 
    elif V > 68.4 and V <= 72:
        Capacity=3640 
        
        Mass=21.6 
    elif V > 72 and V <= 75.6:
        Capacity=3822 
        
        Mass=22.68 
    elif V > 75.6 and V <= 79.2:
        Capacity=4004 
        
        Mass=23.76 
    elif V > 79.2 and V <= 82.8:
        Capacity=4186 
        
        Mass=24.84 
    elif V > 82.8 and V <= 86.4:
        Capacity=4368 
        
        Mass=25.92 
    elif V > 86.4 and V <= 90:
        Capacity=4550 
        
        Mass=27 
    elif V > 90 and V <= 93.6:
        Capacity=4732 
        
        Mass=28.08 
    elif V > 93.6 and V <= 97.2:
        Capacity=4914 
        
        Mass=29.16 
    elif V > 97.2 and V <= 100.8:
        Capacity=5096 
        
        Mass=30.24 
    elif V > 100.8 and V <= 104.4:
        Capacity=5278 
        
        Mass=31.32 
    elif V > 104.4 and V <= 108:
        Capacity=5460 
        
        Mass=32.4 
    elif V > 108 and V <= 111.6:
        Capacity=5642 
        
        Mass=33.48 
    elif V > 111.6 and V <= 115.2:
        Capacity=5824 
        
        Mass=34.56 
    elif V > 115.2 and V <= 118.8:
        Capacity=6006 
        
        Mass=35.64 
    elif V > 118.8 and V <= 122.4:
        Capacity=6188 
        
        Mass=36.72 
    elif V > 122.4 and V <= 126:
        Capacity=6370 
        
        Mass=37.8 
    elif V > 126:
        Capacity=6552 
        
        Mass=38.88 
    else:
        print('Voltage out of range')

    
    return(real_battery_capacity,heat_generated_per_second)