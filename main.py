def rps():
    """Ask players for their input."""
 
    player_one = input("Player 1, Please enter Rock, Paper, or Scissors: ")
    while player_one != "Rock" and player_one != "Paper" and player_one != "Scissors":
        player_one = input("Player 1, Please enter Rock, Paper, or Scissors: ")

    player_two = input("Player 2, Please enter Rock, Paper, or Scissors: ")
    while player_two != "Rock" and player_two != "Paper" and player_two != "Scissors":
        player_two = input("Player 2, Please enter Rock, Paper, or Scissors: ")

    return player_one, player_two


def compare(player_one, player_two):
    """Compares the player inputs."""

    if player_one == "Rock" and player_two == "Scissors":
       return print("Rock Beats Scissors! Player 1 Wins!")
    elif player_one == "Paper" and player_two == "Rock":
        print("Paper Beats Rock! Player 1 Wins!")
    elif player_one == "Scissors" and player_two == "Paper":
        print("Scissors Beat Paper! Player 1 Wins!")
    elif player_one == "Rock" and player_two == "Paper":
        print("Paper Beats Rock! Player 2 Wins!")
    elif player_one == "Paper" and player_two == "Scissors":
        print("Scissors Beats Paper! Player 2 Wins!")
    elif player_one == "Scissors" and player_two == "Rock":
        print("Rock Beats Scissors! Player 2 Wins!")
    else:
        print("It's a Draw!")


def again():
    play_again = input("Would you like to play again? y / n: ")
    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? y / n: ")
    if play_again == "y":
        results()
    else:
        exit

def results():
    player1, player2 = rps()
    compare(player1, player2)
    again()

results()