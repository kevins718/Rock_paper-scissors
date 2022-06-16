# Rock-paper-scissors game vs cpu

import random

print("Welcome to a game of Rock paper scissors!")


def play_game():
    user = input(
        "what is your choice?'r' for Rock, 'p' for paper,'s' for scissors\n")
    user = user.lower()
    choices = ['r', 's', 'p']

    computer = random.choice(['r', 'p', 's'])
    if user in choices:
        for i in user:
            if user == computer:
                print("Player {}: CPU {}. It's a tie.".format(user, computer))

            elif is_win(user, computer):
                print("Player {}: CPU {}. You won!".format(user, computer))
            else:
                print("Player {}: CPU {}. You lost!".format(user, computer))

    else:
        print("Error!Invalid choice!Enter a valid choice!!")
        play_game()


def is_win(player, opponent):
    # return true is the player beats opponent
    # winning conditions:r>s,s>p,p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play_game()
