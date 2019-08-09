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
