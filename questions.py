Ada_Lovelace = 0
Frieda_Kahlo = 0
Abraham_Lincoln = 0
Moe_Howard = 0

print('Which famous historical figure are you? Answer the questions below to find out!')
player_input = input('Hit enter to begin!')

print('I would rather...')
print('a) Do something brand new')
print('b) Improve something that already exists')
player_input = input('Your answer: ')
if player_input == 'a':
    Ada_Lovelace += 1
elif player_input == 'b':
    Frieda_Kahlo += 1
    Abraham_Lincoln += 1
else:
    Moe_Howard += 1


print('My idea of fun is...')
print('a) Spending time with friends')
print('b) Creating art')
print('c) Learning something new')
player_input = input('Your answer: ')
if player_input == 'a':
    Abraham_Lincoln += 1
elif player_input == 'b':
    Frieda_Kahlo += 1
elif player_input == 'c':
    Ada_Lovelace += 1
else:
    Moe_Howard += 1

print('Of the following, my favorite class is...')
print('a) English')
print('b) Math')
print('c) Art')
player_input = input('Your answer: ')
if player_input == 'a':
    Abraham_Lincoln += 1
elif player_input == 'b':
    Ada_Lovelace += 1
elif player_input == 'c':
    Frieda_Kahlo += 1
else:
    Moe_Howard += 1

print('--YOUR HISTORICAL FIGURE--')
print('Your final scores:')
print('Abraham Lincoln: ' + str(Abraham_Lincoln))
print('Ada Lovelace: ' + str(Ada_Lovelace))
print('Frida Kahlo: ' + str(Frieda_Kahlo))

if Frieda_Kahlo > Ada_Lovelace and Frieda_Kahlo > Abraham_Lincoln and Frieda_Kahlo > Moe_Howard:
    print('You are Frieda Kahlo!')
elif Abraham_Lincoln > Ada_Lovelace and Abraham_Lincoln > Frieda_Kahlo and Abraham_Lincoln > Moe_Howard:
    print('You are Abraham Lincoln!')
elif Ada_Lovelace > Abraham_Lincoln and Ada_Lovelace > Frieda_Kahlo and Ada_Lovelace > Moe_Howard:
    print('You are Ada Lovelace!')
else:
    print("Alright wise guy, you're Moe Howard!")