import random



def num_guess():
    while True:

        response = input("How Many Guesses Would You Like ")

        round_error = "Please type either <enter> or an integer more than 0"
        
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


# main routine
Intro = "Welcome to Higher Lower"
high = int(input("Highest Number? "))

rounds_played = 0
choose_instructions = "Pick a Number to Guess"

# generate integer
answer = random.randint(0, high)

# ask user for # number of rounds, <enter> for infinite mode
rounds = num_guess()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Easy Mode: Guess {}".format(rounds_played + 1)
    else:
        heading = "Guess {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = int(input("{} or Type '0' to Give Up: ".format(choose_instructions)))

    if choose == "0":
        break
    
    elif choose == answer:
        choose = "Correct"

    elif choose < answer:
        choose = "Higher"

    else:
        choose = "Lower"
    
    # rest of loop
    print("{}".format(choose))

    if choose == "Correct":
        break

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break
    
print("Thank you for playing")