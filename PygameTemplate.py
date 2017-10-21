import pygame as pg

pg.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pg.display.set_mode((800,600)) #Set screen size here

pg.display.set_caption('Title goes here') #Insert title here

pg.display.update() #update the window here

gameExit = False #game state

#game loop
while not gameExit:
    #for testing events fired in pygame
    for event in pg.event.get(): 
        #print(event)#for debugging events
        if event.type == pg.QUIT:
            gameExit = True

    #Set the background color
    gameDisplay.fill(white)
    #making a rectangle/image/whatever
    pg.draw.rect(gameDisplay, red, [400,300,20,20])
    pg.display.update()#update the display, goes last, always

#End the game and all else
pg.quit()
quit()
