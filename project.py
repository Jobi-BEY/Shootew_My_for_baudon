from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.w = w
        self.rect.h = h
    def  collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    # def die():
    #     if score == 4:
    #         self.kill()
class Wall(sprite.Sprite):
    def __init__(self,cl_1,cl_2,cl_3,x,y,w,h):
        super().__init__()
        self.cl_1 = cl_1
        self.cl_2 = cl_2
        self.cl_3 = cl_3
        self.rect = Rect
        self.width = w
        self.hight = h
        self.image = Surface((self.width, self.hight))
        self.image.fill((cl_1,cl_2,cl_3))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Levers(GameSprite):
    def __init__(self,img1,img2, x,y,w,h,speed):
        super().__init__(img1,x,y,w,h, speed)
        self.image1 = transform.scale(image.load(img1), (w,h))
        self.image2 = transform.scale(image.load(img2), (w,h))
        self.check = False
    def img1(self):
        self.image = self.image1
    def img2(self):
        self.image = self.image2
        global score
        if self.check == False:
            score += 1
            self.check = True


class Player(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.x1 = x
        self.y1 = y
    def update(self):
        self.x1 = self.rect.x
        self.y1 = self.rect.y
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<880:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y <600:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def cancel(self):
        self.rect.x = self.x1
        self.rect.y = self.y1



window = display.set_mode((910,650))
display.set_caption('saveEcoCity')

background = transform.scale(image.load('basement.png'),(910,650))
hero = Player('human.png',70,20,25, 50,5)
levers = sprite.Group()
levers.add(Levers('lever_left.png', 'lever_right.png',100,500,25,25,0))
levers.add(Levers('lever_left.png', 'lever_right.png',800,230,25,25,0))
levers.add(Levers('lever_left.png', 'lever_right.png',280,230,25,25,0))
levers.add(Levers('lever_left.png', 'lever_right.png',800,450,25,25,0))
walls = sprite.Group()
walls.add(Wall(0,0,0,216,0,5,283))
walls.add(Wall(0,0,0,216,283,217,5))
walls.add(Wall(0,0,0,427,139,5,144))
walls.add(Wall(0,0,0,425,137,200,5))
walls.add(Wall(0,0,0,750,165,5,100))
walls.add(Wall(0,0,0,0,460,200,5))
walls.add(Wall(0,0,0,195,466,5,57))
walls.add(Wall(0,0,0,200,523,70,5))
walls.add(Wall(0,0,0,201,615,5,35))
walls.add(Wall(0,0,0,360,371,140,40))
walls.add(Wall(0,0,0,589,367,73,75))
walls.add(Wall(0,0,0,393,490,180,50))
walls.add(Wall(0,0,0,685,485,180,50))
walls.add(Wall(0,0,0,750,265,150,5))
walls.add(Wall(0,0,0,723,367,155,43))
molniuus = sprite.Group()
molniuus.add(GameSprite('molniui.png',460,160,20,40,0))
molniuus.add(GameSprite('molniui.png',500,160,20,40,0))
molniuus.add(GameSprite('molniui.png',460,185,20,40,0))
molniuus.add(GameSprite('molniui.png',500,185,20,40,0))

font.init()
font1 = font.Font(None, 36)
score = 0
finish = False
game = True
FPS = 60 
clock = time.Clock()
font_win = font1.render('Ты выиграл!:)',1,(255,255,255))
font_lose = font1.render('Ты проиграл:( ты не включил все ',1,(255,255,255))
shield= GameSprite('the_shield.png', 450,150,83,83, 0)
loser = GameSprite('lose.png',300,300,00,280,0) 
winner = GameSprite('win.png',300,300,300,280,0)
win = False
los = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
    
        walls.draw(window)
        levers.draw(window)
        shield.reset()
        molniuus.draw(window)
        hero.update()
        hero.reset()
        
        sprite_list1 = sprite.spritecollide(hero,walls,False)
        sprite_list2 = sprite.spritecollide(hero,levers, False)
        sprite_list3 = sprite.collide_rect(hero,shield)
        
        if len(sprite_list1) !=0:
            hero.cancel()
        for i in range(len(sprite_list2)):
            sprite_list2[i].img2()

        levers_score = font1.render('Собрано рычагов'+str(score)+'/4',1,(255,255,255))
        if sprite_list3 == True and score == 4:
            window.blit(font_win, (300,300))
            finish = True
        if sprite_list3 == True and score != 4:
            window.blit(font_lose,(300,300))
            finish = True
    
        window.blit(levers_score,(650,30))
    # if los:
    #     loser.reset()
    # if win:
    #     winner.reset()
    display.update()
    clock.tick(FPS)
        