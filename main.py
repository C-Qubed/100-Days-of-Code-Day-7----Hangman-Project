#Step 1 
import random
import hangman_art
import hangman_words

# variables
lives = 6

chosen_word = random.choice(hangman_words.word_list)

# Initial UI
display = []
guessed_letters = []
word_length = len(chosen_word)

for letter in range(word_length):
    display.append('_')

print(hangman_art.logo)
print(display)

# Play the game
end_of_game = False

while not end_of_game:
    guess = input('Choose a letter: ').lower()

    # Improving User Experience
    guessed_letters.append(guess)
    print(f'\nYou\'ve guessed the letters {guessed_letters}.')
    if guess in display:
        print('You\'ve already guessed that letter.')
    
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter
            'Nice job!'
    
    # Check if user is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f'\nSorry, {guess} is not in the word.')

    

        
    # Update UI
    i = lives
    print(hangman_art.stages[i])
    print(display)

    # check if game should end
    if '_' not in display:
        print('You win!')
        end_of_game = True

    if lives == 0:
        print('\nYou lose...')
        print(f'\nThe correct answer was {chosen_word}')
        end_of_game = True

    # ------------------------------------
        

