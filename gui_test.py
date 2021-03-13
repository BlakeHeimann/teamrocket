# pylint: disable=E1101

# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import PySimpleGUI as sg
# import matplotlib
# from main import main

# (positionY,totalTime, rocket_height) = main()

# fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, totalTime, 1)
# fig.add_subplot(111).plot(positionY)

# matplotlib.use("TkAgg")

# def draw_figure(canvas, figure):
#     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#     figure_canvas_agg.draw()
#     figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
#     return figure_canvas_agg

# # Define the window layout
# layout = [
#     [sg.Text("Plot test")],
#     [sg.Canvas(key="-CANVAS-")],
#     [sg.Button("Ok")],
# ]

# # Create the form and show it without the plot
# window = sg.Window(
#     "Matplotlib Single Graph",
#     layout,
#     location=(0, 0),
#     finalize=True,
#     element_justification="center",
#     font="Helvetica 18",
# )

# # Add the plot to the window
# draw_figure(window["-CANVAS-"].TKCanvas, fig)

# event, values = window.read()

# window.close()

# import PySimpleGUI as sg 
  
# # Add some color 
# # to the window 
# sg.theme('SandyBeach')      
  
# # Very basic window. 
# # Return values using 
# # automatic-numbered keys 
# layout = [ 
#     [sg.Text('Please enter your Name, Age, Phone')], 
#     [sg.Text('Name', default_text = 'hello', size =(15, 1)), sg.InputText()], 
#     [sg.Text('Age', size =(15, 1)), sg.InputText()], 
#     [sg.Text('Phone', size =(15, 1)), sg.InputText()], 
#     [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
#         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
#     [sg.Submit(), sg.Cancel()] 
# ] 
  
# window = sg.Window('Simple data entry window', layout) 
# event, values = window.read() 
# window.close() 
  
# # The input data looks like a simple list  
# # when automatic numbered 
# print(event, values[0], values[1], values[2])

# import PySimpleGUI as sg      

# # Green & tan color scheme      
# sg.ChangeLookAndFeel('GreenTan')      

# sg.SetOptions(text_justification='right')      

# layout = [[sg.Text('Small Launch Vehicle Parameters', font=('Helvetica', 16))],
#             [sg.Text('_'  * 100, size=(65, 1))],  
#             [sg.Text('Stage 1', font=('Helvetica', 14))],       
#             [sg.Text('Stages', size=(15, 1)), sg.Spin(values=[i for i in range(1, 4)], initial_value=3, size=(6, 1)),      
#             sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],      
#             [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)),      
#             sg.In(default_text='10', size=(10, 1))],      
#             [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)),      
#             sg.In(default_text='5', size=(10, 1))],      
#             [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)),      
#             sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],      
#             [sg.Text('_'  * 100, size=(65, 1))],      
#             [sg.Text('Flags', font=('Helvetica', 15), justification='left')],      
#             [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
#             [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
#             [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],      
#             [sg.Text('_'  * 100, size=(65, 1))],      
#             [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],      
#             [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],      
#             [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],      
#             [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],      
#             [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],      
#             [sg.Submit(), sg.Cancel()]]      

# window = sg.Window('Machine Learning Front End', layout, font=("Helvetica", 12))      

# event, values = window.read()

import PySimpleGUI as sg      

# Green & tan color scheme      
sg.ChangeLookAndFeel('DarkBlue')      

sg.SetOptions(text_justification='left')      

layout = [[sg.Text('Small Launch Vehicle Parameters', font=('Helvetica', 20))],
            # I think we can just take out the whole drop down thing and make it so that
            # the user just inputs 0 values for the stages they don't want to run
            #[sg.Text('Stages', size=(20, 1)),sg.Drop(values=('3', '2','1'), auto_size_text=True)],
            ##
            [sg.Text('Payload', font=('Helvetica', 14))],
            [sg.Text('Payload Mass (kg)', size=(15, 1)), sg.In(default_text='5', size=(10, 1)), sg.Text('Payload Fairing Height (m)', size=(21, 1)),      
            sg.In(default_text='1', size=(10, 1))],
            [sg.Text('_'  * 100, size=(65, 1))], 

            [sg.Text('Stage 1', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text='7.5', size=(10, 1)), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text='74', size=(10, 1))],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text='15000', size=(10, 1)), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text='1779', size=(10, 1))],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text='469054', size=(10, 1)), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text=('235.88'), size=(10,1))],
            [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text='51', size=(10, 1))],      
            [sg.Text('_'  * 100, size=(65, 1))],  

            [sg.Text('Stage 2', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text='3.35', size=(10, 1)), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text='64', size=(10, 1))],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text='5080', size=(10, 1)), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text='527', size=(10, 1))],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text='220345', size=(10, 1)), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text=('282.98'), size=(10,1))],
            [sg.Text('Coast Time (s)', size=(20, 1)), sg.In(default_text='164', size=(10, 1))],
            [sg.Text('_'  * 100, size=(65, 1))],  

            [sg.Text('Stage 3', font=('Helvetica', 14))],             
            [sg.Text('Height (m)', size=(20, 1)), sg.In(default_text='2.1', size=(10, 1)), sg.Text('Burn Time (s)', size=(15, 1)),      
            sg.In(default_text='46', size=(10, 1))],      
            [sg.Text('Propellant Mass (kg)', size=(20, 1)), sg.In(default_text='1760', size=(10, 1)), sg.Text('Engine Mass', size=(15, 1)),      
            sg.In(default_text='189', size=(10, 1))],      
            [sg.Text('Thrust (N)', size=(20, 1)), sg.In(default_text='106212', size=(10, 1)), sg.Text('ISP', size=(15, 1)),      
            sg.In(default_text=('282.98'), size=(10,1))], 
            [sg.Text('_'  * 100, size=(65, 1))],

            [sg.Text('Other', font=('Helvetica', 14))],
            [sg.Text('Rocket Diameter (m)', size=(20, 1)), sg.In(default_text='1.405', size=(10, 1)), sg.Text('SRM Variance Factor', size=(20, 1)),      
            sg.In(default_text='0.02', size=(10, 1))],
            
            [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Team Rocket Small Launch Design Tool', layout, font=("Helvetica", 12))      

event, values = window.read()