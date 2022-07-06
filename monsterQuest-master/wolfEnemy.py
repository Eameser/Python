#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
import random

#inherits enemy
class wolf(enemy):
    #initializes wolf
    def __init__(self, n, h):
        self.name = n
        self.health = h
        self.maxHealth = 100
        self.lvl = 2

    def __str__(self):
        return 'I am a Wolf named ' + self.name

    def getName(self):
        return self.name
    #different attacks based on random number generated
    def attack(self, other):
        x = random.randint(1,3)
        if x == 1:
            other.takeDamage(40)
        elif x == 2:
            other.takeDamage(20)
        else:
            other.takeDamage(10)
    #returns current health
    def getHealth(self):
        return self.health

    #takes damage when attacked
    def takeDamage(self, damage):
        self.health = self.health - damage

    #returns max health of enemy
    def maxHealth(self):
        return self.maxHealth

    #can set health to a different value if necessary
    def setHealth(self, health):
        self.health = health
