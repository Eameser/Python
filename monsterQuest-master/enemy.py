#Code created by Akash Patel CS-172-C Lab Section 069

import abc

#abstract base class
class enemy(metaclass = abc.ABCMeta):
    #methods that will be inherited by enemies
    def __init__(self, name, health):
        return
    
    def __str__(self):
        return 'enemy'
    
    def setName(self):
        pass
    
    def getName(self):
        pass
    
    def setHealth(self):
        pass
    
    def getHealth(self):
        pass
    
    @abc.abstractmethod
    #all classes that inherit enemy must have attack and take damage
    def attack(self, other):
        pass
    
    @abc.abstractmethod
    def takeDamage(self, other):
        pass
    
    def maxHealth(self):
        pass
		



 