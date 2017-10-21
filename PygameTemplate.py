import pygame as pg

pg.init()

gameDisplay = pg.display.set_mode((800,600)) #Set screen size here

pg.display.set_caption('Title goes here') #Insert title here

pg.display.update() #update the window here

gameExit = False #game state

#game loop
while not gameExit:
    #for testing events fired in pygame
    for event in pg.event.get(): 
        print(event)

#End the game and all else
pg.quit()
quit()
