import random

player_wins = 0
comp_wins = 0
print("")
print("")
print("Ok Let's get this match started!")
print("")
print("")
print("We'll play a quick game of Rock, Paper, Scissors")

def choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "s"
    else:
        print("I don't understand, pick again")
        choose_option()
    return user_choice

def comp_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = choose_option()
    comp_choice = comp_option()
    print("")

# Player VS Comp - ROCK
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose Rock, I chose Rock, we tied")

        elif comp_choice == "s":
            print("You chose Rock, I chose Scissor, You WIN!")
            player_wins += 1

        elif comp_choice == "p":
            print("You chose Rock, I chose paper, LOSER!")
            comp_wins += 1

    elif user_choice == "p":
        if comp_choice == "p":
            print("You chose Paper, I chose Paper, we tied")

        elif comp_choice == "r":
            print("You chose Paper, I chose Rock, You WIN!")
            player_wins += 1

        elif comp_choice == "s":
            print("You chose Paper, I chose Scissors, LOSER!")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "s":
            print("You chose Scissors, I chose Scissors, we tied")

        elif comp_choice == "r":
            print("You chose Scissors, I chose Rock, LOSER!")
            comp_wins += 1

        elif comp_choice == "p":
            print("You chose Scissors, I chose Paper, YOU WIN!")
            player_wins += 1

    print("")
    print("player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you dare play again! Y/N")
    if user_choice in ["y", "Y"]:
        pass
    elif user_choice in ["N", "n"]:
        breakpoint()
    else:
        breakpoint()


























