
from tkinter import Tk, Canvas, PhotoImage
from random import randint
from math import cos, sin, atan2, sqrt, pi, radians, degrees
from time import time, sleep
from os import name
if name == "nt":
    from winsound import PlaySound, SND_LOOP, SND_ASYNC, SND_PURGE


tk = Tk()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
tk.attributes("-fullscreen", True)
screen = Canvas(tk, width=width, height=height, bg="black") 
screen.pack()

def menu():
    global loop, gameStarted
    gameStarted = False
    loop = True
    if name == "nt":
        PlaySound('Loop.wav', SND_LOOP + SND_ASYNC)
    setInitialValues()
    while loop == True:
        if randint(1, 10) == 1:
            if randint(1,2) == 1:
                drawasteroidR()
            else:
                drawasteroidL()
            
        moveasteroids()

        a = screen.create_text((width/2)+3,103,text= "A S T E R O I D  B L A S T E R",font="fixedsys 75 bold",fill="grey33")
        b = screen.create_text(width/2,100,text= "A S T E R O I D  B L A S T E R",font="fixedsys 75 bold",fill="white")
        c = screen.create_text((width/2)+3, height-147, text="START GAME",font="fixedsys 45",fill="green2")
        d = screen.create_text(width/2, height-150, text="START GAME",font="fixedsys 45",fill="white",activefill="grey50")
        e = screen.create_rectangle((width/2)-222,height-222,(width/2)+228,height-82,outline="green2",width=3)
        f = screen.create_rectangle((width/2)-225,height-225,(width/2)+225,height-85,outline="white",width=3)
        g = screen.create_rectangle((width/2)-222,height-497,(width/2)+228,height-357,outline="yellow4",width=3)
        h = screen.create_rectangle((width/2)-225,height-500,(width/2)+225,height-360,outline="white",width=3)
        
        screen.update()
        sleep(0.01)
        clean()
        screen.delete(a,b,c,d,e,f)

def shipSelector():
    global arrowR, arrowL
    screen.delete("all")
    screen.create_rectangle(0,0,150,height,fill="white")
    screen.create_rectangle(width-150,0,width,height,fill="white",activefill="grey33")

    arrowR = PhotoImage(file="arrowR.gif")
    arrowL = PhotoImage(file="arrowL.gif")
    screen.create_image(width-75,(height/2),image=arrowR)
    screen.create_image(75,height/2,image=arrowL)
def motion(event):
    global x,y,loop
    x, y = event.x, event.y
    x in range(round((width/2)-200),round((width/2)+200))

def click(event):
    if (x in range(round((width/2)-200),round((width/2)+200))) and y in range(height-175,height-35) and gameStarted == False:
        if name == "nt":
            PlaySound(None, SND_PURGE)
        loop = False
        shipSelector()



def setInitialValues():

    global radius, playerSpeed, asteroid, radius, speed, minRadius, maxRadius
    global spawnChance, points, end, maxSpeed
    global playerAngle, angles, playerStart, xCentre, yCentre, line, arc
    global angleOutput, n, r, X, Y, dtheta, xc, yc, theta, arrayX, arrayY
    global pos1, pos2, pos3, player, playerSpeedX, playerspeedY, maxPlayerSpeed
    global bullets, bulletAngle, bulletSpeedsX, bulletSpeedsY, lastBullet
    global startTime


    # else:
    radius = 15
    playerSpeed = 10
    asteroid = []
    radius = []
    speed = []
    minRadius = 15
    maxRadius = 30
    maxSpeed = 10
    spawnChance = 35 
    points = 0  
    enemyChance = 50
    lives = 3

    n=360
    r= -20
    X = 380
    Y = 380

    dtheta = 2*pi/n

    xc = X - r 
    yc = Y - r
    theta = 0

    arrayX = [X]
    arrayY = [Y]
    for i in range(n):



        #CIRCULAR MOTION 
        theta += dtheta

        X = r*cos(theta) + xc
        Y = r*sin(theta) + yc
        arrayX.append(X)
        arrayY.append(Y)


    pos1 = 90
    pos2 = 305
    pos3 = 233

    bullets = []
    bulletAngle = []
    bulletSpeedsX = []
    bulletSpeedsY = []



    coords1 = (arrayX[pos1], arrayY[pos1])
    coords2 = (arrayX[pos2], arrayY[pos2])
    coords3 = (arrayX[pos3], arrayY[pos3])



    maxPlayerSpeed = 2
    playerSpeedX = 0
    playerspeedY = -1

    lastBullet = time()
    
    startTime = time()
    


def drawObjects():

    global player, playerCircle, timeCounter, score, playerAngle, timer

    player = screen.create_polygon(coords1,coords2,coords3,fill="yellow")
    screen.create_text(50,30, text="SCORE", fill="white",font=("helvetica", 16))
    screen.create_text(200,30, text="TIME SURVIVED", fill="white",font=("helvetica", 16))
    score = screen.create_text(50,60, fill="white",font=("helvetica", 16))
    timer = screen.create_text(200,60, fill="white",font=("helvetica", 16))

def updateScore(scoreText):
    screen.itemconfig(score, text=str(scoreText))

def updateTime():
    global currentTime
    currentTime = time() - startTime
    screen.itemconfig(timer, text=str(round(currentTime,1)))



def keyPress(event):
    global pos1, pos2, pos3, maxPlayerSpeed

    if event.keysym in ["a","Left"]:
        pos1 -= 5
        pos2 -= 5
        pos3 -= 5
        if pos1 <= 0:
            pos1 += 359
        if pos2 <= 0:
            pos2 += 359
        if pos3 <= 0:
            pos3 += 359 

    elif event.keysym in ["d","Right"]:
        pos1 += 5
        pos2 += 5
        pos3 += 5
        if pos1 >= 360:
            pos1 -= 359
        if pos2 >= 360:
            pos2 -= 359
        if pos3 >= 360:
            pos3 -= 359

    elif event.keysym in ["w", "Up"]:
        maxPlayerSpeed = 6


    elif event.keysym == "Escape":
        tk.destroy()

def keyUp(event):
    global maxPlayerSpeed
    if event.keysym in ["w", "Up"]:
        maxPlayerSpeed = 2



    

def drawasteroidR():
    x = 0 - 100
    y = randint(0, height)
    r = randint(minRadius, maxRadius)
    draw = screen.create_oval(x-r, y-r, x+r, y+r, outline="grey69",width="4",fill="grey20")
    asteroid.append(draw)
    radius.append(r)
    speed.append(randint(1,maxSpeed)*-1)

def drawasteroidL():
    x = width + 100
    y = randint(0, height)
    r = randint(minRadius, maxRadius)
    draw = screen.create_oval(x-r, y-r, x+r, y+r, outline="grey69",width="4",fill="grey20")
    asteroid.append(draw)
    radius.append(r)
    speed.append(randint(1,maxSpeed))


def moveasteroids():
    for i in range(len(asteroid)):
        screen.move(asteroid[i], -speed[i], 0)

def movePlayer():
    global coords1, coords2, coords3, player, playerspeedY, playerSpeedX, arrayX
    global arrayY, maxPlayerSpeed
    coords1 = (arrayX[pos1], arrayY[pos1])
    coords2 = (arrayX[pos2], arrayY[pos2])
    coords3 = (arrayX[pos3], arrayY[pos3])
    try: screen.delete(player)
    except: pass
    player = screen.create_polygon(coords1,coords2,coords3,fill="yellow")
    playerSpeedX = -(maxPlayerSpeed * cos(radians(pos1)))
    playerspeedY = -(maxPlayerSpeed * sin(radians(pos1)))
    for i in range(len(arrayX)):
        arrayX[i] += playerSpeedX
        arrayY[i] += playerspeedY

def spawnBullet():
    global b, bulletAngle, pos1, bulletSpeeds, bulletSpeedsX, bulletSpeedsY, lastBullet

    if (time() - lastBullet) < 0.5:
        pass
    else:
        b = screen.create_oval(coords1[0]+3,coords1[1]+3,coords1[0]-3,coords1[1]-3,fill="red",outline="red")
        bullets.append(b)
        bulletAngle.append(pos1)
        maxBulletSpeed = 7
        bulletSpeedsX.append (-(maxBulletSpeed * cos(radians(pos1))))
        bulletSpeedsY.append (-(maxBulletSpeed * sin(radians(pos1))))
        lastBullet = time()

def moveBullets():
    for i in range(len(bullets)):
        screen.move(bullets[i], bulletSpeedsX[i], bulletSpeedsY[i])



def checkEdges():
    if (screen.coords(player))[1] <= 0:
        endGame()
    elif (screen.coords(player)[0]) <= 0:
        endGame()
    if (screen.coords(player))[1] >= height:
        endGame()
    elif (screen.coords(player)[0]) >= width:
        endGame()




def getCoords(asteroid):
    xy = screen.coords(asteroid)
    x = (xy[0] + xy[2])/2
    y = (xy[1] + xy[3])/2
    return(x,y)

def deleteAsteroid(i):
    global radius,colours,speed,asteroid
    del radius[i]
    del speed[i]
    screen.delete(asteroid[i])
    del asteroid[i]

def deleteBullet(i):
    global bullets, bulletAngle, bulletSpeedsX, bulletSpeedsY
    del bulletAngle[i]
    del bulletSpeedsX[i]
    del bulletSpeedsY[i]
    screen.delete(bullets[i])
    del bullets[i]

def clean():
    for i in range(len(asteroid)-1, -1, -1):
        x = getCoords(asteroid[i])
        x = x[0]
        if x < -100 or x > width+100:
            deleteAsteroid(i)

    for i in range(len(bullets)-1, -1, -1):
        x = getCoords(bullets[i])
        if ((x[0] < -20 or x[0] > width + 20) or (x[1] < -20 or x[1] > height + 20)):
            deleteBullet(i)


def getDistance(a,b):
    x1 = getCoords(a)
    x1 = x1[0]
    y1 = getCoords(a)
    y1 = y1[1]
    x2 = getCoords(b)
    x2 = x2[0]
    y2 = getCoords(b)
    y2 = y2[1]
    return(sqrt((x2-x1)**2 + (y2-y1)**2))

def collision():
    points = 0
    for i in range(len(asteroid)-1, -1, -1):
        if getDistance(player, asteroid[i]) < (15 + radius[i]):
            endGame()
    try:
        for i in range(len(asteroid)-1, -1, -1):
            for j in range(len(bullets)-1, -1, -1):
                if getDistance(bullets[j], asteroid[i]) < (15 + radius[i]):
                    points += (radius[i] + speed[i])
                    deleteAsteroid(i)
    except:
        pass
    return(points)


def endGame():
    global bullets, gameRunning
    gameRunning = False

    for i in range(len(bullets)-1,-1,-1):
        screen.delete(bullets[i])

    screen.create_polygon(coords1,coords2,coords3,fill="yellow")

    screen.create_text(width/2, height/2, text="GAME OVER", fill="white", font=("helvetica", 45))

    screen.create_text(width/2, (height/2)+45, text="Score:  " + str(points), fill="white",font=("helvetica", 16))
    
    screen.create_text(width/2, (height/2)+90, text="Time Survived:  " + str(round(currentTime,2)) + " seconds", fill="white",font=("helvetica", 16))




def runGame():
    global end, points,spawnChance,enemyChance,gameRunning, player, pos1
    setInitialValues()
    drawObjects()
    scoreCounter = time()
    gameRunning = True
    while True:
        if randint(1, spawnChance) == 1:
            if randint(1,2) == 1:
                drawasteroidR()
            else:
                drawasteroidL()
        if gameRunning == True:
            
            moveasteroids()
            movePlayer()
            spawnBullet()
            moveBullets()
            checkEdges()
        clean()
        points += collision()
        updateScore(points)
        if (time() - scoreCounter) > 1:
            points += 10
            updateScore(points)
            scoreCounter = time()
        updateTime()
        screen.update()
        sleep(0.01)
        screen.delete(player)
    endGame()

tk.after(0,menu)
screen.bind("<Key>", keyPress)
screen.bind("<KeyRelease>", keyUp)
screen.bind("<Motion>", motion)
screen.bind("<Button 1>", click)
screen.pack()
screen.focus_set()
screen.mainloop()

