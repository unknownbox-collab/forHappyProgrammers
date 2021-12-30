import pygame,os
from parameter import *

class Item:
    def __init__(self) -> None:
        self.img = None
        self.rect = None
        self.x = 0
        self.y = 0
        self.name = "ItemName"
        self.description = "ItemDescription"
        self.cost = 0
        self.buff = {}
    
    def setting(self, img, name, description, cost, buff = {}, size = (0,0)):
        img = pygame.image.load(os.path.join('.','assets','items',img))
        self.name = name
        self.description = description
        self.cost = 0
        self.img = pygame.Surface(size[0],size[1])
        self.img.blit(self.img, img)
        self.img = pygame.transform.scale(self.img,size)
        self.rect = img.get_rect()
        self.cost = cost
        self.buff = buff
    
    def setLocation(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self,screen):
        screen.blit()

# 감기약
class ColdMedicineItem(Item):
    def setting(self):
        description = "{체력} + 200"
        super().setting("감기약.png", "감기약", description, 100, {HP : 200})
    
# 녹음기
class RecorderItem(Item):
    def setting(self):
        description = "{공격력} + 20"
        super().setting("녹음기.png", "녹음기", description, 100, {ATK : 20})

# 버튼
class ButtonItem(Item):
    def setting(self):
        description = "{주문력} + 30"
        super().setting("버튼.png", "버튼", description, 100, {AP : 30})

# (식물이)먹어도 괜찮은 물
class WaterItem(Item):
    def setting(self):
        description = "{하트} + 400"
        super().setting("물.png", "(식물전용)식용수", description, 100, {HRT : 400})

# 수도꼭지
class WaterTapItem(Item):
    def setting(self):
        description = "{치명타} + 15%"
        super().setting("수도꼭지.png", "수도꼭지", description, 100, {CRI : 15})

# 우산
class UmbrellaItem(Item):
    def setting(self):
        description = "{방어력} + 20"
        super().setting("우산.png", "우산", description, 100, {DEF : 20})

# 십자가
class CrossItem(Item):
    def setting(self):
        description = "{회복력} + 40"
        super().setting("십자가.png", "십자가", description, 100, {HEAL : 40})

# 도토리의 공책
class NoteOfDotoriItem(Item):
    def setting(self):
        description = "{체력} + 500"
        super().setting("도토리의 공책.png", "도토리의 공책", description, 200, {HP : 500})

# 가위
class ScissorItem(Item):
    def setting(self):
        description = "{공격력} + 50"
        super().setting("가위.png", "가위", description, 200, {ATK : 50})

# 책
class BookItem(Item):
    def setting(self):
        description = "{주문력} + 80"
        super().setting("책.png", "책", description, 200, {AP : 80})

# 모니터
class BookItem(Item):
    def setting(self):
        description = "{주문력} + 80"
        super().setting("책.png", "책", description, 200, {AP : 80})