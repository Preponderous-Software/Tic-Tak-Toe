import pygame

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)

graphiklibversion = "0.2-alpha-1"

#  @author Daniel McCoy Stephenson
#  @since February 3rd, 2022
class Graphik:
    def __init__(self):
        displayWidth = 900
        displayHeight = 600
        self.gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

        self.version = graphiklibversion

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

        self.version = graphiklibversion

    def getVersion(self):
        return self.version

    def drawRectangle(self, xpos, ypos, width, height, color):
        pygame.draw.rect(self.gameDisplay, color, [xpos, ypos, width, height])

    def drawText(self, text, xpos, ypos, size, color):
        myFont = pygame.font.Font('freesansbold.ttf', size)
        textSurface = myFont.render(text, True, color)
        textRectangle = textSurface.get_rect()
        textRectangle.center = ((xpos, ypos))
        self.gameDisplay.blit(textSurface, textRectangle)

    def drawButton(self, xpos, ypos, width, height, colorBox, colorText, sizeText, text, function):
        self.drawRectangle(xpos, ypos, width, height, colorBox)
        self.drawText(text, xpos + (width//2), ypos + (height//2), sizeText, colorText)
        
        # if clicked then do function
        mouse = pygame.mouse.get_pos()
        if (xpos + width > mouse[0] > xpos and ypos + height > mouse[1] > ypos):
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                function()