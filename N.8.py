print("This is a classic Rock-Paper-Scissor game. You just have to write: Rock, Paper, Scissor")

# define the choice of the two players

continue_playing = "yes"
while continue_playing.lower() == "yes":
    player_1_choice = input("Player 1, please, make your choice: ")
    player_2_choice = input("Player 2, please, make your choice: ")
    if player_1_choice.lower() == "rock":
        if player_2_choice.lower() == "paper":
            print("Congratulation Player 2! You won!")
        elif player_2_choice.lower() == "scissor":
            print("Congratulation Player 1! You won!")
        else:
            break
    elif player_1_choice.lower() == "paper":
        if player_2_choice == "rock":
            print("Congratulation Player 1! You won!")
        elif player_2_choice.lower() == "scissor":
            print("Congratulation Player 2! You won!")
        else:
            break
    elif player_1_choice.lower() == "scissor":
        if player_2_choice == "rock":
            print("Congratulation Player 2! You won!")
        elif player_2_choice.lower() == "scissor":
            print("Congratulation Player 1! You won!")
        else:
            break
    continue_playing = input("Do you want to play again? ")
print("The game has ended!")
