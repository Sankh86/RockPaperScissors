import random

while True:
    playerHand = input("Choose Rock, Paper, or Scissors? (q to quit)  ")

    if playerHand.upper() == "Q" or playerHand.upper() == "QUIT":
        break

    if playerHand.upper() == "ROCK" or playerHand.upper() == "PAPER" or playerHand.upper() == "SCISSORS":

        pcHand = random.choice(["Rock", "Paper", "Scissors"])
        print("I throw " + pcHand)

        if pcHand.upper() == playerHand.upper():
            print("We tied!")
        elif (  (pcHand == "Rock" and playerHand.upper() == "PAPER") or
                (pcHand == "Paper" and playerHand.upper() == "SCISSORS") or
                (pcHand == "Scissors" and playerHand.upper() == "ROCK")):
            print("You Won!")
        else:
            print("You Lose!")
    else:
        print("Invalid choice, try again...")