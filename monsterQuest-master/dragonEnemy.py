#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
#inherits enemy
class dragon(enemy):
    #intializes dragon
    def __init__(self, n, h):
        self.name = n
        self.health = h
        self.maxHealth = 100
        self.lvl = 4

    def str(self):
        return 'I am a Dragon named ' + self.name

    def getName(self):
        return self.name
    #dragon only has 1 attack, does 30 damage
    def attack(self, other):
        other.takeDamage(30)
    #returns current health
    def getHealth(self):
        return self.health
    #takes damage when attacked
    def takeDamage(self, damage):
        self.health = self.health - damage
    #returns dragon's max health
    def maxHealth(self):
        return self.maxHealth
    #can set health to a different value if needed
    def setHealth(self, health):
        self.health = health
