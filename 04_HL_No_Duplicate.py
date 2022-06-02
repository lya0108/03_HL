secret_num = 7
attempts = 5

already_guessed = []
guesses_left = attempts
choose = ""

while choose != secret_num and guesses_left >= 1:

    choose = int(input("Guess: "))

    if choose in already_guessed:
        print("You Guessed This Number Already! Please Try Again\nYou Still Have {} Guesses Left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(choose)

    if guesses_left >= 1:

        if choose < secret_num:
            print("Too Low, Try A Higher Number. Guesses Left: {}".format(guesses_left))

        elif choose > secret_num:
            print("Too High, Try A Lower Number. Guesses Left: {}".format(guesses_left))

    else:
        if choose < secret_num:
            print("Too Low")

        elif choose > secret_num:
            print("Too High")

if choose == secret_num:
    if guesses_left == attempts:
        print("Nice Guess!")
    else:
        print("Well Done!")