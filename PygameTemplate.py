import pygame as pg
from Physics import Physics

physics = Physics()

pg.init()

#fps
fps = 60
clock = pg.time.Clock()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

y = 20
x = 20

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

   
    
    #This needs to be fixed!!!!!
    if y < 500:
        yAcceleration = physics.getMotionY()
        y += 0-(yAcceleration/fps) #This will represent 1px as 1m,
                                      # dividing by fps gives 1s
      
    
    
    #making a rectangle/image/whatever
    pg.draw.rect(gameDisplay, red, [400,y,20,20])
    pg.display.update()#update the display, goes last, always

    clock.tick(fps)

#End the game and all else
pg.quit()
quit()
