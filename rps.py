import random

game = True

while game == True:

    print("\nPick an option...")
    print("rock")
    print("paper")
    print("scissors")
    user_thing = input(": ")

    random_num = random.randint(1,3)

    if random_num == 1:
        computer_thing = "rock"
    elif random_num == 2:
        computer_thing = "paper"
    else:
        computer_thing = "scissors"

    if user_thing == "rock":
        if computer_thing == "rock":
            print("User picked rock, computer picked rock.  Try again...")
        elif computer_thing == "paper":
            print("Paper beats rock, you lose!")
            game = False
        else:
            print("Rock beats scissors, you win!")
            game = False
    elif user_thing == "paper":
        if computer_thing == "rock":
            print("Paper beats rock, you win!")
            game = False
        elif computer_thing == "paper":
            print("User picked paper, computer picked paper.  Try again...")
        else:
            print("Scissors beats paper, you lose!")
            game = False
    else:
        if computer_thing == "rock":
            print("Rock beats scissors, you lose!")
            game = False
        elif computer_thing == "paper":
            print("Scissors beats paper, you win!")
            game = False
        else:
            print("You picked scissors, computer picked scissors.  Try again...")