text = input("Please enter the text: ").replace('.', '')
print(text)
words = text.split(' ')
word_dictionary = {}

for i in words:
    if i in word_dictionary:
        word_dictionary[i] += 1
    else:
        word_dictionary[i] = 1

print(word_dictionary)
