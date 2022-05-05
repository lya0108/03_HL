import time
# HL component 1 - Get (and check) user input
print("\x1b[38;2;0;255;255m")
# To Do
# Check a lowest is an integer
# Check that highest round is more than lowest
# Check that rounds is more than 1
# Check that guess is between lowest and highest

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


# Number checker goes here
def int_check(question, low=None, high=None):
    
    situation = ""

    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:
        try:
            response = int(input(question))

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
            print("Please Enter an Integer (ie: a number which does not have a decimal)")
            continue

# main routine

lowest = int_check("Lowest Number: ")
highest = int_check("Highest Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1, highest)
print("i'll give you 1 round")
print()
guess = int_check("Guess: ", lowest, highest) 
print("LOADING...")
time.sleep(3)
print("HOLD ON...")
time.sleep(3)
print("IM WORKING ON IT...")
time.sleep(3)
print("WAIT A MINUTE...")
time.sleep(5)
number = int(input("WAIT WHAT NUMBER DID YOU SAY"))
print("LOADING...")
time.sleep(number)
print("HOLD ON...")
time.sleep(3)
print("IM WORKING ON IT...")
time.sleep(3)
print("I'M GETTTING CLOSE...")
time.sleep(5)
this_your_num = input("IS THIS YOUR NUMBER [{}] ".format(number))
