# Imports go at the top
from microbit import *

#Pullan's Game

screenSize = [5,5]
delay = 125

def lightRow(size):
    position = []
    for i in range(size):
        position.append(i+1)
    return position

def plotLights(xCoords, yCoords):
    for i in range(len(xCoords)) :
        if xCoords[i] in range(screenSize[0]):
            if yCoords[i]  in range(screenSize[1]):
                display.set_pixel(xCoords[i],yCoords[i],9)

def unPlotLights(xCoords, yCoords):
    for i in range(len(xCoords)):
        if xCoords[i] in range(screenSize[0]):
            if yCoords[i] in range(screenSize[1]):
                display.set_pixel(xCoords[i], yCoords[i],0)

def plotLightsYZero(xCoords):
    for x in range(len(xCoords)):
        if xCoords[x] in range(screenSize[0]):
            display.set_pixel(xCoords[x],0,9)   
def moveIt(ar,counter):
    for k in range(len(ar)):
        if ar[k] in range(screenSize[0]):
            display.set_pixel(ar[k],0,0)
        ar[k] = k + 5 - abs(((counter+5)%16) - 8)
    #display.set_pixel(ar[k],0,9)
    plotLightsYZero(ar) #problem offurs becasue drawing dots off screen

def lineMoveBeforeA(rip):
    i = 0;
    while not button_a.is_pressed():
        moveIt(rip, i)
        sleep(delay)
        i = i+1

def flashRow(row, amount) :
        return
def falling(fallNRows): #detects which LEDs are visible and lowers them N rows. Then returns the number of visible lights in the row
    lightsOnTopRowFalling = []
    blankY = []
    for x in range(screenSize[0]):
        if (display.get_pixel(x, 0)):
            blankY.append(0)
            lightsOnTopRowFalling.append(x)
    for i in range(fallNRows) :
        unPlotLights(lightsOnTopRowFalling, blankY)
        for y in range(len(blankY)): 
            blankY[y] = blankY[y]+1
        plotLights(lightsOnTopRowFalling, blankY)
        sleep(100) 
    
    for x in range(len(lightsOnTopRowFalling)):
        if (fallNRows < screenSize[1]-1):
            if not display.get_pixel(lightsOnTopRowFalling[x], fallNRows + 1):
                display.set_pixel(lightsOnTopRowFalling[x], fallNRows,0)
    sleep(100)
    
    visibleLights = 0
    for x in range(screenSize[0]):
        if display.get_pixel(x,fallNRows):
            visibleLights = visibleLights + 1
    return visibleLights

#Main Program
display.clear()
lQ = 3 #light Quantity is the number of lights in play
rip = lightRow(3)
plotLightsYZero(rip)

for round in range(screenSize[1]):
    rip = lightRow(lQ)
    lineMoveBeforeA(rip)
    delay = 0.8*delay
    #flashRow(rip,10)
    lQ = falling(screenSize[1] - round -1)
    sleep(10)