import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
num_rounds = int(input("Enter the number of rounds (3 or 5): "))

while True:
    print("Enter your choice (rock, paper, scissors) or 'exit' to quit:")
    player_choice = input().lower()

    if player_choice == 'exit':
        print("Exiting...")
        break

    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        player_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("Computer wins!")

    """Check for early win condition"""
    if (player_score >= 2 and num_rounds == 3) or (player_score >= 3 and num_rounds == 5):
        print(f"You won  {player_score}  to  {computer_score}!")
        break
    elif computer_score >= 2 and num_rounds == 3 or (computer_score >= 3 and num_rounds == 5):
        print(f"Computer won  {computer_score}  to  {player_score}!")
        break

if player_score == computer_score:
    print(f"It's a draw! {player_score} to {computer_score}")