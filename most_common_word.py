def most_common_word(sentence):
    common_word = {}

    for word in sentence:
        if word in common_word:
            common_word[word] += 1
        else:
            common_word[word] = 1

    most_common = max(common_word, key=common_word.get)

    return f'Most common word is: {most_common}'


sent = input("What is the sentence?: ").split()

print(most_common_word(sent))
