#A monster battle , turn based , dmg randomly generated , attacks from a dictionary.
#User choses , shield , evade and attack.
#shiled raises defence , meaning dmg will take number of defence into consideration.
#evade random chance in evasion.
#attack random number of damage.

import time
import random

monster_health = 800

char_health = 500

defence = ''




def over():
    global char_health
    global monster_health
    if monster_health <= 0:
        print('You bested the monster!')
    elif char_health <= 0:
        print('The monster defeated you')



def battle():


    print( '------')
    print( 'o vv o')
    print('I    I')
    print( 'v----v')
    print('///////')
    print(monster_health,"/800")
    time.sleep(1)

battle()

def monster_attk():
    global char_health
    global monster_health
    monster = random.randint(0,200)
    print('The monster hits you for',monster,'points')
    char_health -= monster



def char_attk():
    global char_health
    char = random.randint(0,150)
    print('You hit the monster for',char,'points')
    global monster_health
    monster_health -= char
    ##print(monster_health)


def evade():
    evad = random.randint(1,2)
    if evad == 1:
        print('You evaded')
    elif evad == 2:
        print('You didnt evade')
        monster_attk()
        
def game():
    
    choose = input('1:attack 2:evade:')
    print("your health:",char_health,"/500")
    global monster_health
    while monster_health > 0 and char_health > 0:
            if choose == "1" or choose =="attack":
                char_attk()
                monster_attk()
                battle()
                game()
            elif choose =="2" or choose =="evade":
                evade()
                game()
                

game()
over()
