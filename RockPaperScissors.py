import random

options = ["Rock", "Paper", "Scissors"]

computer_pick = random.choice(options)

computer_wins = 0
user_wins = 0

while True:

    user_choice = int(input("Type 1 for Rock, 2 for Paper, 3 for Scissors: "))
    if user_choice == 1:
        print("You picked Rock")
    elif user_choice == 2:
        print("You picked Paper")
    elif user_choice == 3:
        print("You picked Scissors")
    else:
        print("Invalid prompt")
        continue

    print(f"Computer picked {computer_pick}")

    if user_choice == 0 and computer_pick[options]:
        print("It's a tie")
    elif user_choice == 1 and computer_pick == 'Paper':
        print("You lose")
        computer_wins +=1
    elif user_choice == 2 and computer_pick == 'Scissors':
        print("You lose")
        computer_wins += 1
    elif user_choice == 3 and computer_pick == 'Rock':
        print("You lose")
        computer_wins += 1
    elif user_choice == 1 and computer_pick == 'Rock':
        print("Tie")
        computer_wins += 1
    elif user_choice == 2 and computer_pick == 'Paper':
        print("Tie")
        computer_wins += 1
    elif user_choice == 3 and computer_pick == 'Scissors':
        print("Tie")
        computer_wins += 1
    else:
        print("You win")
        user_wins += 1

    if input("Do you want to play again? yes or no (y/n): ").lower() == 'y':
        continue
    else:
        break
print(f"Computer won {computer_wins} times.")
print(f"You won {user_wins} times")

