import random
import copy


def game(turns, sequence_start):
    t = 0
    while t < turns:
        print(f"Turn {t + 1}")
        guess = [x.upper() for x in list(input("Enter your guess: "))]

        sequence = copy.deepcopy(sequence_start)
        correct_place = 0
        incorrect_place = 0
        x = 0
        y = 0

        if len(guess) == 4:
            while x < len(guess):
                if guess[x] == sequence[y]:
                    correct_place += 1
                    guess.pop(x)
                    sequence.pop(y)
                else:
                    x += 1
                    y += 1

            for remaining in guess:
                if remaining in sequence:
                    incorrect_place += 1

            if correct_place == 4:
                print("You win!\n")
                break
            else:
                print(
                    f"You have {correct_place} colors placed correctly and {incorrect_place} correct colors place incorrectly.")
                t += 1
        else:
            print("Please type a 4-letter sequence without spaces.")

        if t == turns:
            print("You lose!")
            print("The correct sequence was: ", "".join(sequence_start), "\n")


def main():
    colors = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
    difs = ['Easy (20 turns)', 'Medium (10 turns)', 'Hard: (5 Turns)']

    print("Welcome to Command-Line Mastermind!")
    print(
        "Rules: You have 7 colors available: Red, Orange, Yellow, Green, Blue, Indigo, Violet. Each is represented by its first letter.\nType your 4-letter guess without spaces, and see if you can guess the correct sequence in the number of turns given!")

    while True:
        new_game = input("Play a new game? (Y | y): ")

        if new_game.lower() == 'y':
            for num, dif in enumerate(difs):
                print(f"{num + 1}: {dif}")
            difficulty = int(input("Select Difficulty: "))
            sequence_to_guess = random.choices(colors, k=4)
        else:
            break

        if difficulty == 1:
            game(20, sequence_to_guess)
        elif difficulty == 2:
            game(10, sequence_to_guess)
        elif difficulty == 3:
            game(5, sequence_to_guess)
        else:
            print("Invalid input.")


main()
