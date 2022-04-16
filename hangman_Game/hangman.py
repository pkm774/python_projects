
import random
import hangman_art as ha
import hangman_words as hw

end_of_game = False
lives = 6

print(ha.logo)
print("You have total 6 lives")

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("You Guessed a right Letter")

    # Join all the elements in the list and turn it into a String.
    print(f"\nWord = {' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou won this challenge, CONGRATS !.")

    # Check if user is wrong.
    if guess not in chosen_word:
        print("Your guessed letter is wrong,")
        lives -= 1
        print(ha.stages[lives])
        if lives == 0:
            end_of_game = True
            print("\nYou lost this challenge.")
        else:
            print(f'{guess} is not present in the Word, You loose 1 life,')
            print(f'You have {lives} lives left.')
