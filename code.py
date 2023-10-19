from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Мышеловка")
background = transform.scale(image.load('fon.jpg'),(win_width, win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sise_x,sise_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sise_x,sise_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width-80)
            self.rect.y = 0
            lost = lost + 1
'''mixer.init()
mixer.music.load('')
mixer.music.play()'''
FPS = 120
clock= time.Clock()
run = True
mouseX = -15
mouseY = 418
mouse = Player('mouse.png',mouseX,mouseY, 5,250, 100)
chesses = sprite.Group()
for i in range(1,3):
    chesse = Enemy("chesse.png",randint(80,win_width-80),-40,randint(5,10),90,65)
    chesses.add(chesse)

font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',36)
win = font1.render('YOU WIN!', True, (255,255,255))
lose = font1.render('YOU LOSE:(', True, (188,0,0))
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0, 0))
        mouse.update()
        mouse.reset()
        chesses.update()
        chesses.draw(window)
        if sprite.spritecollide(mouse,chesses, True):
            chesse = Enemy("chesse.png",randint(80,win_width-80),-40,randint(5,10),90,65)
            chesses.add(chesse)
            score +=1
        if score == 5:
            finish = True
            window.blit(lose,(200,200))

        text_lose = font1.render('Увернулся:'+ str(lost), 1,(255,255,255))
        window.blit(text_lose,(10,20)) 
        text_score = font1.render('Пойман:'+ str(score), 1,(255,255,255))
        window.blit(text_score,(10,50)) 
        
    

        clock.tick(FPS)
    display.update()



