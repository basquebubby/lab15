#########################################
#
#    200pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4
width = 480
height = 320

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "green")
		self.down.grid(row=2,column=1)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "green")
		self.right.grid(row=1,column=2)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "green")
		self.left.grid(row=1,column=0)
		
		self.upright = Button(self.myContainer1)
		self.upright.configure(text="UR", background= "lightblue")
		self.upright.grid(row=0,column=2)
		
		self.upleft = Button(self.myContainer1)
		self.upleft.configure(text="UL", background= "lightblue")
		self.upleft.grid(row=0,column=0)
		
		self.downright = Button(self.myContainer1)
		self.downright.configure(text="DR", background= "lightblue")
		self.downright.grid(row=2,column=2)
		
		self.downleft = Button(self.myContainer1)
		self.downleft.configure(text="DL", background= "lightblue")
		self.downleft.grid(row=2,column=0)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                self.down.bind("<Button-1>", self.moveDown)
                self.right.bind("<Button-1>", self.moveRight)
                self.left.bind("<Button-1>", self.moveLeft)
                self.upright.bind("<Button-1>", self.moveUpRight)
                self.upleft.bind("<Button-1>", self.moveUpLeft)
                self.downright.bind("<Button-1>", self.moveDownRight)
                self.downleft.bind("<Button-1>", self.moveDownLeft)
                
		# This creates the drawpad - no need to change this 
	        drawpad.pack()
	        self.animate()

		
	
	def moveUp(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,0,-10)
                if py2 <= 0:
                    drawpad.move(player,0,30)
        
        def moveDown(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,0,10)
                if py1 >= height:
                    drawpad.move(player,0,-30)
        
        def moveRight(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,10,0)
                if px1 >= width:
                    drawpad.move(player,-30,0)
        
        def moveLeft(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,-10,0)
                if px2 <= 0:
                    drawpad.move(player,30,0)
        
        def moveUpRight(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,10,-10)
                if py2 <= 0 or px1 >= width:
                    drawpad.move(player,-30,30)
        
        def moveUpLeft(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,-10,-10)
                if py2 <= 0 or px2 <= 0:
                    drawpad.move(player,30,30)
                    
        def moveDownRight(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,10,10)
                if py1 >= height or px1 >= width:
                    drawpad.move(player,-30,-30)
        
        def moveDownLeft(self, event):   
		global player
		global drawpad
		px1,py1,px2,py2 = drawpad.coords(player)
		global width
		global height
                drawpad.move(player,-10,10)
                if py1 >= height or px2 <= 0:
                    drawpad.move(player,30,-30)
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    global yesWeHit
	    # Insert the code here to make the target move, bouncing on the edges    
	    x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > drawpad.winfo_width(): 
                direction = -4
            elif x1 < 0:
                direction = 4
            drawpad.move(target,direction,0)
               
        #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
        
        # Use the value of didWeHit to create an if statement
        # that determines whether to run drawpad.after(1,self.animate) or not
            if didWeHit is False:
                drawpad.after(1, self.animate) 
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global didWeHit
                global player
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                px1,py1,px2,py2 = drawpad.coords(player)
                if ((px1 >= (tx1-1)) and (px2 <= (tx2+1))) and ((py1 >= (ty1-1)) and (py2 <= (ty2+1))):
                    return True
                else:
                    return False
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)

                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()