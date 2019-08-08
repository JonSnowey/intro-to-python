def software_sales():
    quantity = int(input('How many packages do you want to buy?'))
    package = 99
    

    if quantity == 10:
        discount = 20
    elif quantity <= 19:
        discount = 20
    elif quantity == 20:
        discount = 30
    elif quantity <= 49:
        discount = 30
    elif quantity == 50:
        discount = 50
    elif quantity <=99:
        discount = 50
    elif quantity >=100:
        discount = 50

    
    taken = package * discount /100
    total = package - discount

    print('The discount is %.0f' % taken,'percent')
    print('The total sum is $',total)

software_sales()
    
