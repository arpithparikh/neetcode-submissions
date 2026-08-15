from typing import List

# Get word length
def get_word_length(word: str) -> int:
    return len(word)

#Sort words
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words

#Sort numbers
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=abs)
    return numbers

# Do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
