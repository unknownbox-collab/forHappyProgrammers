from scenes import *
from parameter import *

class Factory:
    @staticmethod
    def getInstance(name):
        if name == START_SCENE:
            return StartScene()
        elif name == ITEM_TEST_SCENE:
            return StartScene()
        