from words import words
from hangman_art import stages, intro, Game_over
import random

guessed_letter = []
blank_list = []
random_word = " "
total_life = 7
lost_life = 0


def blank_generator(random_word):
    for num in random_word:
        blank_list.append("_")


def display_blanks():
    for blank in blank_list:
        print(blank, end=" ")
    print("\n")


def check_guess(char_input):
    i = 0
    for letter in guessed_letter:
        if (letter == char_input):
            i += 1
    if i == 0:
        return False
    return True


def search_letter(char_input):
    index = 0
    s = 0
    for search in random_word:
        if (search == char_input):
            blank_list[index] = search
            s += 1
        index += 1
    if s == 0:
        return False
    else:
        return True


def blank_check():
    check = 0
    for blank in blank_list:
        if (blank == "_"):
            check += 1
    if check == 0:
        return False
    else:
        return True


print(intro)

random.shuffle(words)
random_word = random.choice(words)

blank_generator(random_word)
display_blanks()

while 1:
    char_input = input("Guess a letter: ").upper()
    is_already_guessed = check_guess(char_input)

    if not is_already_guessed:
        guessed_letter.append(char_input)
    else:
        print("Letter is already guessed \nSo try another one")
        continue
    search = search_letter(char_input)
    if search:
        display_blanks()
        check = blank_check()
        if not check:
            print("You WON ! Game Over ")
            break
    else:
        print("You guessed a wrong letter")
        total_life -= 1
        print(stages[7-total_life])
        if total_life == 0:
            print(Game_over)
            break

print(f"Orignal word was : {random_word}")
