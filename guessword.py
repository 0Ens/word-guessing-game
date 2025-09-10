import random

print("Welcome to Guess the Word!")

word_pool = ["cat", "budget", "border", "freight", "import", "clock", "artificial", "linger", "hut", "dangerous", "skeleton", "treatment"]

chosen_word = random.choice(word_pool)

guesses = ''
attempts = 10

while attempts > 0:
    failed = 0
    for char in chosen_word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    print()
    
    if failed == 0:
        print("Congratulations! You've guessed the word correctly!")
        break
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue
    
    if guess in guesses:
        print("You've already guessed that letter. Try again.")
        continue
    
    guesses += guess
    
    if guess not in chosen_word:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")
        if attempts == 0:
            print(f"You've run out of attempts. The word was '{chosen_word}'.")
            break