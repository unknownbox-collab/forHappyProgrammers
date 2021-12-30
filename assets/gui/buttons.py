import pygame, os
from assets.setting.parameter import *

class Button:
    def setting(self,x,y,size,img):
        self.x = x
        self.y = y
        self.preClick = False
        self.xSize = size[0]
        self.ySize = size[1]
        IMG = pygame.image.load(os.path.join('.','assets','image','ui',img))
        self.skin = pygame.transform.scale(IMG, (self.xSize, self.ySize))
    
    def setImg(self,img):
        IMG = pygame.image.load(os.path.join('.','assets','image','ui',img))
        self.skin = pygame.transform.scale(IMG, (self.xSize, self.ySize))
    
    def clicked(self,mouse,**karg):
        x, y, clicked = mouse
        xSize = self.xSize/2
        ySize = self.ySize/2
        xCheck = x - SCREEN_WIDTH / 2 - self.x
        yCheck = y - SCREEN_HEIGHT / 2 - self.y
        if - xSize <= xCheck <= xSize and - ySize <= yCheck <= ySize and clicked:
            if not self.preClick:
                self.preClick = True
                return self.clickMethod(**karg)
        else:
            self.preClick = False
    
    def onMouse(self,mouse,**karg):
        x, y, clicked = mouse
        xSize = self.xSize/2
        ySize = self.ySize/2
        xCheck = x - SCREEN_WIDTH / 2 - self.x
        yCheck = y - SCREEN_HEIGHT / 2 - self.y
        if - xSize <= xCheck <= xSize and - ySize <= yCheck <= ySize and clicked:
            if not self.preClick:
                self.preClick = True
                return self.onMouseMethod(**karg)
        else:
            self.preClick = False

    def show(self,screen):
        self.skinRect = self.skin.get_rect(center = (SCREEN_WIDTH/2 + self.x, SCREEN_HEIGHT/2 + self.y))
        screen.blit(self.skin, self.skinRect)
    
    def clickMethod(self):
        pass
    
    def onMouseMethod(self):
        pass

class StartButton(Button):
    def setting(self, x, y):
        super().setting(x, y, (200,100), '시작버튼.png')
    
    def clickMethod(self):
        return ('CHS', SETTING_SCENE)

class ShopButton(Button):
    def setting(self, x, y):
        super().setting(x, y, (250,125), '상점버튼.png')
    
    def clickMethod(self):
        return ('CHS', SHOP_BUTTON)

class DotoriChooseButton(Button):
    def setting(self, x, y):
        super().setting(x, y, (100,100), 'DotoriChooseButton.png')
    
    def clickMethod(self):
        return ('CCHO', DOTORI)

class GamtoriChooseButton(Button):
    def setting(self, x, y):
        super().setting(x, y, (100,100), 'GamtoriChooseButton.png')
    
    def clickMethod(self):
        return ('CCHO', GAMTORI)