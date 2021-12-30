from sprite import *

class Button(Sprite):
    def __init__(self) -> None:
        super().__init__()
    
    def setting(self, img, size):
        return super().setting(img)
    
    def click(self, pos):
        rect = self.rect[self.now]
        if rect.left <= pos.x <= rect.left + rect.width and rect.top <= pos.y <= rect.top + rect.height:
            self.rect[self.now]
            pygame.Rect()