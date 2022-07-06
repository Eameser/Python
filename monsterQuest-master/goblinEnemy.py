#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
import random

class goblin(enemy):
    #initialize goblin
    def __init__(self, n, h):
        self.name = n
        self.health = h
        self.maxHealth = 100
        self.lvl = 1

    def __str__(self):
        return 'I am a Goblin named ' + self.name

    def getName(self):
        return self.name
    #different attack depending on the number
    def attack(self, other):
        #x = random.randint(1,2)
        #if x == 1:
            other.takeDamage(30)
        #else:
            #other.takeDamage(15)
    #return health
    def getHealth(self):
        return self.health

    #take damage when attacked
    def takeDamage(self, damage):
        self.health = self.health - damage
    #return goblin's max health
    def maxHealth(self):
        return self.maxHealth
    #can alter health if needed
    def setHealth(self, health):
        self.health = health
