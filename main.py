import random


def get_choices():

    wins = 0
    losses = 0
    carry_on = 1

    while carry_on == 1:

        possible_movements = ["rock", "paper", "scissors"]
        computer_choice = random.choice(possible_movements)
        player_choice = input("Choose rock, paper, scissors: ")
        choices = {"player": player_choice, "computer": computer_choice}

        if player_choice in possible_movements:

            print("player choice: " + choices.get("player") + "\ncomputer choice: " + choices.get("computer"))

            if choices.get("player") == "paper" and choices.get("computer") == "rock":
                wins += 1
                print("You won!")

            elif choices.get("player") == "rock" and choices.get("computer") == "scissors":
                wins += 1
                print("You won!")

            elif choices.get("player") == "scissors" and choices.get("computer") == "paper":
                wins += 1
                print("You won!")

            else:
                losses += 1
                print("you lost")

            scoreboard = "scoreboard: {} / {}".format(wins, losses)
            print(scoreboard)

        else:
            print("Type a valid option")

        continue_choice = input("Do you want to play another round? yes / no \n")

        if continue_choice == "yes":
            carry_on = 1
        else:
            carry_on = 0


get_choices()
