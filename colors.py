import random
import string

def code_generator(size=6,chars = string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars)for _ in range(size))
code_generator()


def logging_in():
    password = "cat"
    username ="Melanie"
    email = "Melanie@email.com"
    code= code_generator()
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
            print(code_generator())
            code = input("Enter the code:")
            if code == code:
                new_pass = input("Enter a new password:")
                print("Your password has been changed to",new_pass)
                print("To continue login with your new password")
                updated_pass =input("password:")
                if updated_pass == new_pass:
                    print("Correct password")
                    new_pass == password
        
                else:
                    print('Incorrect password')
        else:
            print("Incorrect email of the account")
logging_in()
        
