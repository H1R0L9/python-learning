from os import remove
from signal import set_wakeup_fd


sequence = [1,1]

def fibonnaci():
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

    if number == 0:
        print([])
    elif number == 1:
        print([1])
    else:
        for i in range(number - 2):
            sequence.append(sequence[i] + sequence[i+1])

    print(sequence)

def remove_odd():
    for i in sequence:
        if i%2 != 0:
            sequence.remove(i)
    print(sequence)

fibonnaci()
remove_odd()