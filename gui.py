import PySimpleGUI as sg      
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

    layout = [[sg.Text('Small Launch Vehicle Parameters', font=('Helvetica', 20))],
                [sg.Button('Default'),sg.Button('SS-520'),sg.Button('Astra')],

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
                [sg.Text('_'  * 100, size=(65, 1))],

                [sg.Text('Other', font=('Helvetica', 14))],
                [sg.Text('Rocket Diameter (m)', size=(20, 1)), sg.In(default_text = inputs.get('outside_diameter'), size=(10, 1),key='outside_diameter'), sg.Text('SRM Variance Factor', size=(20, 1)),      
                sg.In(default_text = inputs.get('propulsion_modifier'), size=(10, 1),key ='propulsion_modifier')],
                
                [sg.Submit(), sg.Cancel()]]  
    return(layout)

currentLayout = 'INPUT.py'
exit_flag = 0
while exit_flag == 0:
    layout = Layout(currentLayout)
    window = sg.Window('Team Rocket Small Launch Design Tool', layout, font=("Helvetica", 12))  
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit_flag = 1
            break
        elif event == 'Default':
            currentLayout = 'INPUT_default.py'
            window.close()
            break
        elif event == 'Submit':   
            print('test hi')
            print(values)
            with open('INPUT.py','w') as input_file:
                for key,value in values.items():
                    print((key), '=', str(value),'\n',file=input_file)
            main()
        # with open('Telemetry_and_Tracking_Outputs.txt','r') as f:
        #     print(f.read())