import random, os
# TODO-1
from hangman_words import word_list
def clear():
    os.system("cls")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3
from hangman_art import logo
print(logo)

# testing code
# print(f'Pssst, the solution is {chosen_word}.')

# create blank
display = []
for _ in  range(word_length):
    display+="_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
# TODO-4
    if guess in display:
        print(f"You've already guessed {guess}")
    
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # TODO-5
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print(f"You lose. The answer is {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    # TODO-2
    from hangman_art import stages
    print(stages[lives])