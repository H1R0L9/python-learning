f = True
while f == True:
    full_name = input("Please enter your full name: ")
    try:
        full_name = int(full_name)
        print("Invalid response")
    except:
        f = False

g = True
while g == True:
    gender = input("Please enter your gender [M/F]: ")
    try:
        gender = int(gender)
        print("Invalid response")
    except:
        if gender == 'm' or gender == 'M' or gender == 'f' or gender == 'F':
            g = False
        else:
            print("Invalid response")


if gender == 'f' or gender == 'F':
    m = True
    while m == True:
        married = input("Are you married? ")
        try:
            married = int(married)
            print("Invalid response")
        except:
            if married == 'y' or married == 'Y' or married == 'n' or married == 'N':
                m = False
            else:
                print("Invalid response")

if (gender == 'f' or gender == 'F') and (married == 'y' or married == 'Y'):
    print("Hello Missus " + full_name)
elif (gender == 'f' or gender == 'F') and (married == 'n' or married == 'N'):
    print("Hello Ms " + full_name)
elif gender == 'm' or gender == 'M':
    print("Hello Mr " + full_name)
