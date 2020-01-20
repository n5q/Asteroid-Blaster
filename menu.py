from tkinter import Tk, Canvas, PhotoImage
from random import randint
from math import cos, sin, atan2, sqrt, pi, radians, degrees
from time import time, sleep


tk = Tk()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
tk.attributes("-fullscreen", True)
screen = Canvas(tk, width=width, height=height, bg="black")	
screen.pack()

screen.update()

screen.create_rectangle(0,0,150,height,fill="white")
screen.create_rectangle(width-150,0,width,height,fill="white")

arrowR= PhotoImage(file="arrowR.gif")
arrowL = PhotoImage(file="arrowL.gif")
screen.create_image(width-75,(height/2),image=arrowR)
screen.create_image(75,height/2,image=arrowL)
screen.create_text((width/2)+3,53,text= "S E L E C T  S H I P",font="Courier 45 bold",fill="grey33")
screen.create_text(width/2,50,text= "S E L E C T  S H I P",font="Courier 45 bold",fill="white")

screen.create_text(width/2, height-100, text="START GAME",font="Courier 45",fill="white",activefill="grey50")
screen.create_rectangle((width/2)-200,height-175,(width/2)+200,height-35,outline="white",width=3)

def motion(event):
	global x,y
	x, y = event.x, event.y
def click(event):
	if (x in range(round((width/2)-200),round((width/2)+200))) and y in range(height-175,height-35):
		runGame()

screen.bind("<Motion>", motion)
screen.bind("<Button 1>", click)
screen.update()
screen.mainloop()
