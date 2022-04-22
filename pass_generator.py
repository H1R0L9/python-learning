import random
import pyperclip
import string

password_characters = []
rand_list = [1,2,3]

def generate_password(length):
    print("Do you want punctuations included in your password? [y/n]")
    ans = input()
    if ans == "y":
        punctiations = True
    elif ans == "n":
        punctiations = False

    i = 0
    while i < length:
        if punctiations == False:
            password = random.choice(string.ascii_letters + string.digits)
        elif punctiations == True:
            password = random.choice(string.ascii_letters + string.digits + string.punctuation)
        password_characters.append(password)
        i+=1

def convert_to_string(list):
    pass_string = ""

    for i in list:
        pass_string += i 

    print("Would you like to paste your previous copy? [y/n]")
    ans = input()
    if ans =="y":
        print(pyperclip.paste())
    elif ans == "n":
        pass

    print("Password copied to your clipboard!")
    pyperclip.copy(pass_string)

    print("Would you like to paste the password? [y/n]")
    ans = input()
    if ans =="y":
        print(pyperclip.paste())
    elif ans == "n":
        pass

def main():
    true = True
    while true:
        try:
            pass_length = int(input("How many characters: "))
            true = False
        except:
            print("Input a number!")

    generate_password(pass_length)
    convert_to_string(password_characters)

main()