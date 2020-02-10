player_1 = input(" what do you want to chose rock, paper or scissors?")
player_2 = input(" what do you want to choose rock, paper or scissors?",)

def compare(p1, p2):

    if p1 == p2:
        return("it's the same")

    elif p1 == 'rock':
        if p2 == 'scissors':
            return("rock beats scissors!")
        else:
            return("try again!")

    elif p1 == 'scissors':
        if p2 == 'paper':
            return("scissors beats paper!")
        else:
            return("try again!")

    elif p1 == 'paper':
        if p2 == 'rock':
            return("paper beats rock!")
        else:
            return("try again!")

    else:
        return("Invalid ,try again.")

print(compare(player_1, player_2))