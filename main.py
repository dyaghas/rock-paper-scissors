def get_choices():
    player_choice = input("Choose rock, paper, scissors: ")
    computer_choice = "paper"
    choices = {"player": player_choice, "commputer": computer_choice}
    return choices


res = get_choices()
print(res)
