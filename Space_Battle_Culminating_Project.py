#-------------------------------------------------------------------------------#
# Name:        Space Battle Videogame                                           #
#                                                                               #
# Author:      Lazar                                                            #
#                                                                               #
# Due:     15/06/2018                                                           #
#-------------------------------------------------------------------------------#

#------------------------------------------- Initialization Process --------------------------------------------------------------

import pygame, time , random

pygame.init()#initialize libraries

#Screen is set with dimensions of 900 by 700
#Caption is set as Space Battle
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption("Space Battle")

#BLACK is defined to be the colour black so it can be used to clear screens with screen.fill
BLACK = (0,0,0)

#------------------------------------------- Functions --------------------------------------------------------------#

"""This function determines the lives amount after a collision occurs"""
def determineLives(lifeamount):

    #life amount is subtracted by 1, followed by a small delay and display update
    lifeamount = lifeamount - 1

    time.sleep (1)

    pygame.display.update()

    #returned so the lives amount in the main program can be updated
    return lifeamount

"""This function goes through the "Game Over" process when the user loses and runs out of lives"""
def gameOver():

    #Screen background is set to black with white text saying "GAME OVER"
    screen.fill(BLACK)
    font = pygame.font.Font(None,50)
    text1 = font.render("GAME OVER ",True,(255,255,255))
    screen.blit(text1, (330,340))

    pygame.display.update()#updates the screen

    #Game over screen lasts for 3 seconds
    time.sleep(3)

"""This function goes through the "Winning" process after the user beats the boss and reaches the end of the game"""
def gameWin():

    #Screen background is set to black with white text saying 'YOU HAVE BEATEN THE GAME"
    screen.fill(BLACK)
    font = pygame.font.Font(None,50)
    text1 = font.render("YOU HAVE BEATEN THE GAME!",True,(255,255,255))
    screen.blit(text1, (150,340))

    pygame.display.update()#updates the screen

    #Winning screen lasts for 3 seconds
    time.sleep(3)

#------------------------------------------- Coordinate Variable Declaration --------------------------------------------------------------

#All the coordinates of the sprites in the game are defined
xrocket = 430
yrocket = 600

xboss= 350
yboss = 50

xminiufo1 = 270
yminiufo1 = 0

xminiufo2 = 375
yminiufo2 = 0

xminiufo3 = 540
yminiufo3 = 0

xminiufo4 = 270
yminiufo4 = 0

xminiufo5 = 375
yminiufo5 = 0

xminiufo6 = 540
yminiufo6 = 0

xsun = 0
ysun = 350

xsun2 = 0
ysun2 = 100

xsun3 = 50
ysun3 = 10

xsun4 = 50
ysun4 = 450

xsun5 = 600
ysun5 = 10

xsun6 = 600
ysun6 = 450

xasteroid = 230
yasteroid = 290

xasteroid2 = 570
yasteroid2 = 290

xasteroid3 = 55
yasteroid3 = 230

xasteroid4 = 605
yasteroid4 = 230

xasteroid5 = 250
yasteroid5 = 140

xasteroid6 = 525
yasteroid6 = 140

xcomet1 = -200
ycomet1 = 175

xcomet2 = -200
ycomet2 = 450

xcomet3 = 340
ycomet3 = 0

xcomet4 = 0
ycomet4 = 150

xcomet5 = 0
ycomet5 = 300

xcomet6 = 0
ycomet6 = 450

xlaser = 50
ylaser = 150

#------------------------------------------- Declaration of Movement Variables --------------------------------------------------------------

#All the movement variables that are used to move sprites are defined
moverocketx=0
moverockety=0
moveufo=0
movesun1x = 3
movesun2x = 3
movecomet1x = 15
movecomet2x = 15
movecomet3y = 15
moveminiufo = 20
movecomet_456 = 17
moveboss = 7

#------------------------------------------- Declaration of Other Variables --------------------------------------------------------------

#Other critical variables besides coordinates and movement are defined
lives = 3
levelcomplete = 0
mini_ufos_position = 1
comets_position = 1
bossHP = 1000

#n is a variable that is used to determine whether the condition for the main menu while loop is true or false
n = True

#------------------------------------------- Image Declaration --------------------------------------------------------------

#Every single sprite in the whole game and their rectangular boundaries are defined
rocket = pygame.sprite.Sprite()
rocket.image = pygame.image.load("rocket_up.png")
rocket.rect = rocket.image.get_rect()#set the sprite's rectangular boundaries

background = pygame.sprite.Sprite()
background.image = pygame.image.load("background.png")
background.rect = background.image.get_rect()#set the sprite's rectangular boundaries

comet1 = pygame.sprite.Sprite()
comet1.image = pygame.image.load("comet1.png")
comet1.rect = comet1.image.get_rect()#set the sprite's rectangular boundaries

comet2 = pygame.sprite.Sprite()
comet2.image = pygame.image.load("comet1.png")
comet2.rect = comet2.image.get_rect()#set the sprite's rectangular boundaries

comet3 = pygame.sprite.Sprite()
comet3.image = pygame.image.load("comet2.png")
comet3.rect = comet3.image.get_rect()#set the sprite's rectangular boundaries

comet4 = pygame.sprite.Sprite()
comet4.image = pygame.image.load("comet1.png")
comet4.rect = comet4.image.get_rect()#set the sprite's rectangular boundaries

comet5 = pygame.sprite.Sprite()
comet5.image = pygame.image.load("comet1.png")
comet5.rect = comet5.image.get_rect()#set the sprite's rectangular boundaries

comet6 = pygame.sprite.Sprite()
comet6.image = pygame.image.load("comet1.png")
comet6.rect = comet6.image.get_rect()#set the sprite's rectangular boundaries

sun = pygame.sprite.Sprite()
sun.image = pygame.image.load("sun.png")
sun.rect = sun.image.get_rect()#set the sprite's rectangular boundaries

sun2 = pygame.sprite.Sprite()
sun2.image = pygame.image.load("sun.png")
sun2.rect = sun2.image.get_rect()#set the sprite's rectangular boundaries

sun3 = pygame.sprite.Sprite()
sun3.image = pygame.image.load("sun.png")
sun3.rect = sun3.image.get_rect()#set the sprite's rectangular boundaries

sun4 = pygame.sprite.Sprite()
sun4.image = pygame.image.load("sun.png")
sun4.rect = sun4.image.get_rect()#set the sprite's rectangular boundaries

sun5 = pygame.sprite.Sprite()
sun5.image = pygame.image.load("sun.png")
sun5.rect = sun5.image.get_rect()#set the sprite's rectangular boundaries

sun6 = pygame.sprite.Sprite()
sun6.image = pygame.image.load("sun.png")
sun6.rect = sun6.image.get_rect()#set the sprite's rectangular boundaries

sun7 = pygame.sprite.Sprite()
sun7.image = pygame.image.load("sun.png")
sun7.rect = sun7.image.get_rect()#set the sprite's rectangular boundaries

sun8 = pygame.sprite.Sprite()
sun8.image = pygame.image.load("sun.png")
sun8.rect = sun8.image.get_rect()#set the sprite's rectangular boundaries

jupiter = pygame.sprite.Sprite()
jupiter.image = pygame.image.load("jupiter.png")
jupiter.rect = jupiter.image.get_rect()#set the sprite's rectangular boundaries

jupiter2 = pygame.sprite.Sprite()
jupiter2.image = pygame.image.load("jupiter.png")
jupiter2.rect = jupiter2.image.get_rect()#set the sprite's rectangular boundaries

jupiter3 = pygame.sprite.Sprite()
jupiter3.image = pygame.image.load("jupiter.png")
jupiter3.rect = jupiter3.image.get_rect()#set the sprite's rectangular boundaries

asteroid = pygame.sprite.Sprite()
asteroid.image = pygame.image.load("asteroid.png")
asteroid.rect = asteroid.image.get_rect()#set the sprite's rectangular boundaries

asteroid2 = pygame.sprite.Sprite()
asteroid2.image = pygame.image.load("asteroid.png")
asteroid2.rect = asteroid2.image.get_rect()#set the sprite's rectangular boundaries

asteroid3 = pygame.sprite.Sprite()
asteroid3.image = pygame.image.load("asteroidbig.png")
asteroid3.rect = asteroid3.image.get_rect()#set the sprite's rectangular boundaries

asteroid4 = pygame.sprite.Sprite()
asteroid4.image = pygame.image.load("asteroidbig.png")
asteroid4.rect = asteroid4.image.get_rect()#set the sprite's rectangular boundaries

asteroid5 = pygame.sprite.Sprite()
asteroid5.image = pygame.image.load("asteroid.png")
asteroid5.rect = asteroid5.image.get_rect()#set the sprite's rectangular boundaries

asteroid6 = pygame.sprite.Sprite()
asteroid6.image = pygame.image.load("asteroid.png")
asteroid6.rect = asteroid6.image.get_rect()#set the sprite's rectangular boundaries

miniufo1 = pygame.sprite.Sprite()
miniufo1.image = pygame.image.load("miniufo.png")
miniufo1.rect = miniufo1.image.get_rect()#set the sprite's rectangular boundaries

miniufo2 = pygame.sprite.Sprite()
miniufo2.image = pygame.image.load("miniufo.png")
miniufo2.rect = miniufo2.image.get_rect()#set the sprite's rectangular boundaries

miniufo3 = pygame.sprite.Sprite()
miniufo3.image = pygame.image.load("miniufo.png")
miniufo3.rect = miniufo3.image.get_rect()#set the sprite's rectangular boundaries

miniufo4 = pygame.sprite.Sprite()
miniufo4.image = pygame.image.load("miniufo.png")
miniufo4.rect = miniufo4.image.get_rect()#set the sprite's rectangular boundaries

miniufo5 = pygame.sprite.Sprite()
miniufo5.image = pygame.image.load("miniufo.png")
miniufo5.rect = miniufo5.image.get_rect()#set the sprite's rectangular boundaries

miniufo6 = pygame.sprite.Sprite()
miniufo6.image = pygame.image.load("miniufo.png")
miniufo6.rect = miniufo6.image.get_rect()#set the sprite's rectangular boundaries

laser = pygame.sprite.Sprite()
laser.image = pygame.image.load("laser.png")
laser.rect = laser.image.get_rect()#set the sprite's rectangular boundaries

boss = pygame.sprite.Sprite()
boss.image = pygame.image.load("ufo.png")
boss.rect = boss.image.get_rect()#set the sprite's rectangular boundaries

menu = pygame.sprite.Sprite()
menu.image = pygame.image.load("menu.png")

#-------------------------------------------------- Main Program Loop ------------------------------------------------------------------------

while(True):

    #--------------------------------------------- Main Menu Loop ---------------------------------------------------------------------------
    #While the user is in the beginning stage of the game, clear everything (if there are any images left from previoud attempts to play) and display the menu image
    while n == True:
        screen.fill(BLACK)
        screen.blit(menu.image, (0,0))

        #---------------------------------- Coordinate Variable Declaration for 2nd+ time playing Game -------------------------------------

        #All the coordinate variables are defined again (if the user plays a 2nd or more time) so each sprite starts in the same spot and not in the spot where the user last left off
        xrocket = 430
        yrocket = 600

        xboss= 350
        yboss = 50

        xminiufo1 = 270
        yminiufo1 = 0

        xminiufo2 = 375
        yminiufo2 = 0

        xminiufo3 = 540
        yminiufo3 = 0

        xminiufo4 = 270
        yminiufo4 = 0

        xminiufo5 = 375
        yminiufo5 = 0

        xminiufo6 = 540
        yminiufo6 = 0

        xsun = 0
        ysun = 350

        xsun2 = 0
        ysun2 = 100

        xsun3 = 50
        ysun3 = 10

        xsun4 = 50
        ysun4 = 450

        xsun5 = 600
        ysun5 = 10

        xsun6 = 600
        ysun6 = 450

        xasteroid = 230
        yasteroid = 290

        xasteroid2 = 570
        yasteroid2 = 290

        xasteroid3 = 55
        yasteroid3 = 230

        xasteroid4 = 605
        yasteroid4 = 230

        xasteroid5 = 250
        yasteroid5 = 140

        xasteroid6 = 525
        yasteroid6 = 140

        xcomet1 = -200
        ycomet1 = 175

        xcomet2 = -200
        ycomet2 = 450

        xcomet3 = 340
        ycomet3 = 0

        xcomet4 = 0
        ycomet4 = 150

        xcomet5 = 0
        ycomet5 = 300

        xcomet6 = 0
        ycomet6 = 450

        xlaser = 50
        ylaser = 150

        #------------------------------------------- Declaration of Movement Variables for 2nd+ time playing Game --------------------------------------------------------------

        #All the movement variables are defined again (if the user plays a 2nd or more time) so any previous movement values are set back to default
        moverocketx=0
        moverockety=0
        moveufo=0
        movesun1x = 3
        movesun2x = 3
        movecomet1x = 15
        movecomet2x = 15
        movecomet3y = 15
        moveminiufo = 20
        movecomet_456 = 17
        moveboss = 7

        #------------------------------------------- Declaration of Other Variables for 2nd+ time playing Game --------------------------------------------------------------

        #All the critical non coordinate variables are defined again (if the user plays a 2nd or more time) so all sprite layouts, amount of lives, and the bosses HP are set back to default
        lives = 3
        levelcomplete = 0
        mini_ufos_position = 1
        comets_position = 1
        bossHP = 1000

        #n is a variable that is used to determine whether the condition for the main menu while loop is true or false, it is set to one again so the main menu loops forever until the user plays
        n = True

        #------------------------------------------- Image Declaration for 2nd+ time playing Game ----------------------------------------------------------------------------

        #All the sprite declarations are defined again (if the user plays a 2nd or more time) to avoid collision errors if the user plays a second or more time
        rocket = pygame.sprite.Sprite()
        rocket.image = pygame.image.load("rocket_up.png")
        rocket.rect = rocket.image.get_rect()#set the sprite's rectangular boundaries

        background = pygame.sprite.Sprite()
        background.image = pygame.image.load("background.png")
        background.rect = background.image.get_rect()#set the sprite's rectangular boundaries

        comet1 = pygame.sprite.Sprite()
        comet1.image = pygame.image.load("comet1.png")
        comet1.rect = comet1.image.get_rect()#set the sprite's rectangular boundaries

        comet2 = pygame.sprite.Sprite()
        comet2.image = pygame.image.load("comet1.png")
        comet2.rect = comet2.image.get_rect()#set the sprite's rectangular boundaries

        comet3 = pygame.sprite.Sprite()
        comet3.image = pygame.image.load("comet2.png")
        comet3.rect = comet3.image.get_rect()#set the sprite's rectangular boundaries

        comet4 = pygame.sprite.Sprite()
        comet4.image = pygame.image.load("comet1.png")
        comet4.rect = comet4.image.get_rect()#set the sprite's rectangular boundaries

        comet5 = pygame.sprite.Sprite()
        comet5.image = pygame.image.load("comet1.png")
        comet5.rect = comet5.image.get_rect()#set the sprite's rectangular boundaries

        comet6 = pygame.sprite.Sprite()
        comet6.image = pygame.image.load("comet1.png")
        comet6.rect = comet6.image.get_rect()#set the sprite's rectangular boundaries

        sun = pygame.sprite.Sprite()
        sun.image = pygame.image.load("sun.png")
        sun.rect = sun.image.get_rect()#set the sprite's rectangular boundaries

        sun2 = pygame.sprite.Sprite()
        sun2.image = pygame.image.load("sun.png")
        sun2.rect = sun2.image.get_rect()#set the sprite's rectangular boundaries

        sun3 = pygame.sprite.Sprite()
        sun3.image = pygame.image.load("sun.png")
        sun3.rect = sun3.image.get_rect()#set the sprite's rectangular boundaries

        sun4 = pygame.sprite.Sprite()
        sun4.image = pygame.image.load("sun.png")
        sun4.rect = sun4.image.get_rect()#set the sprite's rectangular boundaries

        sun5 = pygame.sprite.Sprite()
        sun5.image = pygame.image.load("sun.png")
        sun5.rect = sun5.image.get_rect()#set the sprite's rectangular boundaries

        sun6 = pygame.sprite.Sprite()
        sun6.image = pygame.image.load("sun.png")
        sun6.rect = sun6.image.get_rect()#set the sprite's rectangular boundaries

        sun7 = pygame.sprite.Sprite()
        sun7.image = pygame.image.load("sun.png")
        sun7.rect = sun7.image.get_rect()#set the sprite's rectangular boundaries

        sun8 = pygame.sprite.Sprite()
        sun8.image = pygame.image.load("sun.png")
        sun8.rect = sun8.image.get_rect()#set the sprite's rectangular boundaries

        jupiter = pygame.sprite.Sprite()
        jupiter.image = pygame.image.load("jupiter.png")
        jupiter.rect = jupiter.image.get_rect()#set the sprite's rectangular boundaries

        jupiter2 = pygame.sprite.Sprite()
        jupiter2.image = pygame.image.load("jupiter.png")
        jupiter2.rect = jupiter2.image.get_rect()#set the sprite's rectangular boundaries

        jupiter3 = pygame.sprite.Sprite()
        jupiter3.image = pygame.image.load("jupiter.png")
        jupiter3.rect = jupiter3.image.get_rect()#set the sprite's rectangular boundaries

        asteroid = pygame.sprite.Sprite()
        asteroid.image = pygame.image.load("asteroid.png")
        asteroid.rect = asteroid.image.get_rect()#set the sprite's rectangular boundaries

        asteroid2 = pygame.sprite.Sprite()
        asteroid2.image = pygame.image.load("asteroid.png")
        asteroid2.rect = asteroid2.image.get_rect()#set the sprite's rectangular boundaries

        asteroid3 = pygame.sprite.Sprite()
        asteroid3.image = pygame.image.load("asteroidbig.png")
        asteroid3.rect = asteroid3.image.get_rect()#set the sprite's rectangular boundaries

        asteroid4 = pygame.sprite.Sprite()
        asteroid4.image = pygame.image.load("asteroidbig.png")
        asteroid4.rect = asteroid4.image.get_rect()#set the sprite's rectangular boundaries

        asteroid5 = pygame.sprite.Sprite()
        asteroid5.image = pygame.image.load("asteroid.png")
        asteroid5.rect = asteroid5.image.get_rect()#set the sprite's rectangular boundaries

        asteroid6 = pygame.sprite.Sprite()
        asteroid6.image = pygame.image.load("asteroid.png")
        asteroid6.rect = asteroid6.image.get_rect()#set the sprite's rectangular boundaries

        miniufo1 = pygame.sprite.Sprite()
        miniufo1.image = pygame.image.load("miniufo.png")
        miniufo1.rect = miniufo1.image.get_rect()#set the sprite's rectangular boundaries

        miniufo2 = pygame.sprite.Sprite()
        miniufo2.image = pygame.image.load("miniufo.png")
        miniufo2.rect = miniufo2.image.get_rect()#set the sprite's rectangular boundaries

        miniufo3 = pygame.sprite.Sprite()
        miniufo3.image = pygame.image.load("miniufo.png")
        miniufo3.rect = miniufo3.image.get_rect()#set the sprite's rectangular boundaries

        miniufo4 = pygame.sprite.Sprite()
        miniufo4.image = pygame.image.load("miniufo.png")
        miniufo4.rect = miniufo4.image.get_rect()#set the sprite's rectangular boundaries

        miniufo5 = pygame.sprite.Sprite()
        miniufo5.image = pygame.image.load("miniufo.png")
        miniufo5.rect = miniufo5.image.get_rect()#set the sprite's rectangular boundaries

        miniufo6 = pygame.sprite.Sprite()
        miniufo6.image = pygame.image.load("miniufo.png")
        miniufo6.rect = miniufo6.image.get_rect()#set the sprite's rectangular boundaries

        laser = pygame.sprite.Sprite()
        laser.image = pygame.image.load("laser.png")
        laser.rect = laser.image.get_rect()#set the sprite's rectangular boundaries

        boss = pygame.sprite.Sprite()
        boss.image = pygame.image.load("ufo.png")
        boss.rect = boss.image.get_rect()#set the sprite's rectangular boundaries

        menu = pygame.sprite.Sprite()
        menu.image = pygame.image.load("menu.png")


        #Screen is updated
        pygame.display.update()

        #Event for keys is defined
        event=pygame.event.poll()

        #If the user presses some key
        if (event.type==pygame.KEYDOWN):

            #End the program if the user presses the "END" key
            if (event.key==pygame.K_ESCAPE):
                pygame.quit()
                quit()

            #If the user presses "P", the n variable is set to false so the main menu loop ends and the program proceeds to the levels
            elif (event.key==pygame.K_p):
                n = False

    #------------------------------------------- Easy Level Loop --------------------------------------------------------------

    while(True):

        #All the images in the Easy Level are displayed
        #The screen is cleared of any image before the images are displayed onto the screen
        screen.fill(BLACK)
        rocket.rect.topleft=(xrocket,yrocket)

        screen.blit(background.image, (0,0))
        screen.blit(rocket.image, rocket.rect)

        sun.rect.topleft=(xsun,ysun)
        screen.blit(sun.image, sun.rect)
        sun2.rect.topleft=(xsun2,ysun2)
        screen.blit(sun2.image, sun2.rect)

        #The movement variables are added to their corresponding coordinate variables to allow movement in the level
        xrocket = xrocket + moverocketx
        yrocket = yrocket + moverockety
        xsun = xsun + movesun1x
        xsun2 = xsun2 + movesun2x

        #If the user tries to fly off at the bottom of the screen, move them up
        if yrocket > 650:
            yrocket = yrocket - 10

        #If the user tries to fly off screen on the left, move them right
        if xrocket < 0:
            xrocket = xrocket + 10

        #If the user tries to fly off screen on the right, move them left
        if xrocket > 850:
            xrocket = xrocket - 10

        #If the sun gets close to moving off the screen on the left, start moving it to the right
        if xsun < 0:
            movesun1x = 3

        #If the sun gets close to moving off the screen on the right, start moving it to the left
        if xsun > 650:
            movesun1x = -3

        #If the sun2 gets close to moving off the screen on the left, start moving it to the right
        if xsun2 < 0:
            movesun2x = 3

        #If the sun2 gets close to moving off the screen on the right, start moving it to the left
        if xsun2 > 650:
            movesun2x = -3

        #If the user reaches the very top of the screen, set the levelcomplete variable to 1 to signify that the user completed the level and break out of the Easy Level Loop
        if yrocket == 0:
            levelcomplete = 1
            break

        #If the rocket collides with sun1, subtract one life and set the coordinates of the rocket to the starting position
        if (pygame.sprite.collide_rect(rocket,sun)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, intiate the "Game Over" procedure outlined in the doc string of "gameOver()" and break out of the Easy Level Loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun2, subtract one life and set the coordinates of the rocket to the starting position
        if (pygame.sprite.collide_rect(rocket,sun2)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, intiate the "Game Over" procedure outlined in the doc string of "gameOver()" and break out of the Easy Level Loop
            if lives == 0:
                gameOver()
                break

        #The coordinates of the rocket are put into a list so they can be displayed together on the screen
        coordinates = [xrocket, yrocket]

        #All the useful information at the top of the screen (lives, level name, coordinates) are displayed onto the screen
        font = pygame.font.Font(None,30)
        text1 = font.render("Player Coordinates: " ,True,(255,0,0))
        screen.blit(text1, (520,10))

        font = pygame.font.Font(None,30)
        text1 = font.render(str(coordinates) ,True,(255,255,255))
        screen.blit(text1, (730,10))

        font = pygame.font.Font(None,30)
        text1 = font.render("Easy Level" ,True,(255,255,255))
        screen.blit(text1, (5,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("Lives: " + str(lives) ,True,(255,255,255))
        screen.blit(text1, (200,5))


        #Event for keys is defined
        event=pygame.event.poll()

        #If the user presses the quit button, break out of the Easy Level Loop
        if (event.type==pygame.QUIT):
            break

        #If the user presses a key down
        elif (event.type==pygame.KEYDOWN):#KEYDOWN means a key is pressed

            #Move the rocket right if the user presses down the "D" key
            if (event.key==pygame.K_d):
                moverocketx=5
                moverockety=0

            #Move the rocket left if the user presses down the "A" key
            elif (event.key==pygame.K_a):
                moverocketx=-5
                moverockety=0

            #Move the rocket up if the user presses down the "W" key
            elif (event.key==pygame.K_w):
                moverockety=-5
                moverocketx=0

            #Move the rocket down if the user presses down the "S" key
            elif (event.key==pygame.K_s):
                moverockety=5
                moverocketx=0

            #If the user presses the end key, break out of the Easy Level Loop
            elif (event.key==pygame.K_END):
                break

            #If the user presses the "Q" key, define the level as being complete and break out of the Easy Level Loop (used to skip levels as a cheat)
            elif (event.key==pygame.K_q):
                levelcomplete = 1
                break

        #If the user doesn't press any keys, keep the rocket stationary
        elif (event.type==pygame.KEYUP):
            moverocketx = 0
            moverockety = 0

        #The screen is update after all changes to sprite positions occur
        pygame.display.update()

    #If the level is defined to be incomplete, set the value of n to True to restart the game by using the continue command to restart the menu while statement
    if levelcomplete == 0:
        n = True
        continue

    #One second delay
    time.sleep(1)

    #The rocket coordinates are set back to the starting position
    xrocket = 430
    yrocket = 600

    #------------------------------------------- Medium Level Loop --------------------------------------------------------------

    while(True):

        #All the images in the Medium Level are displayed
        #The screen is cleared of any image before the images are displayed onto the screen
        screen.fill(BLACK)

        rocket.rect.topleft=(xrocket,yrocket)

        screen.blit(background.image, (0,0))
        screen.blit(rocket.image, rocket.rect)

        jupiter.rect.topleft=(350,250)
        screen.blit(jupiter.image, jupiter.rect)

        jupiter2.rect.topleft=(0,250)
        screen.blit(jupiter2.image, jupiter2.rect)

        jupiter3.rect.topleft=(700,250)
        screen.blit(jupiter3.image, jupiter3.rect)

        asteroid.rect.topleft=(xasteroid,yasteroid)
        screen.blit(asteroid.image, asteroid.rect)

        asteroid2.rect.topleft=(xasteroid2,yasteroid2)
        screen.blit(asteroid2.image, asteroid2.rect)

        comet2.rect.topleft=(xcomet2,ycomet2)
        screen.blit(comet2.image, comet2.rect)

        comet1.rect.topleft=(xcomet1,ycomet1)
        screen.blit(comet1.image, comet1.rect)

        laser.rect.topleft=(xlaser,ylaser)
        screen.blit(laser.image, laser.rect)

        #The movement variables are added to their corresponding coordinate variables to allow movement in the level
        xrocket = xrocket + moverocketx
        yrocket = yrocket + moverockety
        xcomet1 = xcomet1 + movecomet1x
        xcomet2 = xcomet2 + movecomet2x


        #If the user tries to fly off at the bottom of the screen, move them up
        if yrocket > 650:
            yrocket = yrocket - 10

        #If the user tries to fly off screen on the left, move them right
        if xrocket < 0:
            xrocket = xrocket + 10

        #If the user tries to fly off screen on the right, move them left
        if xrocket > 850:
            xrocket = xrocket - 10

        #If the user gets close to the top of the screen, signify the second level as complete and break out of the medium level loop
        if yrocket == 0:
            levelcomplete = 2
            break

        #If comet1 disappears a little more then the edge of the right screen, move it back off the edge of the left side of the screen
        if xcomet1 > 1100:
            xcomet1 = -200

        #If comet2 disappears a little more then the edge of the right screen, move it back off the edge of the left side of the screen
        if xcomet2 > 1100:
            xcomet2 = -200

        #If both of the asteroids "disappear"(move very far off screen), then have the laser "dissapear" (move very far off screen)
        if xasteroid == -1000 and yasteroid == -1000 and xasteroid2 == -1000 and yasteroid2 == -1000:
            xlaser = -1000
            ylaser = -1000

        #If the rocket and jupiter1 collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,jupiter)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket and jupiter2 collide, move the rocket down a little bit and have asteroid1 "dissapear" (move very far off screen)
        if (pygame.sprite.collide_rect(rocket,jupiter2)):

            yrocket = yrocket + 10
            xasteroid = -1000
            yasteroid = -1000

        #If the rocket and jupiter3 collide, move the rocket down a little bit and have asteroid2 "dissapear" (move very far off screen)
        if (pygame.sprite.collide_rect(rocket,jupiter3)):

            yrocket = yrocket + 10
            xasteroid2 = -1000
            yasteroid2 = -1000

        #If the rocket and asteroid1 collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket and asteroid2 collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid2)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket and comet1 collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,comet1)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket and comet2 collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,comet2)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket and laser collide, subtract one life and set the rocket's coordinates to starting position
        if (pygame.sprite.collide_rect(rocket,laser)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #The coordinates of the rocket are put into a list so they can be displayed together on the screen
        coordinates = [xrocket, yrocket]

        #All the useful information (amount of lives, level name, coordinates) is displayed at the top of the screen
        font = pygame.font.Font(None,30)
        text1 = font.render("Player Coordinates: " ,True,(255,0,0))
        screen.blit(text1, (520,10))

        font = pygame.font.Font(None,30)
        text1 = font.render(str(coordinates) ,True,(255,255,255))
        screen.blit(text1, (730,10))

        font = pygame.font.Font(None,30)
        text1 = font.render("Medium Level" ,True,(255,255,255))
        screen.blit(text1, (5,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("Lives: " + str(lives) ,True,(255,255,255))
        screen.blit(text1, (200,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("HIT ME!",True,(0,0,0))
        screen.blit(text1, (35,330))

        font = pygame.font.Font(None,30)
        text1 = font.render("HIT ME!",True,(0,0,0))
        screen.blit(text1, (750,300))

        #The event for the keys is defined
        event=pygame.event.poll()

        #If the user presses the quit button, break out of the Easy Level Loop
        if (event.type==pygame.QUIT):
            break

        #If the user presses a key down
        elif (event.type==pygame.KEYDOWN):#KEYDOWN means a key is pressed

            #Move the rocket right if the user presses down the "D" key
            if (event.key==pygame.K_d):
                moverocketx=5
                moverockety=0

            #Move the rocket left if the user presses down the "A" key
            elif (event.key==pygame.K_a):
                moverocketx=-5
                moverockety=0

            #Move the rocket up if the user presses down the "W" key
            elif (event.key==pygame.K_w):
                moverockety=-5
                moverocketx=0

            #Move the rocket down if the user presses down the "S" key
            elif (event.key==pygame.K_s):
                moverockety=5
                moverocketx=0

            #If the user presses the end key, break out of the Medium Level Loop
            elif (event.key==pygame.K_END):
                break

            #If the user presses the "Q" key, define the level as being complete and break out of the Medium Level Loop (used to skip levels as a cheat)
            elif (event.key==pygame.K_q):
                levelcomplete = 2
                break

        #If the user doesn't press any keys, keep the rocket stationary
        elif (event.type==pygame.KEYUP):
            moverocketx = 0
            moverockety = 0

        #The screen is updated to display all the changes of all sprite positions
        pygame.display.update()

    #If the level is defined to be incomplete, set the value of n to True to restart the game by using the continue command to restart the menu while statement
    if levelcomplete == 1:
        n = True
        continue

    #One second delay
    time.sleep(1)

    #The rocket coordinates are set back to the starting position
    xrocket = 430
    yrocket = 600

    #------------------------------------------- Hard Level Loop --------------------------------------------------------------

    while(True):

        #All the images in the Hard Level are displayed
        #The screen is cleared of any image before the images are displayed onto the screen
        screen.fill(BLACK)

        rocket.rect.topleft=(xrocket,yrocket)

        screen.blit(background.image, (0,0))
        screen.blit(rocket.image, rocket.rect)

        sun3.rect.topleft=(xsun3,ysun3)
        screen.blit(sun3.image, sun3.rect)

        sun4.rect.topleft=(xsun4,ysun4)
        screen.blit(sun4.image, sun4.rect)

        sun5.rect.topleft=(xsun5,ysun5)
        screen.blit(sun5.image, sun5.rect)

        sun6.rect.topleft=(xsun6,ysun6)
        screen.blit(sun6.image, sun6.rect)

        asteroid3.rect.topleft=(xasteroid3,yasteroid3)
        screen.blit(asteroid3.image, asteroid3.rect)

        asteroid4.rect.topleft=(xasteroid4,yasteroid4)
        screen.blit(asteroid4.image, asteroid4.rect)

        comet3.rect.topleft=(xcomet3,ycomet3)
        screen.blit(comet3.image, comet3.rect)

        #The movement variables are added to their corresponding coordinate variables to allow movement in the level
        xrocket = xrocket + moverocketx
        yrocket = yrocket + moverockety
        ycomet3 = ycomet3 + movecomet3y

        #If the user tries to fly off at the bottom of the screen, move them up
        if yrocket > 650:
            yrocket = yrocket - 10

        #If the user tries to fly off screen on the left, move them right
        if xrocket < 0:
            xrocket = xrocket + 10

        #If the user tries to fly off screen on the right, move them left
        if xrocket > 850:
            xrocket = xrocket - 10

        #If the user gets close to the top of the screen, signify the third level as complete and break out of the hard level loop
        if yrocket == 0:
            levelcomplete = 3
            break

        #If the position value is 1, only display miniufo1 and miniufo3 and have them move down the screen
        if mini_ufos_position == 1:

            miniufo1.rect.topleft=(xminiufo1,yminiufo1)
            screen.blit(miniufo1.image, miniufo1.rect)

            miniufo3.rect.topleft=(xminiufo3,yminiufo3)
            screen.blit(miniufo3.image, miniufo3.rect)

            yminiufo1 = yminiufo1 + moveminiufo
            yminiufo3 = yminiufo3 + moveminiufo

        #If the position value is 2, only display miniufo1 and miniufo2 and have them move down the screen
        if mini_ufos_position == 2:

            miniufo1.rect.topleft=(xminiufo1,yminiufo1)
            screen.blit(miniufo1.image, miniufo1.rect)

            miniufo2.rect.topleft=(xminiufo2,yminiufo2)
            screen.blit(miniufo2.image, miniufo2.rect)

            yminiufo1 = yminiufo1 + moveminiufo
            yminiufo2 = yminiufo2 + moveminiufo

        #If the position value is 3, only display miniufo2 and miniufo3 and have them move down the screen
        if mini_ufos_position == 3:

            miniufo2.rect.topleft=(xminiufo2,yminiufo2)
            screen.blit(miniufo2.image, miniufo2.rect)

            miniufo3.rect.topleft=(xminiufo3,yminiufo3)
            screen.blit(miniufo3.image, miniufo3.rect)

            yminiufo2 = yminiufo2 + moveminiufo
            yminiufo3 = yminiufo3 + moveminiufo

        #If any of the miniufos get close to going off the screen, set the coordinates of the three miniufos back to default position
        if yminiufo1 > 800 or yminiufo2 > 800 or yminiufo3 > 800:
            xminiufo1 = 270
            yminiufo1 = 0

            xminiufo2 = 450
            yminiufo2 = 0

            xminiufo3 = 540
            yminiufo3 = 0

            #Randomly generate a new position value
            mini_ufos_position = random.randint(1,3)

        #If the comet gets close to going off the screen, move the comet back to the top of the screen
        if ycomet3 > 800:
            ycomet3 = 0

        #If the rocket collides with miniufo1, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo1)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with miniufo2, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo2)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with miniufo3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun5, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun5)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun6, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun6)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun7, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun7)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun8, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun8)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with comet3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,comet3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #The coordinates of the rocket are put into a list so they can be displayed together on the screen
        coordinates = [xrocket, yrocket]

        #All the useful information at the top of the screen (amount of lives, level name, and cooridinates) are displayed on the screen
        font = pygame.font.Font(None,30)
        text1 = font.render("Player Coordinates: " ,True,(255,0,0))
        screen.blit(text1, (520,10))

        font = pygame.font.Font(None,30)
        text1 = font.render(str(coordinates) ,True,(255,255,255))
        screen.blit(text1, (730,10))

        font = pygame.font.Font(None,30)
        text1 = font.render("Hard Level" ,True,(255,255,255))
        screen.blit(text1, (5,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("Lives: " + str(lives) ,True,(255,255,255))
        screen.blit(text1, (200,5))

        #The event for the keys is defined
        event=pygame.event.poll()

        #If the user presses the quit button, break out of the Easy Level Loop
        if (event.type==pygame.QUIT):
            break

        #If the user presses a key down
        elif (event.type==pygame.KEYDOWN):#KEYDOWN means a key is pressed

            #Move the rocket right if the user presses down the "D" key
            if (event.key==pygame.K_d):
                moverocketx=5
                moverockety=0

            #Move the rocket left if the user presses down the "A" key
            elif (event.key==pygame.K_a):
                moverocketx=-5
                moverockety=0

            #Move the rocket up if the user presses down the "W" key
            elif (event.key==pygame.K_w):
                moverockety=-5
                moverocketx=0

            #Move the rocket down if the user presses down the "S" key
            elif (event.key==pygame.K_s):
                moverockety=5
                moverocketx=0

            #If the user presses the end key, break out of the Hard Level Loop
            elif (event.key==pygame.K_END):
                break

            #If the user presses the "Q" key, define the level as being complete and break out of the Hard Level Loop (used to skip levels as a cheat)
            elif (event.key==pygame.K_q):
                levelcomplete = 3
                break

        #If the user doesn't press any keys, keep the rocket stationary
        elif (event.type==pygame.KEYUP):
            moverocketx = 0
            moverockety = 0

        #The screen is update so all the changes to the coordinates of all sprites can be displayed
        pygame.display.update()

    #If the level is defined to be incomplete, set the value of n to True to restart the game by using the continue command to restart the menu while statement
    if levelcomplete == 2:
        n = True
        continue

    #One second delay
    time.sleep(1)

    #The rocket coordinates are set back to the starting position
    xrocket = 430
    yrocket = 600

    #The position layout of the miniufos is set back to default
    mini_ufos_position = 1

    #The speed at which the miniufos move is modified to 8
    moveminiufo = 8

    #------------------------------------------- Boss Level Loop --------------------------------------------------------------

    while(True):

        #All the images in the Hard Level are displayed
        #The screen is cleared of any image before the images are displayed onto the screen
        screen.fill(BLACK)
        rocket.rect.topleft=(xrocket,yrocket)

        screen.blit(background.image, (0,0))
        screen.blit(rocket.image, rocket.rect)

        sun3.rect.topleft=(xsun3,ysun3)
        screen.blit(sun3.image, sun3.rect)

        sun4.rect.topleft=(xsun4,ysun4)
        screen.blit(sun4.image, sun4.rect)

        sun5.rect.topleft=(xsun5,ysun5)
        screen.blit(sun5.image, sun5.rect)

        sun6.rect.topleft=(xsun6,ysun6)
        screen.blit(sun6.image, sun6.rect)

        asteroid3.rect.topleft=(xasteroid3,yasteroid3)
        screen.blit(asteroid3.image, asteroid3.rect)

        asteroid4.rect.topleft=(xasteroid4,yasteroid4)
        screen.blit(asteroid4.image, asteroid4.rect)

        boss.rect.topleft=(xboss,yboss)
        screen.blit(boss.image, boss.rect)

        asteroid5.rect.topleft=(xasteroid5,yasteroid5)
        screen.blit(asteroid5.image, asteroid5.rect)

        asteroid6.rect.topleft=(xasteroid6,yasteroid6)
        screen.blit(asteroid6.image, asteroid6.rect)

        #The movement variables are added to their corresponding coordinate variables to allow movement in the level
        xrocket = xrocket + moverocketx
        yrocket = yrocket + moverockety
        xboss = xboss + moveboss

        #If the user tries to fly off at the bottom of the screen, move them up
        if yrocket > 650:
            yrocket = yrocket - 10

        #If the user tries to fly off screen on the left, move them right
        if xrocket < 0:
            xrocket = xrocket + 10

        #If the user tries to fly off screen on the right, move them left
        if xrocket > 850:
            xrocket = xrocket - 10

        #If the boss gets too close to the sun on its left side, have the boss move to the right
        if xboss < 260:
            moveboss = 7

        #If the boss gets too close to the sun on its right side, have the boss move to the left
        if xboss > 400:
            moveboss = -7

        #If the position value of the miniufos is 1, only display miniufo4 and miniufo6 and have them move down the screen
        if mini_ufos_position == 1:

            miniufo4.rect.topleft=(xminiufo4,yminiufo4)
            screen.blit(miniufo4.image, miniufo4.rect)

            miniufo6.rect.topleft=(xminiufo6,yminiufo6)
            screen.blit(miniufo6.image, miniufo6.rect)

            yminiufo4 = yminiufo4 + moveminiufo
            yminiufo6 = yminiufo6 + moveminiufo

        #If the position value of the miniufos is 2, only display miniufo4 and miniufo5 and have them move down the screen
        if mini_ufos_position == 2:

            miniufo4.rect.topleft=(xminiufo4,yminiufo4)
            screen.blit(miniufo4.image, miniufo4.rect)

            miniufo5.rect.topleft=(xminiufo5,yminiufo5)
            screen.blit(miniufo5.image, miniufo5.rect)

            yminiufo4 = yminiufo4 + moveminiufo
            yminiufo5 = yminiufo5 + moveminiufo

        #If the position value of the miniufos is 3, only display miniufo5 and miniufo6 and have them move down the screen
        if mini_ufos_position == 3:

            miniufo5.rect.topleft=(xminiufo5,yminiufo5)
            screen.blit(miniufo5.image, miniufo5.rect)

            miniufo6.rect.topleft=(xminiufo6,yminiufo6)
            screen.blit(miniufo6.image, miniufo6.rect)

            yminiufo5 = yminiufo5 + moveminiufo
            yminiufo6 = yminiufo6 + moveminiufo

        #If any of the miniufos go off the screen for some distance, set the coordinates of the three miniufos back to default position
        if yminiufo4 > 1500 or yminiufo5 >1500 or yminiufo6 > 1500:
            xminiufo4 = 270
            yminiufo4 = 0

            xminiufo5 = 400
            yminiufo5 = 0

            xminiufo6 = 540
            yminiufo6 = 0

            #A new miniufo position is randomly generated
            mini_ufos_position = random.randint(1,3)

        #If the position value of the comets is 1, only display comet4 and comet6 and have them move to the right on the screen
        if comets_position == 1:

            comet4.rect.topleft=(xcomet4,ycomet4)
            screen.blit(comet4.image, comet4.rect)

            comet6.rect.topleft=(xcomet6,ycomet6)
            screen.blit(comet6.image, comet6.rect)

            xcomet4 = xcomet4 + movecomet_456
            xcomet6 = xcomet6 + movecomet_456

        #If the position value of the comets is 2, only display comet5 and comet6 and have them move to the right on the screen
        if comets_position == 2:

            comet5.rect.topleft=(xcomet5,ycomet5)
            screen.blit(comet5.image, comet5.rect)

            comet6.rect.topleft=(xcomet6,ycomet6)
            screen.blit(comet6.image, comet6.rect)

            xcomet5 = xcomet5 + movecomet_456
            xcomet6 = xcomet6 + movecomet_456

        #If the position value of the comets is 3, only display comet4 and comet5 and have them move to the right on the screen
        if comets_position == 3:

            comet4.rect.topleft=(xcomet4,ycomet4)
            screen.blit(comet4.image, comet4.rect)

            comet5.rect.topleft=(xcomet5,ycomet5)
            screen.blit(comet5.image, comet5.rect)

            xcomet4 = xcomet4 + movecomet_456
            xcomet5 = xcomet5 + movecomet_456

        #If any of the comets go off the screen for some distance, set the coordinates of the three comets back to default position
        if xcomet4 > 2400 or xcomet5 >2400 or xcomet6 > 2400:
            xcomet4 = 0
            ycomet4 = 150

            xcomet5 = 0
            ycomet5 = 300

            xcomet6 = 0
            ycomet6 = 450

            #A new comet position layout is randomly generated
            comets_position = random.randint(1,3)

        #If the rocket collides with sun3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun5, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun5)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun6, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun6)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun7, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun7)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with sun8, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,sun8)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid3, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid3)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid5, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid5)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with asteroid6, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,asteroid6)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with miniufo4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with miniufo5, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo5)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with miniufo6, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,miniufo6)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with comet4, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,comet4)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with comet5, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,comet5)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with comet6, subtract one life and set the coordinates of the rocket back to starting position
        if (pygame.sprite.collide_rect(rocket,comet6)):
            lives = determineLives(lives)

            xrocket = 430
            yrocket = 600

            #If the user runs out of lives, go through the game over procedure (look at gameOver() function) and break out of the medium level loop
            if lives == 0:
                gameOver()
                break

        #If the rocket collides with the boss, subtract 10 from the bosses HP and move the rocket 10 down
        if (pygame.sprite.collide_rect(rocket,boss)):

            bossHP = bossHP - 10
            yrocket = yrocket + 10

        #The coordinates of the rocket are put into a list so they can be displayed together on the screen
        coordinates = [xrocket, yrocket]

        #All the useful information at the top of the screen (amount of lives, level name, player coordinates) are displayed on the screen
        font = pygame.font.Font(None,30)
        text1 = font.render("Player Coordinates: " ,True,(255,0,0))
        screen.blit(text1, (520,10))

        font = pygame.font.Font(None,30)
        text1 = font.render(str(coordinates) ,True,(255,255,255))
        screen.blit(text1, (730,10))

        font = pygame.font.Font(None,30)
        text1 = font.render("Boss Level" ,True,(255,255,255))
        screen.blit(text1, (5,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("Lives: " + str(lives) ,True,(255,255,255))
        screen.blit(text1, (200,5))

        font = pygame.font.Font(None,30)
        text1 = font.render("Boss HP: "  ,True,(255,255,255))
        screen.blit(text1, (300,5))

        font = pygame.font.Font(None,30)
        text1 = font.render( str(bossHP)  ,True,(255,255,255))
        screen.blit(text1, (400,5))

        #Event for the keys is defined
        event=pygame.event.poll()

        #If the user presses the quit button, break out of the Boss Level Loop
        if (event.type==pygame.QUIT):
            break

        #If the user presses a key down
        elif (event.type==pygame.KEYDOWN):#KEYDOWN means a key is pressed

            #Move the rocket right if the user presses down the "D" key
            if (event.key==pygame.K_d):
                moverocketx=5
                moverockety=0

            #Move the rocket left if the user presses down the "A" key
            elif (event.key==pygame.K_a):
                moverocketx=-5
                moverockety=0

            #Move the rocket up if the user presses down the "W" key
            elif (event.key==pygame.K_w):
                moverockety=-5
                moverocketx=0

            #Move the rocket down if the user presses down the "S" key
            elif (event.key==pygame.K_s):
                moverockety=5
                moverocketx=0

            #If the user presses the end key, break out of the Boss Level Loop
            elif (event.key==pygame.K_END):
                break

            #If the user presses the "Q" key, define the level as being complete and break out of the Boss Level Loop (used to skip levels as a cheat)
            elif (event.key==pygame.K_q):
                levelcomplete = 4
                break

        #If the user doesn't press any keys, keep the rocket stationary
        elif (event.type==pygame.KEYUP):
            moverocketx = 0
            moverockety = 0

        #The screen is update so all the changes to all sprites are displayed onto the screen
        pygame.display.update()

        #If the boss HP is reduced to 0, define the level as being complete and break out of the Boss Level Loop
        if bossHP == 0:
            levelcomplete = 4
            break

    #If the level is defined to be incomplete, set the value of n to True to restart the game by using the continue command to restart the menu while statement
    if levelcomplete == 3:
        n = True
        continue

    #If the level is complete, go through the procedure of winning the game (see the code in the "gameWin()" function) and set the value of n to 1 and use a continue statement to bring the user back to the menu
    if levelcomplete == 4:
        gameWin()
        n = 1
        continue

#Quits the program
pygame.quit()


