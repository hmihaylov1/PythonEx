def sort_word(word):
    sorted_word = ''.join(sorted(word))
    length_word = len(word)
    return sorted_word, length_word


word_to_sort = "Hristiyan"


def commonWord(sentence):
    common = {}

    for word in sentence:
        if word in common:
            common[word] += 1
        else:
            common[word] = 1

    most_common = max(common, key=common.get)

    return most_common


def remove_char(word, num):
    num = int(num)
    n = word[num:]

    return n


input_word = input("what is the word?: ")
input_num = input("How many letters do you want to delete?: ")
sent = input("What is the Sentence: ").split()


print(remove_char(input_word, input_num))
print(sort_word(word_to_sort))
print(commonWord(sent))

