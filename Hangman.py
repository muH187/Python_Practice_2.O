import random

words = ["COMPUTER", "SMARTPHONE"]

word = random.choice(words)

total_chances = 7
guessed_word = "-"*len(word)
print(f"The length of word is {len(word)}")

while total_chances != 0:
    print(guessed_word)

    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]

        if guessed_word==word:
            print("Congratulations You Won The Game")
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print(f"Your remaining chances: {total_chances}")

else:
    print("Game Over")
    print("You Lost")
    print("Your chances are exhausted")
print(f"The word is {word}")