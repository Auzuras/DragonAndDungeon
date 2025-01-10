from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from GameClasses.FightArea import FightArea

def test_DragonAndDungeon_test():
    player = Player("Jean", 1, 1)
    
    assert type(player) == Player
    
    enemy = Enemy("Jack", 1, 1)
    
    assert type(enemy) == Enemy
    
    arena = FightArea(player, enemy, 0)
    
    assert type(arena) == FightArea