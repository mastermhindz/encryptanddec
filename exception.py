import random

try:
    print("Welcome to the Dice Game!")

    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")

    player1_score = 0
    player2_score = 0

    num_rounds = int(input("Enter the number of rounds to play: "))

    for round in range(1, num_rounds + 1):
        print("\nRound", round, "Starts!")

        player1_roll = random.randint(1, 6)  
        player2_roll = random.randint(1, 6)

        print(player1_name, "rolled a", player1_roll)
        print(player2_name, "rolled a", player2_roll)

        if player1_roll > player2_roll:
            player1_score += 1
            print(player1_name, "wins the round!")

        elif player1_roll < player2_roll:
            player2_score += 1
            print(player2_name, "wins the round!")

        else:
            print("It's a tie!")

    print("\nGame Over!\n")
    print(player1_name, "score:", player1_score)
    print(player2_name, "score:", player2_score)

    if player1_score > player2_score:
        print(player1_name, "wins the game!")
    elif player1_score < player2_score:
        print(player2_name, "wins the game!")
    else:
        print("It's a tie!")

except:
    print("An error occurred in the program.")