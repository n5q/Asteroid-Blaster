from tkinter import Tk, Canvas, PhotoImage
from random import randint
from math import cos, sin, atan2, sqrt, pi, radians, degrees
from time import time, sleep

tk = Tk()
screen = Canvas(tk, width=146, height=143, bg="white")
screen.pack()
x=5
y=0
for i in range(14):
	screen.create_rectangle(x,y,x+12,y+7,fill="grey66",outline="grey66")
	screen.create_rectangle(x,y,x+10,y+5,fill="black")

	x+=10
	y+=5
x-=10
y++10
for i in range(14):
	screen.create_rectangle(x,y+1,x+12,y+8,fill="grey66",outline="grey66")
	screen.create_rectangle(x,y,x+10,y+5,fill="black")
	x-=10
	y+=5
screen.create_rectangle(0,6,9,y-6,fill="grey66",outline="grey66")
screen.create_rectangle(0,0,7,y+3,fill="black")

screen.update()
screen.postscript(file="arrow.gif", colormode='color')