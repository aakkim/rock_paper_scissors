import random

def play():
    user = input("Choose one: 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if winner(user, computer):
        return "You won!"
    
    return "You lost!"

def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())