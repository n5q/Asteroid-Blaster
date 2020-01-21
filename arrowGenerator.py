
###  THIS SCRIPT GENERATES THE ARROW KEYS TO BE USED ON THE SHIP SELECTION SCREEN  ###
###  THESE ARE NOT DRAWN IN THE GAME BECAUSE SINCE THE GAME RUNS IN FULL SCREEN    ###
###  THE POSITION OF THE X AND Y VALUES WILL VARY DEPENDING ON THE RESOLUTION OF   ###
###  THE MONITOR BEING USED MAKING THE UI INCONSISTENT AND BROKEN                  ###



from tkinter import Tk, Canvas

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