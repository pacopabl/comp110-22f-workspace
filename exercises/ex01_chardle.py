"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730524864"

num_of_var: int = 0

word_guess: str = input("Enter a 5-character word: ")
if len(word_guess) != 5:
    print("Error: Word must contain 5 characters") + exit()

letter_guess: str = input("Enter a single character: ")
if len(letter_guess) != 1:
    print("Error: Character must be a single character. ") + exit()

print("Searching for " + letter_guess +  " in " + word_guess)
if letter_guess == word_guess[0]:    
    print(letter_guess + " found at index 0" )
    num_of_var = num_of_var + 1
if letter_guess == word_guess[1]:    
    print(letter_guess + " found at index 1" )
    num_of_var = num_of_var + 1
if letter_guess == word_guess[2]:    
    print(letter_guess + " found at index 2" )
    num_of_var = num_of_var + 1
if letter_guess == word_guess[3]:    
    print(letter_guess + " found at index 3" )
    num_of_var = num_of_var + 1
if letter_guess == word_guess[4]:    
    print(letter_guess + " found at index 4" )
    num_of_var = num_of_var + 1

if num_of_var == 0:
    print("No instances of " + letter_guess + " found in " + word_guess)
if num_of_var == 1: 
        print(str(num_of_var) + " instance of " + letter_guess + " found in " + word_guess)
if num_of_var > 1:
        print(str(num_of_var) + " instances of " + letter_guess + " found in " + word_guess)

