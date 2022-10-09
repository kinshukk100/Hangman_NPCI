import csv
import random
import sys
import time
from functools import reduce

list_char = []
list_underscore = []
list_guess = []

def get_animal_list() -> list:
    animal_list = [[], [], []]
    file_easy = open("Animal_List(Easy).csv", "r")
    reader_easy = csv.reader(file_easy)
    file_medium = open("Animal_List(Medium).csv", "r")
    reader_medium = csv.reader(file_medium)
    file_hard = open("Animal_List(Hard).csv", "r")
    reader_hard = csv.reader(file_hard)
    for row in reader_easy:
        word = row[0].upper()
        animal_list[0].append(word)
    for row in reader_medium:
        word = row[0].upper()
        animal_list[1].append(word)
    for row in reader_hard:
        word = row[0].upper()
        animal_list[2].append(word)
    return animal_list


def get_flower_list() -> list:
    flower_list = [[], [], []]
    file_easy = open("Flowers_List(Easy).csv", "r")
    reader_easy = csv.reader(file_easy)
    file_medium = open("Flowers_List(Medium).csv", "r")
    reader_medium = csv.reader(file_medium)
    file_hard = open("Flowers_List(Hard) .csv", "r")
    reader_hard = csv.reader(file_hard)
    for row in reader_easy:
        word = row[0].upper()
        flower_list[0].append(word)
    for row in reader_medium:
        word = row[0].upper()
        flower_list[1].append(word)
    for row in reader_hard:
        word = row[0].upper()
        flower_list[2].append(word)
    return flower_list


def get_countries_list() -> list:
    countries_list = [[], [], []]
    file_easy = open("Easy_countries.csv", "r")
    reader_easy = csv.reader(file_easy)
    file_medium = open("medium_countries.csv", "r")
    reader_medium = csv.reader(file_medium)
    file_hard = open("Hard_countries.csv", "r")
    reader_hard = csv.reader(file_hard)
    for row in reader_easy:
        word = row[0].upper()
        countries_list[0].append(word)
    for row in reader_medium:
        word = row[0].upper()
        countries_list[1].append(word)
    for row in reader_hard:
        word = row[0].upper()
        countries_list[2].append(word)
    return countries_list


def hangman(count: int) -> None:
    if count == 1:

        print("   _ \n"
                    "  |  \n"
                    "  |  \n"
                    "  |  \n"
                    "  |  \n"
                    "  |  \n"
                    "  |  \n"
                    "|\n")
    elif count == 2:
        print("   _ \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "|\n")
    elif count == 3:
        print("   _ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "|\n")
    elif count == 4:
        print("   _ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "|\n")
    else:
        print("             __________ \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||     😣 \n"
                  "  ||    /|\ \n"
                  "  ||    / \ \n"
                  "  ||        \n"
                  "  ||        \n"
                  "______ \n"
                  "|    |\n")


def start_the_game(word: str, count: int, level) -> None:
    if count == 5:
        typewriter(f"The word is {word}. Better luck next Time \n")
        play_again = input("Do you want to play again Yes --> Y No --> N  ")
        play_again = play_again[0].upper()
        if play_again == "Y":
            start()
        return
    typewriter("Enter your guess -> ")
    char = input()
    char = char[0]
    if not char.isalpha():
        typewriter("Invalid Input, Try a letter \n")
        start_the_game(word, count, level)
        return
    char = char.upper()
    if char in list_guess:
        typewriter("You have already made this guess. Please make a different guess \n")
        start_the_game(word, count, level)
        return
    list_guess.append(char)
    if char not in word:
        count += 1
        hangman(count)
        g_word = "guesses"
        if count == 4:
            g_word = "guess"
        typewriter(f"Oops! Wrong guess. You have {5 - count} {g_word} remaining \n")
        start_the_game(word,count,level)
        return
    for i in range(len(list_char)):
        if char == list_char[i]:
            list_underscore[i] = char

    if "_" not in list_underscore:
        if level == "HARD":
            typewriter("You Won the Game!!! \n")
            return
        typewriter("Congrats! you have reached the next level\n ")
        if level == "EASY":
            level = "MEDIUM"
            list_underscore.clear()
            list_char.clear()
            list_guess.clear()
            load_the_game(level)
            return
        else:
            level = "HARD"
            list_underscore.clear()
            list_char.clear()
            load_the_game(level)
            list_guess.clear()
            return
    else:
        temp_word = "".join(list_underscore)
        print(temp_word)
        start_the_game(word, count, level)


def load_the_game(level: str) -> None:
    word_list = []
    index = random.choice([0, 1, 2])
    if level == "EASY":
        if index == 0:
            word_list = get_animal_list()[0]
        elif index == 1:
            word_list = get_countries_list()[0]
        else:
            word_list = get_flower_list()[0]
    elif level == "MEDIUM":
        if index == 0:
            word_list = get_animal_list()[1]
        elif index == 1:
            word_list = get_countries_list()[1]
        else:
            word_list = get_flower_list()[1]
    else:
        if index == 0:
            word_list = get_animal_list()[2]
        elif index == 1:
            word_list = get_countries_list()[2]
        else:
            word_list = get_flower_list()[2]
    word = random.choice(word_list)
    for char in word:
        list_underscore.append("_")
        list_char.append(char)
    print("The word is "+"".join(list_underscore))
    if index == 0:
        typewriter("The word is an animal type \n")
    elif index == 1:
        typewriter("The word is a country type \n")
    else:
        typewriter("The word is a sports type \n")
    start_the_game(word, 0,level)


def typewriter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.05)
        else:
            time.sleep(1)


def start() -> None:
    typewriter("Welcome to the Hangman Game! Please Enter your name -> ")
    name = input()
    typewriter(f"Hello {name.upper()} this game is in three levels Easy, Medium & Hard \n")
    time.sleep(1.5)
    typewriter(f"Lets just start with Easy one! All the best {name.upper()} \n")
    time.sleep(0.5)
    level = "EASY"
    load_the_game(level)


start()








