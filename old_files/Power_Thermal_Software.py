# Power and Thermal Software
# This software is purposed to provide data on battery requirements and performance
# given a set of user parameters, as well as to provide the user with options
# for battery and thermal control.

# THEORETICAL BATTERY CAPACITY CALCULATION
# Voltage Input
while 1:
    try:
        V = float(input("\nInput total additive voltage (V): "))
    except ValueError:
        print("\nInvalid")
        continue
    if V <= 0:
        print("\nInvalid")
        continue
    else:
        break

# Current Input
while 1:
    try:
        I = float(input("\nInput total additive current draw (A): "))
    except ValueError:
        print("\nInvalid")
        continue
    if I <= 0:
        print("\nInvalid")
        continue
    else:
         break

# Flight Time Input
while 1:
    try:
        t = float(input("\nInput total flight time (s): "))
    except ValueError:
        print("\nInvalid")
        continue
    if t <= 0:
        print("\nInvalid")
        continue
    else:
        break


T_capacity = V*I*(t/3600) #Watt-hours
print("\nTheoretical Battery Capacity = "+str(T_capacity)+" Wh")

# REAL BATTERY CAPACITY CALCULATION
# Factor of Safety Input
while 1:
     try:
         FoS = float(input("\nInput Factor of Safety: "))
     except ValueError:
         print("\nInvalid")
         continue
     if FoS < 1.2:
         print("\nInvalid; FoS must be greater than or equal to 1.2 to "+
               "account for exponential discharge\n drop when remaining "+
               "battery capacity reaches 20 percent.")
     else:
         break

R_capacity = T_capacity*FoS #Watt-hours
print("\nReal required battery capacity: "+str(R_capacity)+" Wh")

# BATTERY HEAT GENERATION CALCULATION
# Internal Battery Resistance Input
while 1:
    try:
        R = float(input("\nInput internal battery resistance (Ohms): "))
    except ValueError:
        print("\nInvalid")
        continue
    if R <=0:
        print("\nInvalid")
        continue
    else:
        break

# Initial Operating Temperature Input
while 1:
    try:
        T = float(input("\nInput initial battery operating temperature (K): "))
    except ValueError:
        print("\nInvalid")
        continue
    if T <= 0:
        print("\nInvalid")
        continue
    else:
        break

dudt = .00025  # Assumption based off of reference data
Heat = I*I*R+I*T*dudt
print("\nBattery cell heat generation: "+str(Heat)+" J/s")

# Battery Configuration Suggestions for User
# Battery: SAFT VL51ES Battery
# Link: https://www.saftbatteries.com/products-solutions/products/vl51es-battery

print("\nThis software can suggest a SAFT VL51ES battery cell configuration based on user voltage input.\nSource "+
      "Link: https://www.saftbatteries.com/products-solutions/products/vl51es-battery"+"\n\n"+"Note: If"+
      " suggested capacity isn't sufficient, up to 12 cells can be\nwired in parallel to increase"+
      " capacity without affecting voltage.\n")

while 1:
    answer = input("Would you like to be suggested a SAFT VL51ES battery cell configuration? (Y/N):\n ")
    if answer in ['y', 'Y', 'Yes', 'yes', 'YES']:
        if V <= 21.6:
            print("1p6s cell configuration recommended.\n\n Parameters:\n Capacity: 1092 Wh\n Voltage: 21.6 V\n "
                  "Mass: 6.48 kg")
        elif V > 21.6 and V <= 25.2:
            print("1p7s cell configuration recommended.\n\n Parameters:\n Capacity: 1274 Wh\n Voltage: 25.2 V\n "
                  "Mass: 7.56 kg")
        elif V > 25.2 and V <= 28.8:
            print("1p8s cell configuration recommended.\n\n Parameters:\n Capacity: 1456 Wh\n Voltage: 28.8 V\n "
                  "Mass: 8.64 kg")
        elif V > 28.8 and V <= 32.4:
            print("1p9s cell configuration recommended.\n\n Parameters:\n Capacity: 1638 Wh\n Voltage: 32.4 V\n "
                  "Mass: 9.72 kg")
        elif V > 32.4 and V <= 36:
            print("1p10s cell configuration recommended.\n\n Parameters:\n Capacity: 1820 Wh\n Voltage: 36 V\n "
                  "Mass: 10.8 kg")
        elif V > 36 and V <= 39.6:
            print("1p11s cell configuration recommended.\n\n Parameters:\n Capacity: 2002 Wh\n Voltage: 39.6 V\n "
                  "Mass: 11.88 kg")
        elif V > 39.6 and V <= 43.2:
            print("1p12s cell configuration recommended.\n\n Parameters:\n Capacity: 2184 Wh\n Voltage: 43.2 V\n "
                  "Mass: 12.96 kg")
        elif V > 43.2 and V <= 46.8:
            print("1p13s cell configuration recommended.\n\n Parameters:\n Capacity: 23.66 Wh\n Voltage: 46.8 V\n "
                  "Mass: 14.04 kg")
        elif V > 46.8 and V <= 50.4:
            print("1p14s cell configuration recommended.\n\n Parameters:\n Capacity: 2548 Wh\n Voltage: 50.4 V\n "
                  "Mass: 15.12 kg")
        elif V > 50.4 and V <= 54:
            print("1p15s cell configuration recommended.\n\n Parameters:\n Capacity: 2730 Wh\n Voltage: 54 V\n "
                  "Mass: 16.2 kg")
        elif V > 54 and V <= 57.6:
            print("1p16s cell configuration recommended.\n\n Parameters:\n Capacity: 2912 Wh\n Voltage: 57.6 V\n "
                  "Mass: 17.28 kg")
        elif V > 57.6 and V <= 61.2:
            print("1p17s cell configuration recommended.\n\n Parameters:\n Capacity: 3094 Wh\n Voltage: 61.2 V\n "
                  "Mass: 18.36 kg")
        elif V > 61.2 and V <= 64.8:
            print("1p18s cell configuration recommended.\n\n Parameters:\n Capacity: 3276 Wh\n Voltage: 64.8 V\n "
                  "Mass: 19.44 kg")
        elif V > 64.8 and V <= 68.4:
            print("1p19s cell configuration recommended.\n\n Parameters:\n Capacity: 3458 Wh\n Voltage: 68.4 V\n "
                  "Mass: 20.52 kg")
        elif V > 68.4 and V <= 72:
            print("1p20s cell configuration recommended.\n\n Parameters:\n Capacity: 3640 Wh\n Voltage: 72 V\n "
                  "Mass: 21.6 kg")
        elif V > 72 and V <= 75.6:
            print("1p21s cell configuration recommended.\n\n Parameters:\n Capacity: 3822 Wh\n Voltage: 75.6 V\n "
                  "Mass: 22.68 kg")
        elif V > 75.6 and V <= 79.2:
            print("1p22s cell configuration recommended.\n\n Parameters:\n Capacity: 4004 Wh\n Voltage: 79.2 V\n "
                  "Mass: 23.76 kg")
        elif V > 79.2 and V <= 82.8:
            print("1p23s cell configuration recommended.\n\n Parameters:\n Capacity: 4186 Wh\n Voltage: 82.8 V\n "
                  "Mass: 24.84 kg")
        elif V > 82.8 and V <= 86.4:
            print("1p24s cell configuration recommended.\n\n Parameters:\n Capacity: 4368 Wh\n Voltage: 86.4 V\n "
                  "Mass: 25.92 kg")
        elif V > 86.4 and V <= 90:
            print("1p25s cell configuration recommended.\n\n Parameters:\n Capacity: 4550 Wh\n Voltage: 90 V\n "
                  "Mass: 27 kg")
        elif V > 90 and V <= 93.6:
            print("1p26s cell configuration recommended.\n\n Parameters:\n Capacity: 4732 Wh\n Voltage: 93.6 V\n "
                  "Mass: 28.08 kg")
        elif V > 93.6 and V <= 97.2:
            print("1p27s cell configuration recommended.\n\n Parameters:\n Capacity: 4914 Wh\n Voltage: 97.2 V\n "
                  "Mass: 29.16 kg")
        elif V > 97.2 and V <= 100.8:
            print("1p28s cell configuration recommended.\n\n Parameters:\n Capacity: 5096 Wh\n Voltage: 100.8 V\n "
                  "Mass: 30.24 kg")
        elif V > 100.8 and V <= 104.4:
            print("1p29s cell configuration recommended.\n\n Parameters:\n Capacity: 5278 Wh\n Voltage: 104.4 V\n "
                  "Mass: 31.32 kg")
        elif V > 104.4 and V <= 108:
            print("1p30s cell configuration recommended.\n\n Parameters:\n Capacity: 5460 Wh\n Voltage: 108 V\n "
                  "Mass: 32.4 kg")
        elif V > 108 and V <= 111.6:
            print("1p31s cell configuration recommended.\n\n Parameters:\n Capacity: 5642 Wh\n Voltage: 111.6 V\n "
                  "Mass: 33.48 kg")
        elif V > 111.6 and V <= 115.2:
            print("1p32s cell configuration recommended.\n\n Parameters:\n Capacity: 5824 Wh\n Voltage: 115.2 V\n "
                  "Mass: 34.56 kg")
        elif V > 115.2 and V <= 118.8:
            print("1p33s cell configuration recommended.\n\n Parameters:\n Capacity: 6006 Wh\n Voltage: 118.8 V\n "
                  "Mass: 35.64 kg")
        elif V > 118.8 and V <= 122.4:
            print("1p34s cell configuration recommended.\n\n Parameters:\n Capacity: 6188 Wh\n Voltage: 122.4 V\n "
                  "Mass: 36.72 kg")
        elif V > 122.4 and V <= 126:
            print("1p35s cell configuration recommended.\n\n Parameters:\n Capacity: 6370 Wh\n Voltage: 126 V\n "
                  "Mass: 37.8 kg")
        elif V > 126 and V <= 129.6:
            print("1p36s cell configuration recommended.\n\n Parameters:\n Capacity: 6552 Wh\n Voltage: 129.6 V\n "
                  "Mass: 38.88 kg")
        elif V > 129.6:
            print("\nVoltage not supported by this battery; User-specified battery choice recommended.")
        break
    elif answer in ['n', 'N', 'No', 'NO']:
        break
    else:
        print("Invalid input. Please Try again.\n")
        continue

# Cooling Solution Suggestions
while 1:
    answer = input("\nWould you like suggestions for battery cooling solutions? (Y/N):\n ")
    if answer in ['y', 'Y', 'Yes', 'yes', 'YES']:
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
        break
    elif answer in ['n', 'N', 'No', 'no', 'NO']:
        break
    else:
        print("Invalid input. Please try again.\n")
        continue


