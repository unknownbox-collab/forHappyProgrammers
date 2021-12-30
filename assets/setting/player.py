class Player:
    def __init__(self) -> None:
        self.character = None
        self.hp = 0
        self.defence = 0
        self.atk = 0
        self.heal = 0
        self.heart = 0
        self.ap = 0
        self.act = 3

        self.buffEffect = {}
        self.inventory = []
        self.money = 0
    
    def setting(self, character):
        self.character = character
        self.hp = character
    
    def show(self):
        self.character.show()