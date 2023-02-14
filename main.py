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
"invader3": transform.scale(image.load("Images//Invader 3.png"), (40, 40)),
"player": transform.scale(image.load("Images//Player.png"), (40, 40))
}

# Game loop.
oneSecondTick = 0
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits the game by closing the window.
        if gameEvent.type == QUIT:
            gameRunning = False

    # Fills the window with the specified colour (black).
    mainWindow.fill((0, 0, 0))

    # Runs game at 120fps.
    time.Clock().tick(120)

    # Displays the output.
    display.flip()