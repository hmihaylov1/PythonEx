def wordCount(sentence):
    count = {}

    for word in sentence:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    most_frequent = max(count, key=count.get)

    return f'The count of every word is: {count} and the most frequent word is: {most_frequent}'
    # return count, most_frequent


def letterCount(word):
    count = {}

    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    return count


sent = input("Please give me a sentence: ").split()
wrd = input("give me a word please: ")

print(wordCount(sent))
# print(letterCount(wrd))
