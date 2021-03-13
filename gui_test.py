import PySimpleGUI as sg      
#we can use importLib.reload() to re import the INPUT variables at any point
import importlib
from INPUT import *
from main import main
    
sg.ChangeLookAndFeel('DarkBlue')      

sg.SetOptions(text_justification='left')      

layout = [[sg.Text('Small Launch Vehicle Parameters', font=('Helvetica', 20))],
            # I think we can just take out the whole drop down thing and make it so that
            # the user just inputs 0 values for the stages they don't want to run
            #[sg.Text('Stages', size=(20, 1)),sg.Drop(values=('3', '2','1'), auto_size_text=True)],
            ##
            [sg.Text('Payload', font=('Helvetica', 14))],
            [sg.Text('Payload Mass (kg)', size=(15, 1)), sg.In(default_text=str(payload_mass), size=(10, 1),key = 'payload_mass'), sg.Text('Payload Fairing Height (m)', size=(21, 1)),      
            sg.In(default_text=str(payload_fairing_height), size=(10, 1),key = 'payload_fairing_height')],
            [sg.Text('_'  * 100, size=(65, 1))], 

            [sg.Text('Stage 1', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = str(stage1_height), size=(10, 1), key='stage1_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text = str(stage1_burnTime), size=(10, 1),key='stage1_burnTime')],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = str(stage1_propellant_mass), size=(10, 1),key='stage1_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text = str(stage1_engine_mass), size=(10, 1),key ='stage1_engine_mass')],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = str(stage1_thrust), size=(10, 1),key='stage1_thrust'), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text = str(stage1_isp), size=(10,1),key = 'stage1_isp')],
            [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text = str(stage1_coastTime), size=(10, 1),key ='stage1_coastTime')],      
            [sg.Text('_'  * 100, size=(65, 1))],  

            [sg.Text('Stage 2', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = str(stage2_height), size=(10, 1), key='stage2_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text = str(stage2_burnTime), size=(10, 1),key='stage2_burnTime')],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = str(stage2_propellant_mass), size=(10, 1),key='stage2_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text = str(stage2_engine_mass), size=(10, 1),key ='stage2_engine_mass')],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = str(stage2_thrust), size=(10, 1),key ='stage2_thrust'), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text = str(stage2_isp), size=(10,1),key='stage2_isp')],
            [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text = str(stage2_coastTime), size=(10, 1),key='stage2_coastTime')],
            [sg.Text('_'  * 100, size=(65, 1))],  

            [sg.Text('Stage 3', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text = str(stage3_height), size=(10, 1),key='stage3_height'), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text = str(stage3_burnTime), size=(10, 1),key='stage3_burnTime')],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text = str(stage3_propellant_mass), size=(10, 1),key='stage3_propellant_mass'), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text = str(stage3_engine_mass), size=(10, 1),key='stage3_engine_mass')],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text = str(stage3_thrust), size=(10, 1),key='stage3_thrust'), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text = str(stage3_isp), size=(10,1),key ='stage3_isp')], 
            [sg.Text('_'  * 100, size=(65, 1))],

            [sg.Text('Other', font=('Helvetica', 14))],
            [sg.Text('Rocket Diameter (m)', size=(20, 1)), sg.In(default_text = str(outside_diameter), size=(10, 1),key='outside_diameter'), sg.Text('SRM Variance Factor', size=(20, 1)),      
            sg.In(default_text = str(propulsion_modifier), size=(10, 1),key ='propulsion_modifier')],
            
            [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Team Rocket Small Launch Design Tool', layout, font=("Helvetica", 12))      

event, values = window.read()

print(values)

