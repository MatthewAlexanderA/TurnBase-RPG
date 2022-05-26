class Character:

    def __init__(self, role, hp, atk, spd, heal):
        self.role = role
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.heal = heal
    
    def attack(self, enemy, enemyHp, score, playerAction):
        print("\nLoading.....")
        time.sleep(1)
        if self.spd > enemy.spd:
            heroSpd(self, enemy, enemyHp, score, playerAction)
            
        elif self.spd < enemy.spd:
            enemySpd(self, enemy, enemyHp, score, playerAction)

        else:
            sameSpd(self, enemy, enemyHp, score, playerAction)


#import time
import time
#import function randint
from random import randint


#Hero Stat
Knight = Character("Knight", 100, 65, 65, 25)
Archer = Character("Archer", 100, 55 ,70, 20)
Mage   = Character("Mage  ", 100, 70, 45, 30)
Priest = Character("Priest", 100, 45, 55, 50)

Hero = (Knight, Archer, Mage, Priest)

#Enemy Stat
Slime  = Character("Slime ", 100, 10, 50, 5)
Goblin = Character("Goblin", 130, 25, 70, 10)
Orc    = Character("Orc   ", 180, 35, 30, 20)
Demon  = Character("Demon ", 150, 40, 50, 25)

Enemy = (Slime, Goblin, Orc, Demon)


#if enemy speed > hero
def enemySpd(hero, enemy, enemyHp, score, playerAction):
    print("\n===================================================\n")

    rand = randint(1, 3)
    
    if rand == 1 or rand == 2:
        print(enemy.role + " attack " + hero.role)
        print(hero.role + " Recive: " + str(enemy.atk) + " Damage")
        hero.hp -= enemy.atk
        print(hero.role + " Hp: " + str(hero.hp))
    else:
        print(enemy.role + " use heal")
        print(enemy.role + " Recive: " + str(enemy.heal) + " Hp")
        enemyHp += enemy.heal
        print(enemy.role + " Hp: " + str(enemyHp))

    if hero.hp <= 0:
        end(hero, score, enemy)

    else:
        time.sleep(0.5)
        if playerAction == 1:
            print(hero.role + " attack " + enemy.role)
            print(enemy.role + " Recive: " + str(hero.atk) + " Damage")
            enemyHp -= hero.atk
            print(enemy.role + " Hp: " + str(enemyHp))
            print("\n")
        
        if playerAction == 2:
            print(hero.role + " use heal ")
            if hero.hp + hero.heal <= 100:
                print(hero.role + " Recive: " + str(hero.heal) + " Hp")
                hero.hp += hero.heal
                print(hero.role + " Hp: " + str(hero.hp))
                print("\n")
            elif(hero.hp + hero.heal > 100 and hero.hp + hero.heal < 100 + hero.heal):
                print(hero.role + " Restore Hp to 100 Hp")
                hero.hp = 100
                print("\n")
            else:
                print("Your Hp is Already Full")
                print(hero.role + " Hp: " + str(hero.hp))
                print("\n")
            
        if enemyHp <=0:
            score += 1
            powerUp(hero, score)
        else:
            action(hero, enemy, enemyHp, score)


#if hero speed > enemy
def heroSpd(hero, enemy, enemyHp, score, playerAction):
    print("\n===================================================\n")

    if playerAction == 1:
        print(hero.role + " attack " + enemy.role)
        print(enemy.role + " Recive: " + str(hero.atk) + " Damage")
        enemyHp -= hero.atk
        print(enemy.role + " Hp: " + str(enemyHp))
        print("\n")
        
    if playerAction == 2:
        print(hero.role + " use heal ")
        if hero.hp + hero.heal <= 100:
            print(hero.role + " Recive: " + str(hero.heal) + " Hp")
            hero.hp += hero.heal
            print(hero.role + " Hp: " + str(hero.hp))
            print("\n")
        elif(hero.hp + hero.heal > 100 and hero.hp + hero.heal < 100 + hero.heal):
            print(hero.role + " Restore Hp to 100 Hp")
            hero.hp = 100
            print("\n")
        else:
            print("Your Hp is Already Full")
            print(hero.role + " Hp: " + str(hero.hp))
            print("\n")

    if enemyHp <=0:
        score += 1
        powerUp(hero, score)

    else:
        time.sleep(0.5)
        rand = randint(1, 3)
    
        if rand == 1 or rand == 2:
            print(enemy.role + " attack " + hero.role)
            print(hero.role + " Recive: " + str(enemy.atk) + " Damage")
            hero.hp -= enemy.atk
            print(hero.role + " Hp: " + str(hero.hp))
        else:
            print(enemy.role + " use heal")
            print(enemy.role + " Recive: " + str(enemy.heal) + " Hp")
            enemyHp += enemy.heal
            print(enemy.role + " Hp: " + str(enemyHp))

        if hero.hp <= 0:
            end(hero, score, enemy)
        else:
            action(hero, enemy, enemyHp, score)

#if hero speed = enemy
def sameSpd(hero, enemy, enemyHp, score, playerAction):
    print("\n===================================================\n")

    if playerAction == 1:
        print(hero.role + " attack " + enemy.role)
        print(enemy.role + " Recive: " + str(hero.atk) + " Damage")
        enemyHp -= hero.atk
        print(enemy.role + " Hp: " + str(enemyHp))
        print("\n")
        
    if playerAction == 2:
        print(hero.role + " use heal ")
        if hero.hp + hero.heal <= 100:
            print(hero.role + " Recive: " + str(hero.heal) + " Hp")
            hero.hp += hero.heal
            print(hero.role + " Hp: " + str(hero.hp))
            print("\n")
        elif(hero.hp + hero.heal > 100 and hero.hp + hero.heal < 100 + hero.heal):
            print(hero.role + " Restore Hp to 100 Hp")
            hero.hp = 100
            print("\n")
        else:
            print(hero.role + " Hp is Already Full")
            print(hero.role + " Hp: " + str(hero.hp))
            print("\n")

    rand = randint(1, 3)

    if rand == 1 or rand == 2:
        print(enemy.role + " attack " + hero.role)
        print(hero.role + " Recive: " + str(enemy.atk) + " Damage")
        hero.hp -= enemy.atk
        print(hero.role + " Hp: " + str(hero.hp))
    else:
        print(enemy.role + " use heal")
        print(enemy.role + " Recive: " + str(enemy.heal) + " Hp")
        enemyHp += enemy.heal
        print(enemy.role + " Hp: " + str(enemyHp))


    if hero.hp <= 0 and enemyHp <= 0:
        score += 1
        end(hero, score, enemy)
    elif hero.hp <= 0:
        end(hero, score, enemy)
    elif enemyHp <=0:
        score += 1
        powerUp(hero, score)
    else:
        action(hero, enemy, enemyHp, score)

#pick random enemy
def pickEnemy(playerHero, score):
 
    rand = randint(1, 10)
    if rand == 1 or rand == 2 or rand == 3 or rand == 4:
        randEnemy = Enemy[0]
    elif rand == 5 or rand == 6 or rand == 7:
        randEnemy = Enemy[1]
    elif rand == 8 or rand == 9:
        randEnemy = Enemy[2]
    else:
        randEnemy = Enemy[3]
    enemyHp = randEnemy.hp
    playerHero = playerHero
    score = score
    action(playerHero, randEnemy, enemyHp, score)

#menu
def menu():
    print("\n============== Endless Quest ==============\n")
    print("\t\t 1. Start")
    print("\t\t 2. Quit")
    start = int(input("Your Option: "))

    if start == 1:
        choose()
    else:
        quit()

#choose hero
def choose():
    print("\n============== Choose your Hero ==============\n")
    print("    Hero  | HP  | Attack | Speed | Heal")

    for i in range(len(Hero)):
        print(str(i) + ". " + Hero[i].role + " | " + str(Hero[i].hp) + " |   " + str(Hero[i].atk) + "   |  " + str(Hero[i].spd) + "   |  " + str(Hero[i].heal))
        i += 1
    
    playerHero = int(input("Your Choose: "))

    if playerHero == 0:
        playerHero = Hero[0]
    elif playerHero == 1:
        playerHero = Hero[1]
    elif playerHero == 2:
        playerHero = Hero[2]
    elif playerHero == 3:
        playerHero = Hero[3]
    else:
        choose()
    score = 0
    pickEnemy(playerHero, score)

#action
def action(playerHero, randEnemy, enemyHp, score):
    print("\nLoading.....")
    time.sleep(1)

    score = score
    print("\n===================================================\n")
    print(str(playerHero.role) + " HP: " + str(playerHero.hp))
    print(str(randEnemy.role) + " HP: " + str(enemyHp))
    print("Your Score : " + str(score))
    print("\t       Choose Your Action:")
    print("\t\t  1. Attack (" + str(playerHero.atk) + " Damage)")
    print("\t\t  2. Heal (" + str(playerHero.heal) + " Damage)")
    playerAction = int(input("Your Action: "))
    if playerAction == 1:
        playerHero.attack(randEnemy, enemyHp, score, playerAction)
    elif playerAction == 2:
        playerHero.attack(randEnemy, enemyHp, score, playerAction)
    else:
        print("\n")
        print("Invalid Choice, please choose 1 or 2")
        action(playerHero, randEnemy, enemyHp, score)

#cek for power up(unfinish)
def powerUp(playerHero, score):
    if score % 3 == 0:
        print("\n===================================================\n")
        pickEnemy(playerHero, score)
    else:
        pickEnemy(playerHero, score)

#random power up (unfinish)

#end
def end(playerHero, score, randEnemy):
    print("\n===================================================\n")
    print(str(playerHero.role) + " has been Defeated by " + str(randEnemy.role))
    print("Your Score: " + str(score))
    new = input("\nPress Enter...")
    playerHero.hp = 100
    menu()


#Start Game
menu()