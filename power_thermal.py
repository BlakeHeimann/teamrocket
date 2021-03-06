# Power and Thermal Software
# This software is purposed to provide data on battery requirements and performance
# given a set of user parameters, as well as to provide the user with options
# for battery and thermal control.

# THEORETICAL BATTERY CAPACITY CALCULATION

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

    thermal_capacity = voltage*current*(totalTime/3600) #Watt-hours
    real_thermal_capacity = thermal_capacity*factor_of_safety #Watt-hours
    #change in internal energy of battery over the change in time
    heat_generated_per_second = battery_cells*(current**2*resistance+current*initial_temperature*dudt)

    # print("Theoretical Battery Capacity = "+str(T_capacity)+" Wh")
    # print("Real required battery capacity: "+str(R_capacity)+" Wh")
    # print("Battery cell heat generation: "+str(heat_generated_per_second)+" J/s")
    return(real_thermal_capacity,heat_generated_per_second)