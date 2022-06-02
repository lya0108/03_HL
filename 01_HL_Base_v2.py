from math import log2
from random import randint
import time
import math

# functions
def boundary_check(question, low=None, high=None, exit_code = None):
    
    situation = ""


    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:

        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please Enter a Number Between {} and {}".format(low, high))
                    continue

            elif situation == "low only":
                if response < low:
                    print("Please Enter a Number That is More Than or Equal to {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please Enter an Integer (ie: a Number Which Does Not Have a Decimal)")
            continue

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:
        
        # asks user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        print(error)
        print()

def decorator(text, decoration, lines):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print(decoration * text_length)
        print(statement)
        print(decoration * text_length)
        return ""

    elif lines == "2":
        print("|",statement,"|")

    elif lines == "1":
        print(statement)
        return ""

    else:
        return ""

# main routine
print("\x1b[38;2;0;255;255m")\

# lists of valid responses
yes_no_list = ["yes", "no"]
onetwo = ["1","2"]

# list to hold game history / summary
game_summary = []
already_guessed = []

# asks if the user has played before, if not shows instructions
decorator("Welcome to Higher Lower / Hot'N'Cold", "=", "2")
intro = choice_checker("Is This Your First Time Playing? ", yes_no_list, "Please Enter Yes(Y) or No(N)")
print()

if intro == "yes":
    decorator("How To Play", "=", "1")
    print()
    print("Choose Whether You Would Like To Choose The Highest Number\n\nThen Type [1] For Higher Lower Or [2] For Hot'N'Cold\nEach Round You Will Guess a Number")
    print()
    decorator("Rules For Higher Lower", "~", "1")
    print("Higher - The Number Is Higher")
    print("Lower - The Number Is Lower")
    print()
    decorator("Rules For Hot'N'Cold", "~", "1")
    print("Boiling - The Number Is Very Close")
    print("Warm - The Number Is Close")
    print("Luke-Warm - The Number Is slightly Close")
    print("Cold - The Number Is Far")
    print("Freezing - The Number Is Very Far")
    print()
    print("FYI: If You Don't Type a Number to Guess You Lose a Guess :^) (Not My Problem)")
    print()
    decorator("Good Luck", "=", "1")
    print()


# asks user if they want to choose their own numbers
custom_num = choice_checker("Would You Like to Choose The Highest Number? (The Default is 1 - 100) ", yes_no_list, "Please Type Yes(Y) or No(N)")
print()

# if 'yes' asks for the lowest and highest number then generates a secret number between them
if custom_num == "yes":
    bound_high = boundary_check("Highest Number? ", 2)
    # secret_num = randint(1, bound_high)

# if 'no' generates a secret number between 1 - 100
elif custom_num == "no":
    bound_high = 100
    # secret_num = randint(1, bound_high)

# asks user if they want 'higher lower' or 'hot'n'cold' then asks for number of guesses
mode = choice_checker("Please Type [1] For Higher Lower Or [2] For Hot'N'Cold ", onetwo, "Please Type Either [1] For Higher Lower Or [2] For Hot'N'Cold")
attempts = math.ceil(log2(bound_high))
attempts_used = 1
win = ""
bound_low = 1

end_game = "no"
while end_game == "no":
    
    if mode == "2":
        print()
        heading = decorator("Hot'N'Cold Guess {} of {}".format(attempts_used, attempts), "=", "1")
        print()

    else:
        print()
        heading = decorator("Higher Lower Guess {} of {}".format(attempts_used, attempts), "=", "1")
        print()

    print("Choose a Number Between {} and {}".format(bound_low, bound_high))

    choose = boundary_check("Pick a Number to Guess or Type 'exit' to Give Up: ", None, None, "exit")

    if choose in already_guessed:
        print("You Guessed This Number Already! Please Try Again\nYou Still Have {} Guesses Left".format(attempts - attempts_used))
        continue   

    already_guessed.append(choose)  
    
    # compare user guess with secret and give feedback
    if mode == "2": 

        if choose == "exit":
            result = "Gave Up"

        # user wins
        elif choose == secret_num:
            win = "w"
            attempts_used -= 1
            result = "Congratulations it Took You {} Guesses".format(attempts_used)
        
        # if guess is too low
        elif choose < bound_low:
            print("Please Choose a Number Higher Than {}".format(bound_low))
            result = "Number Too Low"
            attempts_used -= 1

        # boiling is very close to secret (within 5%)
        elif secret_num - (bound_high/20) < choose < secret_num + (bound_high/20):
            result = "Boiling"

        # warm is close to secret (within 10%)
        elif secret_num - (bound_high/10) < choose < secret_num + (bound_high/10):
            result = "Warm"
        
        # luke-warm is slightly close to secret (within 25%)
        elif secret_num - (bound_high/4) < choose < secret_num + (bound_high/4):
            result = "Luke-Warm"
        
        # cold is far from secret (within 50%)
        elif secret_num - (bound_high/2) < choose < secret_num + (bound_high/2):
            result = "Cold"

        # freezing is very far from secret (50% or more)
        elif bound_low <= choose <= bound_high:
            result = "Freezing"
        
        # if guess is too high
        else:
            print("Please Choose a Number Lower Than {}".format(bound_high))
            result = "Number Too High"
            attempts_used -= 1

    else:
        
        if choose == "exit":
            result = "Gave Up"        

        # user wins
        elif choose == secret_num:
            win = "w"
            result = "Congratulations it Took You {} Guesses".format(attempts_used)
        
        # if guess is too low
        elif choose < bound_low:
            print("Please Choose a Number Higher Than {}".format(bound_low))
            result = "Number Too Low"
            attempts_used -= 1
        
        # higher is below secret
        elif bound_low <= choose < secret_num:
            result = "Higher ↑"
            bound_low = choose

        # lower is above secret
        elif secret_num < choose <= bound_high:
            result = "Lower ↓"
            bound_high = choose
        
        # if guess is too high
        else:
            print("Please Choose a Number Lower Than {}".format(bound_high))
            result = "Number Too High"
            attempts_used -= 1
    
    # rest of loop
    outcome = "Guess {}: {} {}".format(attempts_used, choose, result)
    game_summary.append(outcome)
    
    attempts_used += 1

    print("{}".format(result))
    
    # end game if # of attempts used = attempts or user guesses the secret
    if win == "w" or attempts+1 == attempts_used or result == "Gave Up":
        break

# asks user if they wish to see their game history, if yes shows summary
if result == "Gave Up" and attempts_used == 1:
    print()

else:
    print()
    history = choice_checker("Would You Like To See Your Guess History? ",yes_no_list, "Please Type Yes(Y) Or No(N)")
    print()
    if history == "yes":
        for item in game_summary:
            print(item)
            print()

print()
decorator("Thank you for playing", "=", "2")
decorator("The Secret Number Was {}".format(secret_num), "=", "2")
print()
time.sleep(5)