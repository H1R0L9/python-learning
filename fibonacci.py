f = True
while f == True:
    number = input("How many terms do you want: ")
    try:
        number = int(number)
        if number < 0:
            print("Negative is no")
        elif number > 100000000:
            print("The number is too big!")
        else:
            f = False
    except:
        print("Invalid response")


a = 1
b = 1

for i in range(number):
    print(str(a) + " ")
    c = a + b
    a = b
    b = c
