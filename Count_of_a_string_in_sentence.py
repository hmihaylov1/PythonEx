# def string_app(sentence):
#     print("Sentence given: ", sentence)
#
#     count = sentence.count("Emma")
#     print("Times the word 'Emma' appeared in the given sentence: ", count)
#
# sent = input("Give a sentence to count words: ")
#
# string_app(sent)

from collections import Counter
import re

def string_app(sentence):
    print("Sentence given:", sentence)

    # Convert sentence to lowercase and use regex to find words
    words = re.findall(r'\b\w+\b', sentence.lower())

    # Use Counter to count occurrences of each word
    word_counts = Counter(words)

    # Find the most common word and its count
    most_common_word, count = word_counts.most_common(1)[0]

    print(f"Most common word: '{most_common_word}'")
    print(f"Times the word '{most_common_word}' appeared in the given sentence: {count}")

# Input sentence
sent = input("Give a sentence to count words: ")

# Call the function
string_app(sent)
