from assets.gui.buttons import *
from assets.setting.parameter import *
from assets.setting.factory import *
from assets.setting.character import *

itemFac = ItemFactory()
buttonFac = ButtonFactory()
characterFac = CharacterFactory()

class Scene:
    def __init__(self) -> None:
        self.name = 'SceneName'
    
    def act(self, mouse = None, **kargs):
        return [None]

    def show(self, screen):
        pass
    
    def __repr__(self) -> str:
        return self.name

class StartScene(Scene):
    def __init__(self):
        self.name = 'StartScene'
        self.startButton = buttonFac.create(START_BUTTON)
        self.startButton.setting(0,50)
        self.logo = pygame.image.load(os.path.join('.','assets','image','ui','logo.png'))
        self.logo = pygame.transform.scale(self.logo, (500, 250))
    
    def act(self, mouse = None, **kargs):
        return [self.startButton.clicked(mouse=mouse)]

    def show(self, screen):
        screen.fill(SKYBLUE)
        self.startButton.show(screen)
        logoRect = self.logo.get_rect(center = (SCREEN_WIDTH/2 + 0, SCREEN_HEIGHT/2 - 150))
        screen.blit(self.logo, logoRect)

class SettingScene(Scene):
    def __init__(self):
        self.name = 'SettingScene'
        self.character = characterFac.create(DOTORI)
        self.character.setting(-400,-180)
        self.chooseButtons = []

        start = DOTORI_CHOOSE_BUTTON
        end = GAMTORI_CHOOSE_BUTTON
        for i in range(start, end+1):
            newButton = buttonFac.create(i)
            newButton.setting(-440 + (i - start) * 110,40)
            self.chooseButtons.append(newButton)
    
    def act(self, mouse = None, **kargs):
        return [button.clicked(mouse=mouse) for button in self.chooseButtons]
    
    def show(self, screen):
        screen.fill(SKYBLUE)
        self.character.show(screen)
        pygame.draw.line(screen,BLACK,(0,280),(SCREEN_WIDTH,280),5)
        for button in self.chooseButtons:
            button.show(screen)

        #self.startButton.show(screen)
        #logoRect = self.logo.get_rect(center = (SCREEN_WIDTH/2 + 0, SCREEN_HEIGHT/2 - 150))
        #screen.blit(self.logo, logoRect)

class HowToPlayScene(Scene):
    def __init__(self):
        self.name = 'HowToPlayScene'

class ShopScene(Scene):
    def __init__(self):
        self.name = 'HowToPlayScene'

class InGameScene(Scene):
    def __init__(self) -> None:
        self.name = 'InGameScene'

class LookOpponentScene(Scene):
    def __init__(self) -> None:
        self.name = 'LookOpponentScene'
