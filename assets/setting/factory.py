from assets.gui.scenes import *
from assets.setting.items import *
from assets.setting.parameter import *
from abc import *
        
class Factory(metaclass=ABCMeta):
    @abstractclassmethod
    def create(name):
        pass

class SceneFactory(Factory):
    def create(self, name):
        if name == START_SCENE:
            return StartScene()
        elif name == ITEM_TEST_SCENE:
            return ItemTestScene()

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