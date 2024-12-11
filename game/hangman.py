# version 3 of hangman game

# import random library
import random

# make list by name word_list
word_list = ["aardvark", "baboon", "camel"]

# choose word in word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# print chosen_word by random
print(f"the chose word is-> {chosen_word}")

# put display variable and show to user how he/she has a gift(mistry)
display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# give guess user 
guess = input("Guess a word: ").lower()
      
      