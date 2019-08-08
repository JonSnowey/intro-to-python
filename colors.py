def logging_in():
    password = "cat"
    username ="Melanie"
    email = "Melanie@email.com"
    code="123"
    new_pass=""
    updated_pass = new_pass

    print('Welcome to GuestBook')
    print("////////////////////")

    password = input("////Password:")
    username = input("////Username:")
    if password == "cat" and username == "Melanie":
        print("////Correct credentials")
        print("////////////////////")
    else:
        print("////////////////////")
        print("Username or password is incorrect")
        email = input("To reset your password enter your email:")
        if email == "Melanie@email.com":
            print("An email has been sent to your email with a code")
            code = input("Enter the code:")
            if code == "123":
                new_pass = input("Enter a new password:")
                print("Your password has been changed to",new_pass)
                print("To continue login with your new password")
                updated_pass =input("password:")
                if updated_pass == new_pass:
                    print("Correct password")
                else:
                    print('Incorrect password')
                
                 
        else:
            print("Incorrect email of the account")

        
              
            
            
            
logging_in()
        
