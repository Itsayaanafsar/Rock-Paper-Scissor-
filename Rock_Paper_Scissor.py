import random

print("Welcome to Rock, Paper, Scissors!")
print("Best of three wins the game.")

emojis = {"rock": "🪨", "paper": "📃", "scissors": "✂"}
round_number = 0
player_score = 0
computer_score = 0
ties = 0

while True:
    round_number += 1
    print(f"Round {round_number}:")
    choice = input("Enter your choice (rock, paper or scissors): ").lower()

    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    print(f"You chose: {emojis[choice]}")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chose: ", emojis[computer_choice])
    if choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (
        (choice == 'rock' and computer_choice == 'scissors') or 
        (choice == 'paper' and computer_choice == 'rock') or 
        (choice == 'scissors' and computer_choice == 'paper')):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score => You: {player_score}, Computer: {computer_score} Ties: {ties}")

    if player_score == 2:
        print("================================================")
        print("-----Congratulations! You are the winner!-----")
        print("================================================")
        break
    elif computer_score == 2:
        print("================================================")
        print("-----Computer wins! Better luck next time-----")
        print("================================================")
        break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

