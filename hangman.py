import random
import art
import wordlist

chosen_word = random.choice(wordlist.word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

print(art.title)

display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
     
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        if lives == 0:
          print ("You lose.")
          end_of_game = True

    if guess in display:
        print(f"You've already guessed {guess}.")
          
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print (art.stages[lives])