from wordle import Wordle
from colorama import Fore
import random


def main():
    word_set = load_word_set("words_database.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("\nType your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long" + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved: print("you've solved the puzzle")
    else: print(f"you failed to solved the puzzle,\nThe secret word was: ***{wordle.secret.upper()}***\n\n")

    command = input("Do you want to play again? (Y/N): ")
    if command == "Y": main()
    else: print("Goodbye!!!")



def display_results(wordle: Wordle):
    print("\nYour results so far...")

    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")



def load_word_set(path):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set



def convert_result_to_color(result):
    result_with_color = []
    for letter in result:
        if letter.is_in_position: color = Fore.GREEN
        elif letter.is_in_word: color = Fore.YELLOW
        else: color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)



def draw_border_around(lines, size = 9, pad = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘	"
    space = " " * pad

    print(top_border)
    for line in lines: print("│" + space + line + space + "│")
    print(bottom_border)



if __name__ == "__main__":
    print("Welcome User...!!!")
    main()