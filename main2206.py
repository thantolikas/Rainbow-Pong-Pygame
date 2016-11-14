import pygame, sys, mylib2206
from pygame.locals import *

def splash_loop(splash, window):
    my_clock = pygame.time.Clock()  # the clock

    clicked = False 
    while clicked == False:
        for ev in pygame.event.get():
        # print(ev.type)
            if ev.type == QUIT:
                pygame.quit()           
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    clicked = True
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
        splash.draw(window) 
        pygame.display.update()
    
        my_clock.tick(120)

pygame.init()

settings = mylib2206.Settings(800, 700)  # initializing the static game info and onjects

pygame.mixer.music.load("bg_music.mp3")  # loaging background music
pygame.mixer.music.play(-1)  # playing music in repeat

# initializing pygame
main_window = pygame.display.set_mode((settings.horiz, settings.vert)) 
pygame.display.set_caption("Rainbow Pong")

my_clock = pygame.time.Clock()  # the clock

# Loop for the splash screen / When space is pressed the loop breaks
splash_loop(settings.splash,main_window)
           
# main game loop          
while True:
    
    # event checking
    for ev in pygame.event.get():
        # print(ev.type)
        if ev.type == QUIT:
            pygame.quit()           
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                settings.platform.moveUp = True
            elif ev.key == K_DOWN:
                settings.platform.moveDown = True
            elif ev.key == K_w:
                settings.platform2.moveUp = True
            elif ev.key == K_s:
                settings.platform2.moveDown = True
            elif ev.key == K_ESCAPE: # if ESCAPE is pressed the game stops and the splash is shown
                settings.p1score = 0 # the scores go back to 0
                settings.p2score = 0
                splash_loop(settings.splash, main_window)
                
        if ev.type == KEYUP:
            if ev.key == K_UP:
                settings.platform.moveUp = True
            elif ev.key == K_DOWN:
                settings.platform.moveDown = True
            elif ev.key == K_w:
                settings.platform2.moveUp = True
            elif ev.key == K_s:
                settings.platform2.moveDown = True
 
    
    # Drawing objects 
    settings.bg.draw(main_window)
    settings.top_border.draw(main_window)
    settings.btm_border.draw(main_window)
    settings.platform.draw(main_window)
    settings.platform2.draw(main_window)
    
    # Moving the objects accordingly
    settings.platform.move(main_window, settings)
    settings.platform2.move(main_window, settings)
    settings.platform.moveDown = settings.platform2.moveDown = False
    settings.platform.moveUp = settings.platform2.moveUp = False
    settings.ball.move(main_window, settings)
    
    # Displaying the score
    my_font = pygame.font.Font("Pixeled.ttf", 100)    
    
    # player 1 score
    player1 = my_font.render\
                (str(settings.p1score), True, (66, 3, 248))  
    # player 2 score
    player2 = my_font.render\
                (str(settings.p2score), True, (66, 3, 248))            
    
    main_window.blit(player1, (100, 100))
    main_window.blit(player2, (600, 100))
    
    

           
    pygame.display.update()
    my_clock.tick(120)




