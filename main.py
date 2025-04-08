player_one = input("Player 1, Please enter Rock, Paper, or Scissors: ")
while player_one != "Rock" and player_one != "Paper" and player_one != "Scissors":
    player_one = input("Player 1, Please enter Rock, Paper, or Scissors: ")

player_two = input("Player 2, Please enter Rock, Paper, or Scissors: ")
while player_two != "Rock" and player_two != "Paper" and player_two != "Scissors":
    player_two = input("Player 2, Please enter Rock, Paper, or Scissors: ")

if player_one == "Rock" and player_two == "Scissors":
    print("Player 1 Wins!")
elif player_one == "Paper" and player_two == "Rock":
    print("Player 1 Wins!")
elif player_one == "Scissors" and player_two == "Paper":
    print("player 1 Wins!")
elif player_one == "Rock" and player_two == "Paper":
    print("Player 2 Wins!")
elif player_one == "Paper" and player_two == "Scissors":
    print("Player 2 Wins!")
elif player_one == "Scissors" and player_two == "Rock":
    print("Player 2 Wins!")
else:
    print("It's a Draw!")