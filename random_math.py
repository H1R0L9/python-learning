import random

operator_list = ["+", "-", "*", "/"]
solutions = []
correct_ans = 0

print("Round off the decimals to 2 places if needed!")

for i in range(10):
    operation = operator_list[random.randint(0, 3)]
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    answer = input(str(a) + " " + operation + " " + str(b) + " = ")

    solution = int(round(eval(str(a) + operation + str(b)), 2))
    solutions.append(solution)

    if answer == str(solutions[i]):
        print("CORRECT")
        correct_ans += 1
    else:
        print("WRONG")


print("You got: " + str(correct_ans) + "/10 questions correct!")

if correct_ans == 10:
    print("Wow! You got all the questions correct!")

print("The solutions in order were:")
for i in range(len(solutions)):
    print(str(i+1) + ". " + str(solutions[i]))