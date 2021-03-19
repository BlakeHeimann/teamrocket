import PySimpleGUI as sg  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib    
import matplotlib.pyplot as plt
from main import main
import numpy as numpy

def Layout(inputfile_name):
    #Reads in the initial input variables to a dict
    input_array = numpy.char.rstrip(numpy.char.lstrip(numpy.loadtxt(inputfile_name,delimiter = '=',dtype = 'str')))
    input_keys = input_array[:,0]
    input_values = input_array[:,1]
    inputs = dict(zip(input_keys,input_values))

    sg.ChangeLookAndFeel('DarkBlue')      

    sg.SetOptions(text_justification='left')      

    l = [[sg.Text('Small Launch Vehicle Parameters', font=('Helvetica', 20))],
                [sg.Button('Default'),sg.Button('SS-520')],

                [sg.Text('Payload', font=('Helvetica', 14))],
                [sg.Text('Payload Mass (kg)', size=(15, 1)), sg.In(default_text=inputs.get('payload_mass'), size=(10, 1),key = 'payload_mass'), sg.Text('Payload Fairing Height (m)', size=(21, 1)),      
                sg.In(default_text=inputs.get('payload_fairing_height'), size=(10, 1),key = 'payload_fairing_height')],
                [sg.Text('_'  * 100, size=(65, 1))], 

                [sg.Text('Stage 1', font=('Helvetica', 14))],             
                [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = inputs.get('stage1_height'), size=(10, 1), key='stage1_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage1_burnTime'), size=(10, 1),key='stage1_burnTime')],      
                [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = inputs.get('stage1_propellant_mass'), size=(10, 1),key='stage1_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage1_engine_mass'), size=(10, 1),key ='stage1_engine_mass')],      
                [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = inputs.get('stage1_thrust'), size=(10, 1),key='stage1_thrust'), sg.Text('ISP', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage1_isp'), size=(10,1),key = 'stage1_isp')],
                [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text = inputs.get('stage1_coastTime'), size=(10, 1),key ='stage1_coastTime')],      
                [sg.Text('_'  * 100, size=(65, 1))],  

                [sg.Text('Stage 2', font=('Helvetica', 14))],             
                [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = inputs.get('stage2_height'), size=(10, 1), key='stage2_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage2_burnTime'), size=(10, 1),key='stage2_burnTime')],      
                [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = inputs.get('stage2_propellant_mass'), size=(10, 1),key='stage2_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage2_engine_mass'), size=(10, 1),key ='stage2_engine_mass')],      
                [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = inputs.get('stage2_thrust'), size=(10, 1),key ='stage2_thrust'), sg.Text('ISP', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage2_isp'), size=(10,1),key='stage2_isp')],
                [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text = inputs.get('stage2_coastTime'), size=(10, 1),key='stage2_coastTime')],
                [sg.Text('_'  * 100, size=(65, 1))],  

                [sg.Text('Stage 3', font=('Helvetica', 14))],             
                [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = inputs.get('stage3_height'), size=(10, 1),key='stage3_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage3_burnTime'), size=(10, 1),key='stage3_burnTime')],      
                [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = inputs.get('stage3_propellant_mass'), size=(10, 1),key='stage3_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage3_engine_mass'), size=(10, 1),key='stage3_engine_mass')],      
                [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = inputs.get('stage3_thrust'), size=(10, 1),key='stage3_thrust'), sg.Text('ISP', size=(15, 1)),      
                sg.In(default_text = inputs.get('stage3_isp'), size=(10,1),key ='stage3_isp')], 
                [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text = inputs.get('stage3_coastTime'), size=(10, 1),key ='stage3_coastTime')],
                [sg.Text('_'  * 100, size=(65, 1))],

                [sg.Text('Other', font=('Helvetica', 14))],
                [sg.Text('Rocket Diameter (m)', size=(20, 1)), sg.In(default_text = inputs.get('outside_diameter'), size=(10, 1),key='outside_diameter'), sg.Text('SRM Variance Factor', size=(20, 1)),      
                sg.In(default_text = inputs.get('propulsion_modifier'), size=(10, 1),key ='propulsion_modifier')],
                [sg.Text('Battery Voltage (V)',size=(20, 1)), sg.In(default_text = inputs.get('voltage'), size=(10, 1),key='voltage')],

                [sg.Submit(),sg.Button('Show Results'),sg.Button('Exit')]]  
    return(l)

currentLayout = 'INPUT.py'
exit_flag = 0
while exit_flag == 0:
    layout = Layout(currentLayout)
    currentLayout = 'INPUT.py'
    window = sg.Window('Team Rocket Small Launch Design Tool', layout, font=("Helvetica", 12))  
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == 'Exit':
            exit_flag = 1
            break
        elif event == 'Default':
            currentLayout = 'INPUT_default.py'
            window.close()
            break
        elif event == 'SS-520':
            currentLayout = 'INPUT_SS-520.py'
            window.close()
            break
        elif event == 'Submit':   
            with open('INPUT.py','w') as input_file:
                for key,value in values.items():
                    print((key), '=', str(value),'\n',file=input_file)
            (positionY,positionX,totalTime, rocket_height,total_mass,total_center_of_mass, 
            slv_cop_from_origin, stage1_mass,stage2_mass, stage3_mass, payload_fairing_mass,
            nosecone_mass, real_battery_capacity, heat_generated_per_second, stage1_delta_v, 
            stage2_delta_v, stage3_delta_v, time_of_supersonic, max_dynamic_pressure, 
            time_of_max_dynamic_pressure,horizontal_velocity,vertical_velocity) = main()
        # with open('Telemetry_and_Tracking_Outputs.txt','r') as f:
        #     print(f.read())
        elif event == 'Show Results' and "positionY" in locals():
            fig = plt.figure()
            t = numpy.arange(0, totalTime)
            fig.add_subplot().plot(t,positionY)
            plt.grid()
            plt.title('Altitude (m) vs Time (s)')
            plt.xlabel('Time (s)')
            plt.ylabel('Altitude (m)')

            fig2 = plt.figure()
            fig2.add_subplot().plot(t,positionX)
            plt.grid()
            plt.title('Distance (m) vs Time (s)')
            plt.xlabel('Time (s)')
            plt.ylabel('Distance (m)')

            matplotlib.use("TkAgg")

            def draw_figure(canvas, figure):
                figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
                figure_canvas_agg.draw()
                figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
                return figure_canvas_agg

            # Define the window layout
            left_col = [
                [sg.Text('Rocket Height (m) :    '),sg.Text(str(round(rocket_height,2)))],
                [sg.Text('Total Rocket Mass (kg) :    '),sg.Text(str(round(total_mass,2)))],
                [sg.Text('Center of Mass from Base (m) :    '),sg.Text(str(round(total_center_of_mass,2)))],
                [sg.Text('Center of Pressure from Base (m) :    '),sg.Text(str(round(slv_cop_from_origin,2)))],
                [sg.Text('Stage 1 Total Mass (kg) :    '),sg.Text(str(round(stage1_mass,2)))],
                [sg.Text('Stage 2 Total Mass (kg) :    '),sg.Text(str(round(stage2_mass,2)))],
                [sg.Text('Stage 3 Total Mass (kg) :    '),sg.Text(str(round(stage3_mass,2)))],
                [sg.Text('Payload Fairing Total Mass (kg) :    '),sg.Text(str(round(payload_fairing_mass,2)))],
                [sg.Text('Nosecone Total Mass (kg) :    '),sg.Text(str(round(nosecone_mass,2)))],
                [sg.Text('Battery Capacity (Wh) :    '),sg.Text(str(round(real_battery_capacity,2)))],
                [sg.Text('Battery Heat Generation (J/s) :    '),sg.Text(str(round(heat_generated_per_second,2)))],
                [sg.Text('Stage 1 Delta V (m/s) :    '),sg.Text(str(round(stage1_delta_v,2)))],
                [sg.Text('Stage 2 Delta V (m/s) :    '),sg.Text(str(round(stage2_delta_v,2)))],
                [sg.Text('Stage 3 Delta V (m/s) :    '),sg.Text(str(round(stage3_delta_v,2)))],
                [sg.Text('Time of Supersonic Flight (s) :    '),sg.Text(str(round(time_of_supersonic,2)))],
                [sg.Text('Max Dynamic Pressure (Pa) :    '),sg.Text(str(numpy.round(*max_dynamic_pressure,2)))],
                [sg.Text('Time of Max Dynamic Pressure (s) :    '),sg.Text(str(round(time_of_max_dynamic_pressure,2)))],
                [sg.Button("Back"),sg.Button("Exit")],
            ]

            right_col = [
                [sg.Text("Trajectory of Small Launch Vehicle")],
                [sg.Canvas(key="-CANVAS-")],
                [sg.Text('Final Altitude (m): '), sg.Text(str(round(*positionY[len(positionY)-1],2)))],
                [sg.Text('End of Flight Vertical Velocity (m/s): '), sg.Text(str(round(*vertical_velocity[len(vertical_velocity)-1],2)))],
            ]

            extra_col = [
                [sg.Text("Horizontal Distance Travelled in Flight")],
                [sg.Canvas(key="-CANVAS2-")],
                [sg.Text("Distance Travelled Before Payload Release (m): "),sg.Text(str(round(*positionX[len(positionX)-1],2)))],
                [sg.Text('End of Flight Horizontal Velocity (m/s): '), sg.Text(str(round(*horizontal_velocity[len(horizontal_velocity)-1],2)))]
            ]

            layout = [[sg.Column(left_col, element_justification='l'),sg.VSeperator(),sg.Column(right_col, element_justification='c'),sg.VSeperator(),sg.Column(extra_col,element_justification='c')]]

            # Create the form and show it without the plot
            window.close()
            window = sg.Window(
                "Team Rocket Small Launch Design Tool",
                layout,
                location=(550, 540),
                finalize=True,
                element_justification="center",
                font="Helvetica 12",
            )

            # Add the plot to the window
            draw_figure(window["-CANVAS-"].TKCanvas, fig)
            draw_figure(window["-CANVAS2-"].TKCanvas, fig2)

            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                exit_flag = 1
                break
            elif event == "Back":
                window.close()
                break