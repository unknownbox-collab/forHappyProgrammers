import pygame,os
from assets.setting.parameter import *

class Character:
    def setting(self,x,y,degree,size,img):
        self.x = x
        self.y = y
        self.degree = degree
        self.preClick = False
        self.xSize = size[0]
        self.ySize = size[1]
        IMG = pygame.image.load(os.path.join('.','assets','image','character',img))
        IMG = pygame.transform.scale(IMG, (self.xSize, self.ySize))
        self.skin = pygame.Surface(size,pygame.SRCALPHA)
        self.skin.blit(IMG,(0,0))
        
    def setImg(self,img):
        IMG = pygame.image.load(os.path.join('.','assets','image','character',img))
        self.skin = pygame.transform.scale(IMG, (self.xSize, self.ySize))
    
    def show(self,screen):
        skin = pygame.transform.rotate(self.skin, self.degree)
        self.skinRect = skin.get_rect(center = (SCREEN_WIDTH/2 + self.x, SCREEN_HEIGHT/2 + self.y))
        screen.blit(skin, self.skinRect)

class Dotori(Character):
    def setting(self, x, y, degree = 0, size = (200,300)):
        return super().setting(x, y, degree, size, 'Dotori.png')

class Gamtori(Character):
    def setting(self, x, y, degree = 0, size = (200,300)):
        return super().setting(x, y, degree, size, 'Gamtori.png')