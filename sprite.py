import pygame,os

class Sprite:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.degree = 0
        self.img = []
        self.rect = None
        self.now = 0
    
    def setting(self, img):
        temp = list(map(lambda x : pygame.image.load(os.path.join('.','assets',x)), img))
        self.rect = list(map(lambda x : x.get_rect(), temp))
        self.img = list(map(lambda x : pygame.Surface(x.size), self.rect))
        self.img = list(map(lambda x : self.img[x].blit(temp[x], (0,0)), range(len(temp))))
    
    def setLocation(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def changeLocation(self, x = 0, y = 0):
        self.x += x
        self.y += y
    
    def setDegree(self, degree):
        self.degree = degree
    
    def rotate(self, degree):
        self.degree += degree
    
    def show(self,screen):
        screen.blit(self.img[self.now],(self.x,self.y))