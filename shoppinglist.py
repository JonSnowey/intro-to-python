##shopping list

items = []

i = 0
while 1:
    i += 1
    item = input('Enter item %d: '%i)
    if item =='':
        break
    else:
        if item in items:
            print('Already on the list')
            items.remove(item)
    items.append(item)


    
print('Your items:',items)
##ticking off items off the list , it would be better to tick it by number? by its position in the set?


tick = input('name of item gotten:')
if tick in items:
    items.remove(tick)
    print('remaining:',items)
