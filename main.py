import pygame,sys
from assets.setting.parameter import *

pygame.init()
pygame.display.set_caption("~~그때 그 발명대회~~")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

from assets.setting.factory import *
from assets.gui.scenes import *

class SceneFactory(Factory):
    def create(self, name):
        if name == START_SCENE:
            return StartScene()
        elif name == SETTING_SCENE:
            return SettingScene()
        elif name == SHOP_BUTTON:
            return ShopScene()
        elif name == IN_GAME_SCENE:
            return InGameScene()
        elif name == LOOK_OPPONENT_SCENE:
            return LookOpponentScene()

sceneFac = SceneFactory()
nowScene = START_SCENE

def compileSceneCmd(cmd):
    global nowScene

    # Change Scene : ('CHS', SCENE_NUM)
    if cmd[0] == 'CHS':
        nowScene = cmd[1]

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        mouse = list(pygame.mouse.get_pos()) + [False]
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse[2] = True
    scene = sceneFac.create(nowScene)
    commands = scene.act(mouse = mouse)
    print(commands)
    if not all(map(lambda x : x is None, commands)):
        for cmd in commands:
            if cmd != None:
                compileSceneCmd(cmd)
    scene.show(screen)
    pygame.display.update()