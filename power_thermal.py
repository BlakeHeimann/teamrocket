# Power and Thermal Software
# This software is purposed to provide data on battery requirements and performance
# given a set of user parameters, as well as to provide the user with options
# for battery and thermal control.

# THEORETICAL BATTERY CAPACITY CALCULATION

#INPUTS
Voltage
Current
totalTime
factor_of_safety
resistance

initial_temperature
dudt = .00025  #Assumption based off of reference data

T_capacity = V*I*(t/3600) #Watt-hours
print("Theoretical Battery Capacity = "+str(T_capacity)+" Wh")

# REAL BATTERY CAPACITY CALCULATION
# Factor of Safety Input

R_capacity = T_capacity*FoS #Watt-hours
print("Real required battery capacity: "+str(R_capacity)+" Wh")

# BATTERY HEAT GENERATION CALCULATION
# Internal Battery Resistance Input

# Initial Operating Temperature Input

#change in internal energy of battery over the change in time
dudt = .00025  #Assumption based off of reference data
Heat = I*I*R+I*T*dudt
print("Battery cell heat generation: "+str(Heat)+" J/s")