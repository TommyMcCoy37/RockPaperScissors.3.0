#Tommy McCoy
#Rock Paper Scissors
#Self-learn project
#05/02/2022

# Basic Paper Scissors Rock game (Vs. Computer, ver.3.0)

#adding random 
from random import randint

player_wins = 0
computer_wins = 0
winning_score = 5

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score {player_wins} Computer Score: {computer_wins}")
	print("Rock...")
	print("Paper...")
	print("Scissors...")

	#User input force to lower for no input error.
	player = input("Player, make your move: ").lower()
	if player == "quit" or player == "q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}.")

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			player_wins += 1
		elif computer == "paper":
			print("computer wins!")
			computer_wins += 1

	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			player_wins += 1
		elif computer == "scissors":
			print("computer wins!")
			computer_wins += 1

	elif player == "scissors":
		if computer == "paper":
			print("player wins!")
			player_wins += 1
		elif computer == "rock":
			print("computer wins!")
			computer_wins += 1
	else:
		print("Please enter a valid move.")


if player_wins > computer_wins:
	print("CONGRATS YOU WIN!!!")
elif player_wins == computer_wins:
	print("IT'S A TIE!")
else:
	print("OH NO, COMPUTER WINS...")
print(f"FINAL SCORES: Player: {player_wins} Computer Score: {computer_wins}")



