import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list) - 1)]
word_length = len(chosen_word)
lives = 6

display = []
for char in chosen_word:
    display += '_'
print(display)

while "_" in display:
    if lives < 0:
        print(f"You lost. The word was \"{chosen_word}\".")
        break
    else:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f'You\'ve already guessed {guess}. Try again.')
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if guess == letter:
                    display[position] = letter
                    print(display)
            if guess not in chosen_word:
                print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
                print(hangman_art.stages[lives])
                lives -= 1
else:
    print('You win!')
