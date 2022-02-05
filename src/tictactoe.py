import pygame
import time
import random
from Graphik import *

pygame.init()

black = (0,0,0)
white = (255,255,255)

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

graphik = Graphik(gameDisplay)

pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

topLeftL = ""
topMiddleL = ""
topRightL = ""

middleLeftL = ""
middleMiddleL = ""
middleRightL = ""

bottomLeftL = ""
bottomMiddleL = ""
bottomRightL = ""

moves = 0

def drawGridSlot(xpos, ypos, XorO, function):
    graphik.drawButton(xpos, ypos, 100, 100, white, black, 64, XorO, function)

def test():
    print("test")

def exit():
    pygame.quit()
    quit()

def topLeft():
    global topLeftL
    global moves
    print(topLeftL)
    if topLeftL == "":
        topLeftL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def topMiddle():
    global topMiddleL
    global moves
    print(topMiddleL)
    if topMiddleL == "":
        topMiddleL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def topRight():
    global topRightL
    global moves
    print(topRightL)
    if topRightL == "":
        topRightL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def middleLeft():
    global middleLeftL
    global moves
    print(middleLeftL)
    if middleLeftL == "":
        middleLeftL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def middleMiddle():
    global middleMiddleL
    global moves
    print(middleMiddleL)
    if middleMiddleL == "":
        middleMiddleL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def middleRight():
    global middleRightL
    global moves
    print(middleRightL)
    if middleRightL == "":
        middleRightL = "X"
        drawGrid()
        moves += 1
        computerTurn()

def bottomLeft():
    global bottomLeftL
    global moves
    print(bottomLeftL)
    if bottomLeftL == "":
        bottomLeftL = "X"
        drawGrid()
        moves += 1
        computerTurn()    

def bottomMiddle():
    global bottomMiddleL
    global moves
    print(bottomMiddleL)
    if bottomMiddleL == "":
        bottomMiddleL = "X"
        drawGrid()
        moves += 1
        computerTurn()  

def bottomRight():
    global bottomRightL
    global moves
    print(bottomRightL)
    if bottomRightL == "":
        bottomRightL = "X"
        drawGrid()
        moves += 1
        computerTurn()  

def computerTurn():
    checkForWinCondition()
    global topLeftL
    global topMiddleL
    global topRightL
    global middleLeftL
    global middleMiddleL
    global middleRightL
    global bottomLeftL
    global bottomMiddleL
    global bottomRightL
    global moves
    
    if moves != 9:
        time.sleep(1)

        went = False
        while (went == False):
            randomInt = random.randint(1,10)
            if randomInt == 1:
                if topLeftL == "":
                    topLeftL = "O"
                    went = True
                    moves += 1
            if randomInt == 2:
                if topMiddleL == "":
                    topMiddleL = "O"
                    went = True
                    moves += 1
            if randomInt == 3:
                if topRightL == "":
                    topRightL = "O"
                    went = True
                    moves += 1
            if randomInt == 4:
                if middleLeftL == "":
                    middleLeftL = "O"
                    went = True
                    moves += 1
            if randomInt == 5:
                if middleMiddleL == "":
                    middleMiddleL = "O"
                    went = True
                    moves += 1
            if randomInt == 6:
                if middleRightL == "":
                    middleRightL = "O"
                    went = True
                    moves += 1
            if randomInt == 7:
                if bottomLeftL == "":
                    bottomLeftL = "O"
                    went = True
                    moves += 1
            if randomInt == 8:
                if bottomMiddleL == "":
                    bottomMiddleL = "O"
                    went = True
                    moves += 1
            if randomInt == 9:
                if bottomRightL == "":
                    bottomRightL = "O"
                    went = True
                    moves += 1
    drawGrid()
    checkForWinCondition()
    
def drawGrid():
    centerGridX = (displayWidth//2 - 50)
    centerGridY = (displayHeight//2 - 50)
    
    graphik.drawRectangle(centerGridX - 125, centerGridY - 125, 350, 350, black)
    
    drawGridSlot(centerGridX - 125, centerGridY - 125, topLeftL, topLeft) # top row left column
    drawGridSlot(centerGridX, centerGridY - 125, topMiddleL, topMiddle) # top row middle column
    drawGridSlot(centerGridX + 125, centerGridY - 125, topRightL, topRight) # top row right column
    
    drawGridSlot(centerGridX - 125, centerGridY, middleLeftL, middleLeft) # middle row left column
    drawGridSlot(centerGridX, centerGridY, middleMiddleL, middleMiddle) # middle row middle column
    drawGridSlot(centerGridX + 125, centerGridY, middleRightL, middleRight) # middle row right column

    drawGridSlot(centerGridX - 125, centerGridY + 125, bottomLeftL, bottomLeft) # top row left column
    drawGridSlot(centerGridX, centerGridY + 125, bottomMiddleL, bottomMiddle) # top row middle column
    drawGridSlot(centerGridX + 125, centerGridY + 125, bottomRightL, bottomRight) # top row right column
    
#    if moves == 9:
#        graphik.drawButton(displayWidth//2 - 50, displayHeight - 100, 100, 50, black, white, 20, "Quit", exit)
    
    pygame.display.update()

def restart():
    global topLeftL
    global topMiddleL
    global topRightL
    global middleLeftL
    global middleMiddleL
    global middleRightL
    global bottomLeftL
    global bottomMiddleL
    global bottomRightL
    global moves
    topLeftL = ""
    topMiddleL = ""
    topRightL = ""

    middleLeftL = ""
    middleMiddleL = ""
    middleRightL = ""

    bottomLeftL = ""
    bottomMiddleL = ""
    bottomRightL = ""
    
    moves = 0
    titleScreen()

def playerWin():
    time.sleep(1)
    print("Player Wins")

    while moves > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            graphik.drawText("You won!", displayWidth//2, displayHeight//4, 64, black)
            middleButtonXPos = displayWidth//2 - 50
            graphik.drawButton(middleButtonXPos, displayHeight - 200, 100, 50, black, white, 16, "Play Again", restart)
            graphik.drawButton(middleButtonXPos, displayHeight - 100, 100, 50, black, white, 16, "Quit", exit)

            pygame.display.update()
    
def computerWin():
    time.sleep(1)
    print("Computer Wins")

    while moves > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            graphik.drawText("You lost!", displayWidth//2, displayHeight//4, 64, black)
            middleButtonXPos = displayWidth//2 - 50
            graphik.drawButton(middleButtonXPos, displayHeight - 200, 100, 50, black, white, 20, "Play Again", restart)
            graphik.drawButton(middleButtonXPos, displayHeight - 100, 100, 50, black, white, 20, "Quit", exit)

            pygame.display.update()
            
def tie():
    time.sleep(1)
    print("It was a tie!")

    while moves > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            graphik.drawText("You lost!", displayWidth//2, displayHeight//4, 64, black)
            middleButtonXPos = displayWidth//2 - 50
            graphik.drawButton(middleButtonXPos, displayHeight - 200, 100, 50, black, white, 20, "Play Again", restart)
            graphik.drawButton(middleButtonXPos, displayHeight - 100, 100, 50, black, white, 20, "Quit", exit)

            pygame.display.update()

def checkForWinCondition():
    # case top row
    if topLeftL == "X" and topMiddleL == "X" and topRightL == "X":
        playerWin()
        
    if topLeftL == "O" and topMiddleL == "O" and topRightL == "O":
        computerWin()
    
    # case middle row
    if middleLeftL == "X" and middleMiddleL == "X" and middleRightL == "X":
        playerWin()
        
    if middleLeftL == "O" and middleMiddleL == "O" and middleRightL == "O":
        computerWin()
    
    # case bottom row
    if bottomLeftL == "X" and bottomMiddleL == "X" and bottomRightL == "X":
        playerWin()
        
    if bottomLeftL == "O" and bottomMiddleL == "O" and bottomRightL == "O":
        computerWin()
    
    # case left column
    if topLeftL == "X" and middleLeftL == "X" and bottomLeftL == "X":
        playerWin()
        
    if topLeftL == "O" and middleLeftL == "O" and bottomLeftL == "O":
        computerWin()
    
    # case middle column
    if topMiddleL == "X" and middleMiddleL == "X" and bottomMiddleL == "X":
        playerWin()
        
    if topMiddleL == "O" and middleMiddleL == "O" and bottomMiddleL == "O":
        computerWin()
    
    # case right column
    if topRightL == "X" and middleRightL == "X" and bottomRightL == "X":
        playerWin()
        
    if topRightL == "O" and middleRightL == "O" and bottomRightL == "O":
        computerWin()
    
    # case diagonal ->
    if topLeftL == "X" and middleMiddleL == "X" and bottomRightL == "X":
        playerWin()
        
    if topLeftL == "O" and middleMiddleL == "O" and bottomRightL == "O":
        computerWin()
        
    # case diagonal <-
    if topRightL == "X" and middleMiddleL == "X" and bottomLeftL == "X":
        playerWin()
        
    if topRightL == "O" and middleMiddleL == "O" and bottomLeftL == "O":
        computerWin()
        
    if moves == 9:
        tie()

def gridScreen():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            gameDisplay.fill(white)
            
            drawGrid()

def titleScreen():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            graphik.drawText("Tic Tac Toe", displayWidth//2, displayHeight//4, 64, black)
            middleButtonXPos = displayWidth//2 - 50
            graphik.drawButton(middleButtonXPos, displayHeight - 300, 100, 50, black, white, 20, "Start", gridScreen)
#            graphik.drawButton(middleButtonXPos, displayHeight - 200, 100, 50, black, white, 20, "Stats", test)
            graphik.drawButton(middleButtonXPos, displayHeight - 100, 100, 50, black, white, 20, "Quit", exit)

            pygame.display.update()

titleScreen()