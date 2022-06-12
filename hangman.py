import random

pl_list = ["python", "java", "swift", "javascript"]
print("H A N G M A N")

won = 0
lost = 0


def play():
    entered_letters = []
    rand_choice = list(random.choice(pl_list))
    invisible_state = list("-" * len(rand_choice))
    global lost
    global won
    i = 0
    print("".join(invisible_state))
    while i < 8:
        user_input = input("Input a letter: ")
        if len(user_input) != 1 or user_input.isspace():
            print("Please, input a single letter.")
        elif not user_input.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            entered_letters.append(user_input)
            if entered_letters.count(user_input) > 1:
                print("You've already guessed this letter.")
            elif user_input not in rand_choice:
                print("That letter doesn't appear in the word.")
                i += 1
        for j in range(len(rand_choice)):
            if user_input == rand_choice[j]:
                invisible_state[j] = user_input
        print()
        print("".join(invisible_state))
        if "-" not in invisible_state:
            print("You guessed the word " + "".join(invisible_state) + "!\nYou survived!")
            won += 1
            break
    else:
        print("You lost!")
        lost += 1


while True:
    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu_choice == "play":
        play()
    elif menu_choice == "results":
        print(f"You won: {won} times.\nYou lost: {lost} times.")
    elif menu_choice == "exit":
        break
