#This program will tell you the ingredients of given drinks or the drinks based on
#ingredients you ask for.

##The database of drinks and it's contents##

import time
drinks = {
    'martini':{'vodka','vermouth'},
    'black russian':{'vodka','kahlua'},
    'white russian':{'cream','kahlua','vodka'},
    'manhattan':{'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
    }

drink = ""
ingredient=""


##check if the drink is in the database##

def beverages():
    drink = input("insert the name of the alcoholic beverage:")
    if drink in drinks:
        print('The',drink,'is in our database')
        print('Here are the contents:',drinks[drink])
        time.sleep(2)
        ##print contents of input beverage if its in the db ##
    else:
        print('This drink is not in the database')
        beverages()
        
#beverages()

def by_ingredient():
    ingredient = input('Enter an ingredient:')
    for name,contents in drinks.items():
        if ingredient in contents:
            print(name)
            time.sleep(1)
            
    


#by_ingredient()#

    

def choose():
    choice=input('Search by beverage or ingredient?:')
    if choice == "beverage":
        beverages()
    elif choice == "ingredients" or "ingredient":
        by_ingredient()
choose()
