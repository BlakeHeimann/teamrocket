
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
        print('Voltage out of range')

    print("Solution 1\n Product: KOOLANCE VLX-450 Inline 450W Chiller\n Cooling Method: Conduction\n"+
              " Heat Sink: R-134a\n Mass: 4.63 kg\n Cooling Capacity: 450 J/s\n" +
              " Source Link: https://koolance.com/450W-chiller-subassembly-vlx-450?specsheet=1\n\n"+
              "Solution 2\n Product: Advanced Thermal Solutions Inc. ATS-CP-1000 Cold Plate\n"+
              " Cooling Method: Conduction\n Heat Sink: Variable Fluid\n Mass: 1.2 kg\n Cooling Capacity: 1000 J/s\n"+
              " Source Link: https://www.digikey.com/en/products/detail/advanced-thermal-solutions-inc./ATS-CP-1000"+
              "/7721833\n\n"+"Solution 3\n Product: Aspen Systems ECU-550\n Cooling Method: Convection\n"+
              " Heat Sink: Local Atmosphere\n Mass: 9.07 kg\n Cooling Capacity: 550 J/s\n Source Link: "+
              "https://aspensystems.com/products/ecu-series-for-military-electronics/\n"+
              " NOTE: Not recommended for high-altitude flight due to loss of local atmosphere.\n")

    return(real_battery_capacity,heat_generated_per_second)