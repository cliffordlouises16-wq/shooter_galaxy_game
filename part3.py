from pygame import *
from random import randint

#background music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


#fonts and captions
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 36)


#we need the following images:
img_back = "galaxy.jpg"  #game background
img_hero = "rocket.png"  #hero
img_bullet = "bullet.png"  #bullet
img_enemy = "ufo.png"  #enemy

# parent class for other sprites
class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # Every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # Every sprite must have the rect property
        self.rect = self.image.get_rect()
        self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.XXXXXXX(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    # method to shoot
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


# enemy sprite class
class Enemy(GameSprite):
    # enemy movement
    def update(self):
        self.rect.y += self.speed
        global lost

        # disappears upon reaching the screen edge
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


# bullet sprite class
class Bullet(GameSprite):
    # bullet movement
    def update(self):
        self.rect.y += self.speed

        # disappears upon reaching the screen edge
        if self.rect.y < 0:
            self.kill()