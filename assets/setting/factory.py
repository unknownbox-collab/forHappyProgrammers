from assets.setting.items import *
from assets.setting.player import *
from assets.setting.parameter import *
from assets.setting.character import *
from assets.gui.buttons import *
from abc import *

from assets.setting.player import Player
        
class Factory(metaclass=ABCMeta):
    @abstractclassmethod
    def create(name):
        pass

class PlayerFactory(Factory):
    def create(self):
        return Player()

class ButtonFactory(Factory):
    def create(self, name):
        if name == START_BUTTON:
            return StartButton()
        elif name == SHOP_BUTTON:
            return ShopButton()
        elif name == DOTORI_CHOOSE_BUTTON:
            return DotoriChooseButton()
        elif name == GAMTORI_CHOOSE_BUTTON:
            return GamtoriChooseButton()

class CharacterFactory(Factory):
    def create(self, name):
        if name == DOTORI:
            return Dotori()
        elif name == GAMTORI:
            return Gamtori()

class ItemFactory(Factory):
    def create(self, name):
        if name == COLD_MEDICINE_ITEM:
            return ColdMedicineItem()
        elif name == RECORDER_ITEM:
            return RecorderItem()
        elif name == BUTTON_ITEM:
            return ButtonItem()
        elif name == WATER_ITEM:
            return WaterItem()
        elif name == WATER_TAP_ITEM:
            return WaterTapItem()
        elif name == UMBRELLA_ITEM:
            return UmbrellaItem()
        elif name == CROSS_ITEM:
            return CrossItem()
        elif name == NOTE_OF_DOTORI_ITEM:
            return NoteOfDotoriItem()
        elif name == SCISSOR_ITEM:
            return ScissorItem()
        elif name == BOOK_ITEM:
            return BookItem()
        elif name == MONITOR_ITEM:
            return MonitorItem()
        elif name == MINI_SUN_CLOCK_ITEM:
            return MiniSunClockItem()
        elif name == CHEON_JE_PENCIL_ITEM:
            return CheonJePencilItem()
        elif name == YORSIA_DARKNESS_SPHERE_ITEM:
            return YorsiaDarknessSphereItem()
        elif name == BICYCLE_ITEM:
            return BicycleItem()
        elif name == SHAPED_RULER_ITEM:
            return ShapedRulerItem()