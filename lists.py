factorial = []

f = True
while f == True:
    number = input("Please enter a positive number: ")
    try:
        number = int(number)
        if number < 0:
            print("Invalid response")
        elif number > 100000:
            print("The number is too big!")
        else:
            f = False
    except:
        print("Invalid response")

for i in range(number):
    newnumber = number - i
    if newnumber > 0:
        factorial.append(newnumber)

result = 1
for i in factorial:
    result = result * i

print("The factorial of " + str(number) + " is: " + str(result))
