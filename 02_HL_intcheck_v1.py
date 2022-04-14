# HL component 1 - Get (and check) user input

# To Do
# Check a lowest is an integer
# Check that highest round is more than lowest
# Check that rounds is more than 1
# Check that guess is between lowest and highest

# Number checker goes here
def int_check(question, low = None, high = None):
    
    situation = ""

    if low is not None and high is not None:
        situation = "Both"

    elif low is not None and high is None:
        situation = "Low Only"
    
    while True:
        try:
            response = int(input(question))

            # checks input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please Enter a Number Between {} and {}".format(low, high))
                    continue

            elif situation == "low Only":
                if response < low:
                    print("Please Enter a Number That is More Than or Equal to {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please Enter an Integer")
            continue

# main routine

lowest = int_check("Lowest Number: ")
highest = int_check("Highest Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest) 