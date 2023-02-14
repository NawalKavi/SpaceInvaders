# Importing library and initialising.
from pygame import *
init()

# Setting up the screen.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))

# Images.
imageDictionary = {
"invader1": transform.scale(image.load("Images//Invader 1.png"), (40, 40)),
"invader2": transform.scale(image.load("Images//Invader 2.png"), (40, 40)),
"invader3": transform.scale(image.load("Images//Invader 3.png"), (40, 40))
}

# Invader class.
class Invader(Rect):
    # Generates an invader.
    def __init__(self, x, y, invaderType):
        super().__init__(x, y, 40, 40)
        self.invaderImage = imageDictionary[invaderType]
    # Position of the invader.
    def centreImage(numOfInvader, gapInvader):
        subtractThis = numOfInvader * gapInvader
        halfThis = subtractThis - width
        firstInvaderX = halfThis / 2
    # Blits the image and draws it.
    def draw(self, screen):
        screen.blit(self.invaderImage, (self.x, self.y))

# 1D array for aliens.
invaderArr = []

# Loop for appending aliens into the 1D array.
x = 200
while x < 900:
    # Creates an invader using the class.
    generateInvader = Invader(x, 20, "invader3")
    invaderArr.append(generateInvader)
    x = x + 40

# Game loop.
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits the game by closing the window.
        if gameEvent.type == QUIT:
            gameRunning = False
    # Fills the window with the specified colour (black).
    mainWindow.fill((0, 0, 0))
    # Draws the current invader from the 1D array.
    for currentInvader in invaderArr:
        currentInvader.draw(mainWindow)
    # Displays the output.
    display.flip()