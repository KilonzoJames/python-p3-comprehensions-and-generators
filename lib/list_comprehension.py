#!/usr/bin/env python3
'''python-p3-comprehensions-and-generators'''

def return_evens(num_list):
    return_even=[n for n in num_list if n % 2 ==0]
    return return_even
numbers = [0, 1, 3, 5, 7, 8, 9]
print(return_evens(numbers))

def make_exclamation(sentence_list):
    list_with_exclamation=[n + '!' for n in sentence_list]
    return list_with_exclamation
sentence=["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentence))
