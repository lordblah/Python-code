from abc import ABCMeta,abstractmethod
#creating base class
class Enemy(object):
    __metaclass__ = ABCMeta

    @abstractmethod #decorator, going to alter it
    def attackPlayer(self,player):
        pass

class EnvironmentAsset(object): #
    __metaclass__ =  ABCMeta
    @abstractmethod
    def __init__(self): #saying that they cannot move
        self.mobile = False

class Trap(Enemy, EnvironmentAsset): #inheriting from two other clsses
    def __init__(self):
        super(Trap,self).__init__()
    def attackPlayer(self,player):
        return player.health - 10

x = 10






#why een use this, having a class, inherite from multiple classes
#is useful, so you don't have to write a new class. take from what you have in stock
