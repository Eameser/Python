#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
import random

class hero(enemy):
    #instantiates hero, gives hero 10 fireballs, 6 potions, and takes off the shield
    def __init__(self, n, h):
        self.name = n
        self.maxHealth = 100
        self.health = h
        self.fireballs = 10
        self.potions = 6
        self.shield = False

    def __str__(self):
        return 'I am '+ self.name

    def getName(self):
        return self.name
    #turns off shield, attacks, subtracts one from total fireballs
    def fireballAttack(self, other):
        self.shield = False
        other.takeDamage(40)
        self.fireballs -= 1
    #turns off shield, heals hero, subtracts one from total potions
    def potionHeal(self):
        self.shield = False
        self.health = self.health + 25
        self.potions -= 1
    #activates shield
    def shieldd(self):
        self.shield = True

    #turns off shield, does 15 damage
    def attack(self, other):
        self.shield = False
        other.takeDamage(15)
    #returns current health of hero
    def getHealth(self):
        return self.health

    #takes damage, if shield is on, only take half damage
    def takeDamage(self, damage):
        if self.shield is True:
            self.health = self.health - (damage / 2)
        else:
            self.health = self.health - damage
    #returns number of potions left
    def getPotions(self):
        return self.potions
    #returns number of fireballs left
    def getFireballs(self):
        return self.fireballs
    #can set health i f needed
    def setHealth(self, h):
        self.health = h
    #returns max health
    def maxHealth(self):
        return self.maxHealth
