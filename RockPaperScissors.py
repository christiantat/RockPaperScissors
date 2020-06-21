import random
import time

def setup():
    print("Rock")
    time.sleep(0.6)
    print("Paper")
    time.sleep(0.6)
    print("Scissor")
    time.sleep(0.6)
    print("Shoot!")
    time.sleep(0.6)


player_score = 0
computer_score = 0
moves = ["Rock", "Paper", "Scissor"]
print("Welcome to The Rock Paper Scissors Mega Large Championship of the World Galaxy Tournament")
print("Best two out of three. Let's do this.")
while player_score < 2 and computer_score < 2:
    player_move = input("Rock, Paper, or Scissors? ")
    player_move = player_move.lower()
    computer_move = random.choice(moves)
    computer_move = computer_move.lower()
    if player_move == "rock":
        setup()
        if computer_move == "rock":
            print("Opponent chose " + computer_move + ", it's a tie.")
        elif computer_move == "paper":
            computer_score += 1
            print("Opponent chose " + computer_move + ", you lose this round.")
        else:
            player_score += 1
            print("Opponent chose " + computer_move + ", you win this round!")
    elif player_move == "paper":
        setup()
        if computer_move == "rock":
            player_score += 1
            print("Opponent chose " + computer_move + ", you win this round!")
        elif computer_move == "paper":
            print("Opponent chose " + computer_move + ", it's a tie.")
        else:
            computer_score += 1
            print("Opponent chose " + computer_move + ", you lose this round")
    elif player_move == "scissors":
        setup()
        if computer_move == "rock":
            computer_score += 1
            print("Opponent chose " + computer_move + ", you lose this round")
        elif computer_move == "paper":
            player_score += 1
            print("Opponent chose " + computer_move + ", you win this round!")
        else:
            print("Opponent chose " + computer_move + ", it's a tie.")
    else:
        print("Please enter a valid move.")
    print("Your Score: " + str(player_score) + " - " + "Opponent Score: " + str(computer_score))
if player_score > computer_score:
    print("You Win!")
else:
    print("You lose.")
# Papi
