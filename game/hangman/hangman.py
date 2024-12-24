# import random library
import random
import hangman_art 
# make list by name word_list
word_list = ["aardvark", "baboon", "camel"]
# Set 'lives' to equal 4.
lives = 4
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

# letters input() the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while end_of_game == False:
    # give guess user 
    guess = input("Guess a word: ").lower()
        
    # check guess user in chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

        # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "you lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        print(lives)
        if lives == 0:
            print("You lose!")
            break
    
    if "_" not in display:
        end_of_game = True
        print("You win!")