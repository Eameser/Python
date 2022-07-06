#Code created by Akash Patel CS-172-C Lab Section 069

from dragonEnemy import *
from goblinEnemy import *
from wolfEnemy import *
from zombieEnemy import *
from hero import *
import random
import sys
from git import *


fighterList = []
count = 0

move = []

def battle(h, mm):
    m = mm
    print('You have encountered ' + m.getName())
    #print hero's and monster's name and health
    print(h.getName() , ': ' , h.health , '/' , h.maxHealth , ' health')
    print(m.getName() + ':', str(m.health) + '/' + str(m.maxHealth) + ' health')
    #fight while both sides still have health, end when one's health hits 0
    while(h.health > 0 and m.health > 0):
        print('Remaining:', h.getFireballs(), 'Fireballs', h.getPotions(), 'Potions')
        #print(h.health, hero.health)
        command = input('Enter command: q - Sword / w - Shield / e - Fireball / r - Potion / t - Exit \n')
        #uses sword attack
        if(command.lower() == 'q'):
            move.append('q')
            print('Sword Attack!')
            h.attack(m)
            #checks if monster is still alive after the hero attacks. If the monster is dead, break the loop and move to the next monster. Else, keep going
            if(m.health <= 0):
                m.setHealth(0)
                print(h.getName(), 'defeated', m.getName())
                break
            print(m.getName() + ' attacks you! ')
            m.attack(h)
        if(command.lower() == 'w'):
            move.append('w')
            print('Shield!')
            h.shieldd()
            print(m.getName() + ' attacks you! ')
            m.attack(h)
        #make sure user has fireballs before attacking. If there are no fireballs, user loses the turn and is notified. Else, attacks
        if(command.lower() == 'e'):
            move.append('e')
            print('Fireball Attack!')
            if(h.getFireballs() == 0):
                print('No fireballs left!')
            else:
                h.fireballAttack(m)
            #checks if monster is still alive after the hero attacks. If the monster is dead, break the loop and move to the next monster. Else, keep going
            if(m.health <= 0):
                m.setHealth(0)
                print(h.getName(), 'defeated ', m.getName())
                break
            print(m.getName() + ' attacks you! ')
            m.attack(h)
        #make sure user is in a condition to use potion, if they are, use it. if not, turn is lost and user is notified
        if(command.lower() == 'r'):
            move.append('r')
            print('Potion!')
            if(h.getPotions() == 0):
                print('No Potions Left!')
            elif(h.health == h.maxHealth):
                print('Already at Full Health!')
            else:
                h.potionHeal()
            print(m.getName() + ' attacks you! ')
            m.attack(h)
        #if user enters exit, exit
        if(command.lower() == 't'):
            print('Thanks for playing!')
            sys.exit()

        if(command.lower() == 'enms'):
            global fighterList
            for e in fighterList:
                print(e.name, ": ", e.health)
            #print(m.name, m.health)

        if(command.lower() == 'hr'):
            global hero1
            print(h.name, ": ", h.health)
            print(hero1.name, hero1.health)

# git part
        if command.lower() == "git" or command.lower() == "GIT":
            while True:
                git.git_menu()
                i = int(input("Choose command: "))
                if i == 6:
                    game = []
                    game.append(move)
                    our_hero = {"name": h.name,
                                    "maxHealth": 100,
                                    "health": h.health,
                                    "fireballs": h.fireballs,
                                    "potions": h.potions,
                                    "shield": h.shield}
                    game.append(our_hero)
                    #global fighterList
                    for en in fighterList:
                        game.append({"name": en.name,
                                        "maxHealth": 100,
                                        "health": en.health,
                                        "lvl": en.lvl})

                    git.git_command(i)(game)
                elif i == 9:
                    break
                elif i == 8:
                    com_game = git.curr_branch.load_commit()
                    h = hero(com_game[1]["name"], com_game[1]["health"])
                    h.fireballs = com_game[1]["fireballs"]
                    h.potions = com_game[1]["potions"]
                    h.shield = com_game[1]["shield"]
                    hero1 = h
                    #global fighterList
                    fighterList.clear()

                    enms = com_game[2:]
                    for enm in enms:
                        if enm["lvl"] == 1:
                            fighterList.append(goblin(enm["name"], enm["health"]))
                        if enm["lvl"] == 2:
                            fighterList.append(wolf(enm["name"], enm["health"]))
                        if enm["lvl"] == 3:
                            fighterList.append(zombie(enm["name"], enm["health"]))
                        if enm["lvl"] == 4:
                            fighterList.append(dragon(enm["name"], enm["health"]))
                    m = fighterList[0]

                else:
                    git.git_command(i)()
        #if hero's health falls below 0, set it to 0, display hero's health and monster's health, exit since hero lost
        if(h.health <= 0):
            h.setHealth(0)
            print(h.getName(), 'was defeated by', m.getName())
            print(h.getName() + ':', str(h.health) + '/' + str(h.maxHealth))
            print(m.getName() + ':', str(m.health) + '/' + str(m.maxHealth))
            sys.exit()

        #display hero's and enemy's health after each turn
        print(h.getName() + ':', str(h.health) + '/' + str(h.maxHealth))
        print(m.getName() + ':', str(m.health) + '/' + str(m.maxHealth))
if __name__ == '__main__':
    #global fighterList
    fighterList = []
    git = Git()
    print("\nWelcome to Adventure Battle!")
    heroName = input('What is the name of your hero? ')
    if heroName.lower() == 'exit':
        sys.exit()
    #instantiate a hero with the given name and 100 health
    hero1 = hero(heroName, 100)
    #ask for how many enemies the hero wants to fight
    fighters = input('How many enemies will ' + heroName + ' battle? (enter 1 - 4)')
    valid = False
    if fighters.lower() == 'exit':
        sys.exit()
    else:
        while valid is False:
            try:
                fighters = int(fighters)
                valid = True
            except:
                print('Please Enter a Valid Input')
                fighters = input('How many enemies will ' + heroName + ' battle? ')

    #instantiate the monsters
    wolf1 = wolf('Baxter the Wolf', 100)
    dragon1 = dragon('Drogon the Dragon', 100)
    goblin1 = goblin('Gerald the Goblin', 100)
    zombie1 = zombie('Zeus the King Zombie', 100)
    #create a list of the monsters then shuffle it to add randomness
    list = [wolf1, dragon1, goblin1, zombie1]
    random.seed(0)
    random.shuffle(list)
    for x in range(fighters):
        fighterList += [list[x]]
    #global count
    count = len(fighterList)
    x = 0
    while x <= count:
        print('\n')
        battle(hero1, fighterList[x])
        if count != len(fighterList):
            count = len(fighterList)
            x = 0
            continue
        x += 1

    print('You have defeated all of the enemies in the world!')
