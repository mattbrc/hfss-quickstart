from Tkinter import *
from math import *


class MainApplication:
	
	#clears all user input values
	def clear_button_press(self, value):
		self.entry1.delete(0, "end")
		self.entry2.delete(0, "end")
		self.entry3.delete(0, "end")
		self.entry4.delete(0, "end")
		self.entry5.delete(0, "end")
		
	#Gets all user input values		
	def enter_button_press(self, value):
		
		#Gets frequency input
		frequency = float(self.fEntry.get())
		
		#Gets Epsilon 1 input
		Er1 = float(self.Er1Entry.get())
		
		#Gets Height 1 input
		h1 = float(self.h1Entry.get())
		
		#Gets Epsilon 2 input
		Er2 = float(self.Er2Entry.get())
		
		#Gets Height 2 input
		h2 = float(self.h2Entry.get())
		
		#Test to make sure inputs are working
		print(frequency, " ", Er1, " ", h1, " ", Er2, " ", h2)		
		
		#Speed of light and pi
		c = 299792458
		pi = 3.14159265359
	
		#Calculate patch width
		w = c / (2 * frequency * 10**9 * sqrt((Er1 + 1)/2))
		
		#Calculate Effective dielectric
		eeff = ((Er1 + 1) / 2) + ((Er1 -1) * ((1 + 12*(h1 / w))**(-0.5)) / 2)
		
		#Calculate Delta L
		deltaL = h1 * ( (.412 * (eeff + 0.3) * ((w / h1) + 0.264)) / ((eeff-0.258) * ((w / h1) + 0.8)) )
		
		#Calculate l0
		l0 = c / (frequency * 10**9)
		
		#Calculate leff
		leff = c / (2 * frequency*10**9 * sqrt(eeff))
		
		#Calculate L
		l = leff - 2*deltaL
		
		#Calculate Rin
		rIn = 90 * ((Er1**2 / (Er1 - 1)) * (l / w))
		
		#Calculate patch feed point
		q = 50 / rIn
		y0 = acos(q) * (l/w)
		
		#Calculate cutout values
		g = (l0 / sqrt(Er1))
		ls = 0.3 * g
		ws = 0.065 * g
		ps = 0.135 * g
		
		""" test all nums
		print(w)
		print eeff
		print deltaL
		print l0
		print l
		print rIn
		print y0
		print (ls, ws, ps)
		"""
		
	#Use to run HFSS, need hycohanz		
	#def open_button_press(self):
			
					
	def __init__(self, root):
	
		#Defines title for the app
		root.title("HFSS E-Patch Build 1.0.0") 
		
		#Defines width and height of the app
		root.geometry("316x360")
		
		#Block user from resizing window
		root.resizable(width=False, height=False)
		
		#Will hold the 1st entry
		self.fEntry = StringVar(root, value="")
		
		#Create text box for 1st Entry
		self.entry1 = Entry(root, textvariable=self.fEntry, width=15)
		self.entry1.grid(row=0, column=1)
		
		#Will hold the 2nd entry
		self.Er1Entry = StringVar(root, value="")
		
		#Create text box for 2nd entry
		self.entry2 = Entry(root, textvariable=self.Er1Entry, width=15)
		self.entry2.grid(row=1, column=1)
		
		#Will hold the 3rd entry
		self.h1Entry = StringVar(root, value="")
		
		#Create text box for 3rd entry
		self.entry3 = Entry(root, textvariable=self.h1Entry, width=15)
		self.entry3.grid(row=2, column=1)
		
		#Will hold the 4th entry
		self.Er2Entry = StringVar(root, value="")
		
		#Create text box for 4th entry
		self.entry4 = Entry(root, textvariable=self.Er2Entry, width=15)
		self.entry4.grid(row=3, column=1)
		
		#Will hold the 5th entry
		self.h2Entry = StringVar(root, value="")
		
		#Create text box for 5th entry
		self.entry5 = Entry(root, textvariable=self.h2Entry, width=15)
		self.entry5.grid(row=4, column=1)
		
		#Create Enter button
		self.button1 = Button(root, text="Enter",
						command=lambda: self.enter_button_press("Enter"), width=10, font=("Courier"))
		
		self.button1.grid(row=5, column=1, sticky=W)						
		
		#Create Clear inputs button
		self.button2 = Button(root, text="Clear",
						command=lambda: self.clear_button_press("Clear"), width=10, font=("Courier"))
		
		self.button2.grid(row=6, column=1, stick=W)
		
		#Create labels for user input
		self.label1 = Label(root, text="Frequency (GHz)", font=("Courier", 12)).grid(row=0, column=0, sticky=W)
		
		self.label2 = Label(root, text="Er1 (Dielectric Constant)", font=("Courier", 12)).grid(row=1, column=0, sticky=W)
		
		self.label3 = Label(root, text="Height 1 (m)", font=("Courier", 12)).grid(row=2, column=0, sticky=W)
		
		self.label4 = Label(root, text="Er2 (Dielectric Constant)", font=("Courier", 12)).grid(row=3, column=0, sticky=W)
		
		self.label5 = Label(root, text="Height 2 (m)", font=("Courier", 12)).grid(row=4, column=0, sticky=W)
		
	
#Get the root window object				
root = Tk()

#Create the app
HFSSGui = MainApplication(root)   

#Run the app until exited
root.mainloop()
