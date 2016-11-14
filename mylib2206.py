from pygame.sprite import *

# GameObject Class
# Inherits from Sprite
# Generalized sprite object
class GameObject(Sprite):
    def __init__(self, top, left, height, width, imageName):
        Sprite.__init__(self)
        self.rect = pygame.Rect(top, left, height, width)
        self.image = pygame.image.load(imageName)
        self.transimage = pygame.transform.scale(self.image, (height, width))
    # Draws the object on the screen
    def draw(self, window):
        window.blit(self.transimage, self.rect)
# Settings class
# Holds all the game objects and info
class Settings:
    def __init__(self, horiz, vert):
        self.horiz = horiz  # Horizontal screen resolution
        self.vert = vert  # Vertical screen resolution
        self.top_border = GameObject(0, 0, 800, 20, "border.png")  # Top border 
        self.btm_border = GameObject(0, 680, 800, 20, "border.png")  # Bottom border
        self.p1score = 0  # Player 1 score
        self.p2score = 0  # Player 2 score
        self.platform = Platform(0, 50, 17, 115, -20, "2.png")  # Player 1 platform
        self.platform2 = Platform(783, 50, 17, 115, -20, "2.png")  # Player 2 platform
        self.bg = GameObject(0, 0, 800, 700, "bg.png")  # The background image
        self.splash = GameObject(0, 0, 800, 700, "splash.png")  # The splash image
        self.ball = Ball(500, 200, 35, 35, 3, 3, "1.png")  # The ball

# AnimatedObject Class
# Inherits from GameObject
# For animated game objects
class AnimatedObject(GameObject):
    def __init__(self, top, left, height, width, speedX, speedY, imageName):
        Sprite.__init__(self)               
        GameObject.__init__(self, top, left, height, width, imageName)
        self.speedX = speedX
        self.speedY = speedY
        
    def move(self, window, settings):
        pass
    def check_bounce(self, window, settings):
        pass
    
# Ball class
# Inherits from AnimatedObject
# Represents the ball
class Ball(AnimatedObject):
    def __init__(self, top, left, height, width, speedX, speedY, imageName):
        AnimatedObject.__init__(self, top, left, height, width, speedX, speedY, imageName)
    
    # moves the ball by speedX and speedY and call check_bounce method
    def move(self, window, settings):
        self.rect.move_ip(self.speedX, self.speedY)
        self.draw(window)
        return self.check_bounce(settings, window)
    # checks if the ball collides with the other sprites of the game
    def check_bounce(self, settings, window, offset=0):
        if pygame.sprite.collide_rect(self, settings.top_border):  # if the ball collides with top border
            self.rect.move_ip(0, -self.speedY)
            self.speedY = -self.speedY
            self.draw(window)
        
        elif pygame.sprite.collide_rect(self, settings.btm_border):  # if the ball collides with the bottom border
            self.rect.move_ip(0, self.speedY - 2)
            self.speedY = -self.speedY
            self.draw(window)
        
        elif pygame.sprite.collide_rect(self, settings.platform):  # if the ball collides with the player 1 platform
            self.speedX = -self.speedX
        
        elif pygame.sprite.collide_rect(self, settings.platform2):  # if the ball collides with the player 2 platform
            self.speedX = -self.speedX
        
        elif self.rect.left < -offset:  # if the ball reached the left end of the window / if yes gives a point to player 1 and changes the speed
            settings.p2score += 1
            self.speedX = -self.speedX

        elif self.rect.right > settings.horiz + offset:  # if the ball reached the right end of the window / if yes gives a point to player 2
            settings.p1score += 1
            self.speedX = -self.speedX

# Platform class
# Inherits from AnimatedObject
# Represents the players' platforms
class Platform(AnimatedObject):
    def __init__(self, top, left, height, width, speedY, imageName):
        AnimatedObject.__init__(self, top, left, height, width, 0, speedY, imageName)
        self.moveUp = False
        self.moveDown = False
    
    # moves the platform by speedX and speedY depending on the moveUp and moveDown variables and calls check_bounce method
    def move(self, window, settings):
        if self.moveUp == True:
            self.rect.move_ip(self.speedX, self.speedY)
            self.draw(window)
        
        elif self.moveDown == True:
            self.rect.move_ip(self.speedX, -self.speedY)
            self.draw(window)
        
        return self.check_bounce(window, settings)
    
    # checks if the plaform collides with one of the borders (top or bottom) of the game
    def check_bounce(self, window, settings):
        if self.moveUp:
            if pygame.sprite.collide_rect(self, settings.top_border):  # collision with the top_border
                self.rect.move_ip(0, -self.speedY)
                self.draw(window)
                self.moveUp = False
        
        elif self.moveDown:
            if pygame.sprite.collide_rect(self, settings.btm_border):  # collision with the btm border
                self.rect.move_ip(0, self.speedY)
                self.draw(window)
                self.moveDown = False

            
    
    
    
    
