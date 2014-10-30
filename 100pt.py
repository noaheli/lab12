#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the buttons, the oval moves to the left or right

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "Blue")
		self.button2.grid(row=0,column=1)
	        # Add a second button!
				
		
						
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2.bind("<Button-1>", self.button2Click)
		# Create the code to bind an action to the second button
		# Do not change "<Button-1>"
		 
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event): 
		global oval
		global drawpad
		drawpad.move(oval, -10, 0)
	def button2Click(self, event): 
		global oval
		global drawpad
		drawpad.move(oval, 10, 0)
	
		
myapp = MyApp(root)
root.mainloop()