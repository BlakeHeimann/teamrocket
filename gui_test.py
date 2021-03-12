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

import PySimpleGUI as sg      

# Green & tan color scheme      
sg.ChangeLookAndFeel('GreenTan')      

sg.SetOptions(text_justification='right')      

layout = [[sg.Text('Machine Learning Command Line Parameters', font=('Helvetica', 16))],      
            [sg.Text('Passes', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),      
            sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],      
            [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)),      
            sg.In(default_text='10', size=(10, 1))],      
            [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)),      
            sg.In(default_text='5', size=(10, 1))],      
            [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)),      
            sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],      
            [sg.Text('_'  * 100, size=(65, 1))],      
            [sg.Text('Flags', font=('Helvetica', 15), justification='left')],      
            [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
            [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
            [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],      
            [sg.Text('_'  * 100, size=(65, 1))],      
            [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],      
            [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],      
            [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],      
            [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],      
            [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],      
            [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Machine Learning Front End', layout, font=("Helvetica", 12))      

event, values = window.read()