from abc import *

class Scene:
    def __init__(self) -> None:
        self.name = 'SceneName'
        self.screen = None
    
    def act(self):
        pass
    
    def setScreen(self,screen):
        self.screen = screen
    
    def __repr__(self) -> str:
        return self.name

class StartScene(Scene):
    def __init__(self):
        self.name = 'StartScene'
        self.screen = None

class ItemTestScene(Scene):
    def __init__(self):
        self.name = 'ItemTestScene'
        self.screen = None