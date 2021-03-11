from INPUT import *
from main import *
import csv
import os
import tkinter as tk

top = tk.Tk()
##########################################################################
#Take file input
##########################################################################
# Get filename here.
inputfile = form['filename']
# Test if the file was uploaded
if inputfile.filename:
# strip the leading path from the file name
   fn = os.path.basename(inputfile.filename)
   open(fn, 'wb').write(inputfile.file.read()) 

##########################################################################
#How many stages dropdown***
##########################################################################
# Create Label 
label = Label( top , text = "Number of Launch Stages: " ) 
label.pack() 

# Dropdown menu options 
options = [ 
    1, 
    2, 
    3
] 
  
# datatype of menu text 
clicked = IntVar() 
  
# initial menu text 
clicked.set( 3 ) 
  
# Create Dropdown menu 
drop = OptionMenu( top , clicked , *options ) 
drop.pack() 

##########################################################################
#Submit Input File & Number of Stages selections
##########################################################################

##########################################################################
#Call input file for input
##########################################################################
input = open(“input.py”, mode=‘r’)
contents = input.read()

##########################################################################
#Populate fields & fill w/ input file data based on number of stages
##########################################################################
#def main():
	if(clicked == 1):
        tk.Label(top, text="Outside Diameter").grid(row=0)
        tk.Label(top, text="Stage 1 Height").grid(row=1)
        tk.Label(top, text="Stage 2 Height").grid(row=2)
        tk.Label(top, text="Stage 3 Height").grid(row=3)
        tk.Label(top, text="Payload Fairing Height").grid(row=4)
        tk.Label(top, text="Payload Mass").grid(row=5)
        tk.Label(top, text="Stage 1 Propellant Mass").grid(row=6)
        tk.Label(top, text="Stage 1 Engine Mass").grid(row=7)
        tk.Label(top, text="Stage 1 Thrust").grid(row=8)
        tk.Label(top, text="Stage 1 Burn Time").grid(row=9)
        tk.Label(top, text="Stage 1 ISP").grid(row=10)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        e5 = tk.Entry(top)
        e6 = tk.Entry(top)
        e7 = tk.Entry(top)
        e8 = tk.Entry(top)
        e9 = tk.Entry(top)
        e10 = tk.Entry(top)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=7, column=1)
        e9.grid(row=8, column=1)
        e10.grid(row=9, column=1)

        top.mainloop()
	
	elif (clicked == 2):
		tk.Label(top, text="Outside Diameter").grid(row=0)
        tk.Label(top, text="Stage 1 Height").grid(row=1)
        tk.Label(top, text="Stage 2 Height").grid(row=2)
        tk.Label(top, text="Stage 3 Height").grid(row=3)
        tk.Label(top, text="Payload Fairing Height").grid(row=4)
        tk.Label(top, text="Payload Mass").grid(row=5)
        tk.Label(top, text="Stage 1 Propellant Mass").grid(row=6)
        tk.Label(top, text="Stage 1 Engine Mass").grid(row=7)
        tk.Label(top, text="Stage 1 Thrust").grid(row=8)
        tk.Label(top, text="Stage 1 Burn Time").grid(row=9)
        tk.Label(top, text="Stage 1 ISP").grid(row=10)
        tk.Label(top, text="Stage 2 Propellant Mass").grid(row=11)
        tk.Label(top, text="Stage 2 Engine Mass").grid(row=12)
        tk.Label(top, text="Stage 2 Thrust").grid(row=13)
        tk.Label(top, text="Stage 2 Burn Time").grid(row=14)
        tk.Label(top, text="Stage 2 ISP").grid(row=15)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        e5 = tk.Entry(top)
        e6 = tk.Entry(top)
        e7 = tk.Entry(top)
        e8 = tk.Entry(top)
        e9 = tk.Entry(top)
        e10 = tk.Entry(top)
        e11 = tk.Entry(top)
        e12 = tk.Entry(top)
        e13 = tk.Entry(top)
        e14 = tk.Entry(top)
        e15 = tk.Entry(top)
        e16 = tk.Entry(top)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=7, column=1)
        e9.grid(row=8, column=1)
        e10.grid(row=9, column=1)
        e11.grid(row=10, column=1)
        e12.grid(row=11, column=1)
        e13.grid(row=12, column=1)
        e14.grid(row=13, column=1)
        e15.grid(row=14, column=1)
        e16.grid(row=15, column=1)

        top.mainloop()
	
	else:
		tk.Label(top, text="Outside Diameter").grid(row=0)
        tk.Label(top, text="Stage 1 Height").grid(row=1)
        tk.Label(top, text="Stage 2 Height").grid(row=2)
        tk.Label(top, text="Stage 3 Height").grid(row=3)
        tk.Label(top, text="Payload Fairing Height").grid(row=4)
        tk.Label(top, text="Payload Mass").grid(row=5)
        tk.Label(top, text="Stage 1 Propellant Mass").grid(row=6)
        tk.Label(top, text="Stage 1 Engine Mass").grid(row=7)
        tk.Label(top, text="Stage 1 Thrust").grid(row=8)
        tk.Label(top, text="Stage 1 Burn Time").grid(row=9)
        tk.Label(top, text="Stage 1 ISP").grid(row=10)
        tk.Label(top, text="Stage 2 Propellant Mass").grid(row=11)
        tk.Label(top, text="Stage 2 Engine Mass").grid(row=12)
        tk.Label(top, text="Stage 2 Thrust").grid(row=13)
        tk.Label(top, text="Stage 2 Burn Time").grid(row=14)
        tk.Label(top, text="Stage 2 ISP").grid(row=15)
        tk.Label(top, text="Stage 3 Propellant Mass").grid(row=16)
        tk.Label(top, text="Stage 3 Engine Mass").grid(row=17)
        tk.Label(top, text="Stage 3 Thrust").grid(row=18)
        tk.Label(top, text="Stage 3 Burn Time").grid(row=19)
        tk.Label(top, text="Stage 3 ISP").grid(row=20)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        e5 = tk.Entry(top)
        e6 = tk.Entry(top)
        e7 = tk.Entry(top)
        e8 = tk.Entry(top)
        e9 = tk.Entry(top)
        e10 = tk.Entry(top)
        e11 = tk.Entry(top)
        e12 = tk.Entry(top)
        e13 = tk.Entry(top)
        e14 = tk.Entry(top)
        e15 = tk.Entry(top)
        e16 = tk.Entry(top)
        e17 = tk.Entry(top)
        e18 = tk.Entry(top)
        e19 = tk.Entry(top)
        e20 = tk.Entry(top)
        e21 = tk.Entry(top)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=7, column=1)
        e9.grid(row=8, column=1)
        e10.grid(row=9, column=1)
        e11.grid(row=10, column=1)
        e12.grid(row=11, column=1)
        e13.grid(row=12, column=1)
        e14.grid(row=13, column=1)
        e15.grid(row=14, column=1)
        e16.grid(row=15, column=1)
        e17.grid(row=16, column=1)
        e18.grid(row=17, column=1)
        e19.grid(row=18, column=1)
        e20.grid(row=19, column=1)
        e21.grid(row=20, column=1)

        top.mainloop()

#Call main.py to calculate and write to output file

#Close input & ouput files
r.close()
w.close()

#End of code