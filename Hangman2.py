import random

options = ["ALI", "MIRZA", "BILAL", "AISHA", "UMER"]

option = random.choice(options)
print(f"The length of word is {len(option)}")
guessed_word = '-'*len(option)
total_chances = 7

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()

    if letter in option:
        for char in range(len(option)):
            if letter == option[char]:
                guessed_word = guessed_word[:char] + letter + guessed_word[char+1:]

        if option == guessed_word:
            print("Congratulations You Won:")
            break
    else:
        total_chances -= 1
        print("Incorrect")
        print("Your remaining chances:", total_chances)
else:
    print("Game Over")
    print("Your all chances are exhausted")
print("The word is", option)
