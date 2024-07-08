word = input('Enter a word please: ')
print("You entered the word: ", word)

size = len(word)

for i in range (0, size - 1, 2):
    print("index [", i, "]", word[i])