# version 1 of hangman game

# import random library
import random

# make list by name word_list
word_list = ["aardvark", "baboon", "camel"]

# choose word in word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
