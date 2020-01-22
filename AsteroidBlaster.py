
###  THE UI AND FONTS WILL BE BROKEN ON SCREENS WITH RESOLUTIONS LOWER THAN   ###
###  1280x1024 OR SMALL SCREENS SUCH AS LAPTOPS BECAUSE I HAVE NOT TESTED     ###
###  ON ANYTHING SMALLER. MOST FONTS ARE BROKEN ON MAC/LINUX BECAUSE FIXEDSYS ###
###  IS A WINDOWS FONT                                                        ###


from tkinter import Tk, Canvas, PhotoImage
from random import randint
from math import cos, sin, atan2, sqrt, pi, radians, degrees
from time import time, sleep
from json import load, dump, loads

# WINSOUND IS NOT AVALIABLE ON MACOS/LINUX SO IF YOU ARE PLAYING ON EITHER OF THOSE PLATFORMS
# YOU WILL JUST HAVE TO PLAY WITHOUT SOUND :/

from os import name
if name == "nt": Windows = True
if Windows:
    from winsound import PlaySound, SND_LOOP, SND_ASYNC, SND_PURGE


tk = Tk()

width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()


tk.attributes("-fullscreen", True)
screen = Canvas(tk, width=width, height=height, bg="black") 
screen.pack()
firstRun = True


def menu():
    global loop, gameStarted, instruction, selector, highscore
    selector = False
    gameStarted = False
    loop = False
    instruction = False
    screen.delete("all")
    screen.update()
    loop = True
    if firstRun == True:
        if Windows:
            PlaySound('Loop.mp3', SND_LOOP + SND_ASYNC)

    with open("Highscores.json","r") as data:
        obj = loads(data.read())
        highscore = str(obj["highScore"])

    setInitialValues()
    while loop == True:
        if randint(1, 8) == 1:
            if randint(1,2) == 1:
                drawasteroidR()
            else:
                drawasteroidL()
            
        moveasteroids()


        a = screen.create_text((width/2)+3,103,text= "A S T E R O I D  B L A S T E R",font="fixedsys 75 bold",fill="grey33")
        b = screen.create_text(width/2,100,text= "A S T E R O I D  B L A S T E R",font="fixedsys 75 bold",fill="white")
        c = screen.create_text((width/2)+3, height-153, text="START GAME",font="fixedsys 45",fill="green2")
        d = screen.create_text(width/2, height-155, text="START GAME",font="fixedsys 45",fill="white",activefill="grey50")
        e = screen.create_rectangle((width/2)-222,height-222,(width/2)+228,height-82,outline="green2",width=3)
        f = screen.create_rectangle((width/2)-225,height-225,(width/2)+225,height-85,outline="white",width=3)
        g = screen.create_rectangle((width/2)-247,height-397,(width/2)+253,height-257,outline="gold",width=3)
        h = screen.create_rectangle((width/2)-250,height-400,(width/2)+250,height-260,outline="white",width=3)
        i = screen.create_text((width/2)+3,height-327, text="INSTRUCTIONS",font="fixedsys 45",fill="gold",activefill="grey50")
        j = screen.create_text(width/2,height-330, text="INSTRUCTIONS",font="fixedsys 45",fill="white",activefill="grey50")
        k = screen.create_text(width/2,height-650,text="HIGHSCORE: " + highscore,font="fixedsys 36",fill="white")

        screen.update()
        sleep(0.01)
        clean()
        screen.delete(a,b,c,d,e,f,g,h,i,j,k)

def instructions():
    global instruction,firstRun,loop
    firstRun = False
    instruction = True
    loop = False
    screen.delete("all")
    screen.update()
    loop = True

    setInitialValues()
    while loop == True:
        if randint(1, 8) == 1:
            if randint(1,2) == 1:
                drawasteroidR()
            else:
                drawasteroidL()
            
        moveasteroids()   

        a = screen.create_text((width/2)+3,78,text= "I N S T R U C T I O N S",font="fixedsys 75 bold",fill="grey33")
        b = screen.create_text(width/2,75,text= "I N S T R U C T I O N S",font="fixedsys 75 bold",fill="white")
        c = screen.create_text(width/2, 400, font="fixedsys 22",fill="white", text =
            "MOVE YOUR PLAYER USING THE LEFT AND RIGHT ARROW KEYS, HOLD THE UP ARROW KEY\nTO GET A SPEED BOOST BUT KEEP IN MIND THAT YOU CANNOT TURN WHILE BOOSTING.\nYOU CAN PRESS THE ESCAPE KEY AT ANY TIME TO QUIT THE GAME, OR Q TO RETURN\nTO THE MENU.\n \nYOUR SHIP AUTOMATICALLY FIRES BULLETS, IF A BULLET HITS AN ASTEROID\nYOU WILL GET POINTS, THE SMALLER THE ASTEROID AND THE FASTER IT IS MOVING\nTHE MORE POINTS YOU WILL GET. YOU ALSO GAIN 10 POINTS FOR EACH SECOND\nYOU SURVIVE. IF YOU HIT THE EDGE OF THE SCREEN OR AN ASTEROID YOU WILL\nDIE AND THE GAME WILL BE OVER.") 
        d = screen.create_rectangle((width/2)-222,height-397,(width/2)+228,height-257,outline="gold",width=3)
        e = screen.create_rectangle((width/2)-225,height-400,(width/2)+225,height-260,outline="white",width=3)
        f = screen.create_text((width/2)+3,height-327, text="BACK",font="fixedsys 45",fill="gold",activefill="grey50")
        g = screen.create_text(width/2,height-330, text="BACK",font="fixedsys 45",fill="white",activefill="grey50")


        screen.update()
        sleep(0.01)
        clean()
        screen.delete(a,b,c,d,e,f,g)


def shipSelector():
    global arrowR, arrowL, loop, instruction, selector, ship, color
    ship = 0
    loop = False
    screen.delete("all")
    screen.update()
    loop = True
    instruction = True
    selector = True

    setInitialValues()
    while loop == True:
        if randint(1, 8) == 1:
            if randint(1,2) == 1:
                drawasteroidR()
            else:
                drawasteroidL()
            
        moveasteroids()

        ships = ["yellow","blue","red","green"]
        reloads = [0.3,1.5,0.2,1]
        rotations = [5,12,2,15]
        bulletSpeeds = [15,25,4,25]
        speeds = [3,4,1,1.5]
        color = ships[ship]

        screen.create_rectangle(0,0,150,height,fill="white",activefill="grey33")
        screen.create_rectangle(width-150,0,width,height,fill="white",activefill="grey33")
        arrowR = PhotoImage(file="arrowR.gif")
        arrowL = PhotoImage(file="arrowL.gif")
        a = screen.create_image(width-75,(height/2),image=arrowR)
        b = screen.create_image(75,height/2,image=arrowL)
        c = screen.create_text((width/2)+3, height-153, text="START GAME",font="fixedsys 45",fill="green2")
        d = screen.create_text(width/2, height-155, text="START GAME",font="fixedsys 45",fill="white",activefill="grey50")
        e = screen.create_rectangle((width/2)-222,height-222,(width/2)+228,height-82,outline="green2",width=3)
        f = screen.create_rectangle((width/2)-225,height-225,(width/2)+225,height-85,outline="white",width=3)
        g = screen.create_polygon(width/2,400,(width/2)-100,700,(width/2)+100,700,fill=color)  
        h = screen.create_text(width/2,75,text="S E L E C T  S H I P",font="fixedsys 75 bold",fill="white")
        i = screen.create_text((width/2)-225,200,text="Reload Time: " + str(reloads[ship]),font = "fixedsys 22",fill="white")
        j = screen.create_text((width/2)+225,200,text="Rotation Speed: " + str(rotations[ship]),font = "fixedsys 22",fill="white")
        k = screen.create_text((width/2)-225,300,text="Bullet Speed: " + str(bulletSpeeds[ship]),font = "fixedsys 22",fill="white")
        l = screen.create_text((width/2)+225,300,text="Movement Speed: " + str(speeds[ship]),font = "fixedsys 22",fill="white")

        screen.update()
        sleep(0.01)
        clean()
        screen.delete(a,b,c,d,e,f,g,h,i,j,k,l)


def motion(event):
    global x,y,loop,ship
    x, y = event.x, event.y

def click(event):
    global ship
    if (x in range(round((width/2)-225),round((width/2)+225))) and y in range(height-225,height-85) and gameStarted == False:
        loop = False
        if selector == True:
            runGame()
        elif instruction == True:
            pass
        else:
            shipSelector()
    elif (x in range(round((width/2)-250),round((width/2)+250))) and y in range(height-400,height-260) and gameStarted == False:
        loop = False
        if instruction == False:
            instructions()
        elif selector == False:
            menu()
    if selector == True:
        if x > width-150:
            if ship == 3: ship = 0
            else: ship += 1
        if x < 150:
            if ship == 0: ship = 3
            else: ship -= 1


def setInitialValues(*args):

    global radius, asteroid, radius, speed, minRadius, maxRadius
    global spawnChance, points, end, maxSpeed
    global playerAngle, angles, playerStart, xCentre, yCentre, line, arc
    global angleOutput, n, r, X, Y, dtheta, xc, yc, theta, arrayX, arrayY
    global pos1, pos2, pos3, player, playerSpeedX, playerspeedY, maxPlayerSpeed
    global bullets, bulletAngle, bulletSpeedsX, bulletSpeedsY, lastBullet
    global startTime,coords1,coords2,coords3, maxBulletSpeed, boostSpeed, rotation
    global maxPlayerSpeed1, bulletCooldown


    radius = 15
    asteroid = []
    radius = []
    speed = []
    minRadius = 15
    maxRadius = 30
    maxSpeed = 20
    spawnChance = 30
    points = 0  
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
    playerSpeedX = 0
    playerspeedY = -1
    lastBullet = time()
    startTime = time()
    
    if args:
        maxSpeed = 10
        if args[0] == "yellow":
            bulletCooldown = 0.3
            rotation = 5
            maxBulletSpeed = 15
            maxPlayerSpeed = 3

        elif args[0] == "blue":
            bulletCooldown = 1.5
            rotation = 12
            maxBulletSpeed = 25
            maxPlayerSpeed = 4

        elif args[0] == "red":
            bulletCooldown = 0.2
            rotation = 3
            maxBulletSpeed = 4
            maxPlayerSpeed = 0.5

        elif args[0] == "green":
            bulletCooldown = 1
            rotation = 15
            maxBulletSpeed = 25
            maxPlayerSpeed = 1.5

        maxPlayerSpeed1 = maxPlayerSpeed
        boostSpeed = maxPlayerSpeed + 4

def drawObjects():

    global player, playerCircle, score, playerAngle, timer
    player = screen.create_polygon(coords1,coords2,coords3,fill=color)
    screen.create_text(50,30, text="SCORE", fill="white",font=("fixedsys", 22))
    screen.create_text(250,30, text="TIME SURVIVED", fill="white",font=("fixedsys", 22))
    score = screen.create_text(50,60, fill="white",font=("fixedsys", 20))
    timer = screen.create_text(250,60, fill="white",font=("fixedsys", 20))

def updateScore(scoreText):
    screen.itemconfig(score, text=str(scoreText))

def updateTime():
    global currentTime
    currentTime = time() - startTime
    screen.itemconfig(timer, text=str(round(currentTime,1)))



def keyPress(event):
    global pos1, pos2, pos3, maxPlayerSpeed,rotation

    if event.keysym in ["a","Left"]:
        pos1 -= rotation
        pos2 -= rotation
        pos3 -= rotation
        if pos1 <= 0:
            pos1 += 359
        if pos2 <= 0:
            pos2 += 359
        if pos3 <= 0:
            pos3 += 359 

    elif event.keysym in ["d","Right"]:
        pos1 += rotation
        pos2 += rotation
        pos3 += rotation
        if pos1 >= 360:
            pos1 -= 359
        if pos2 >= 360:
            pos2 -= 359
        if pos3 >= 360:
            pos3 -= 359

    elif event.keysym in ["w", "Up"]:
        maxPlayerSpeed = boostSpeed


    elif event.keysym == "Escape":
        if name == "nt":
            PlaySound(None, SND_PURGE)
        tk.destroy()

    elif event.keysym == "q":
        menu()

def keyUp(event):
    global maxPlayerSpeed
    if event.keysym in ["w", "Up"]:
        maxPlayerSpeed = maxPlayerSpeed1



    

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
    player = screen.create_polygon(coords1,coords2,coords3,fill=color)
    playerSpeedX = -(maxPlayerSpeed * cos(radians(pos1)))
    playerspeedY = -(maxPlayerSpeed * sin(radians(pos1)))
    for i in range(len(arrayX)):
        arrayX[i] += playerSpeedX
        arrayY[i] += playerspeedY

def spawnBullet():
    global b, bulletAngle, pos1, bulletSpeeds, bulletSpeedsX, bulletSpeedsY, lastBullet

    if (time() - lastBullet) < bulletCooldown:
        pass
    else:
        b = screen.create_oval(coords1[0]+3,coords1[1]+3,coords1[0]-3,coords1[1]-3,fill="red",outline="red")
        bullets.append(b)
        bulletAngle.append(pos1)

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

    screen.create_polygon(coords1,coords2,coords3,fill=color)

    screen.create_text(width/2, (height/2) - 50, text="GAME OVER", fill="white", font=("fixedsys", 45))

    screen.create_text(width/2, (height/2)+50, text="Score:  " + str(points), fill="white",font="fixedsys 22")
    
    screen.create_text(width/2, (height/2)+100, text="Time Survived:  " + str(round(currentTime,2)) + " seconds", fill="white",font="fixedsys 22")

    screen.create_text(width/2, (height/2)+150, text="PRESS \"Q\" TO PLAY AGAIN OR \"ESC\" TO QUIT", fill="white",font="fixedsys 22")

    with open("Highscores.json","r") as data:
        obj = load(data)
        hs = (obj["highScore"])

    if points > hs:

        with open("Highscores.json","w") as data:
            #data.write("{\n\"highScore\" : " + str(points) +"\n}")
            obj["highScore"] = points
            dump(obj, data)





def runGame():
    
    global end, points,spawnChance,gameRunning, player, pos1,loop
    PlaySound(None, SND_PURGE)
    PlaySound("Splash.mp3", SND_ASYNC + SND_LOOP)
    loop = False
    screen.delete("all")
    screen.update()
    setInitialValues(color)
    drawObjects()
    scoreshiper = time()
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
        if (time() - scoreshiper) > 1:
            points += 10
            updateScore(points)
            scoreshiper = time()
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

