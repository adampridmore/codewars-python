# https://www.codewars.com/kata/5672a98bdbdd995fad00000f

# Rules of the "Rock, Paper, Scissors" game are:
#
# Rock beats Scissors,
# Scissors beat Paper,
# Paper beats Rock,
# Two identical moves are a draw.
# Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.

def game(p1, p2):
    if (p1 == p2): return 'Draw!'

    if (p1 == "rock" and p2 == "scissors"): return "Player 1 won!"
    if (p1 == "scissors" and p2 == "paper"): return "Player 1 won!"
    if (p1 == "paper" and p2 == "rock"): return "Player 1 won!"

    if (p2 == "rock" and p1 == "scissors"): return "Player 2 won!"
    if (p2 == "scissors" and p1 == "paper"): return "Player 2 won!"
    if (p2 == "paper" and p1 == "rock"): return "Player 2 won!"


print(game("rock", "paper"))

