import csv
import random
import sys
import time
from functools import reduce
from gtts import gTTS
import playsound

list_char = []
list_underscore = []
list_guess = []
name = []


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


def get_games_list() -> list:
    games_list = [[], [], []]
    file_easy = open("Games_List(Easy).csv", "r")
    reader_easy = csv.reader(file_easy)
    file_medium = open("Games_List(Medium).csv", "r")
    reader_medium = csv.reader(file_medium)
    file_hard = open("Games_List(Hard).csv", "r")
    reader_hard = csv.reader(file_hard)
    for row in reader_easy:
        word = row[0].upper()
        games_list[0].append(word)
    for row in reader_medium:
        word = row[0].upper()
        games_list[1].append(word)
    for row in reader_hard:
        word = row[0].upper()
        games_list[2].append(word)
    return games_list


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

        print("  ______________ \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||        \n"
                  "  ||        \n"
                  "______ \n"
                  "|    |\n")
    elif count == 2:
        print("  ______________ \n"
                  "  ||     | \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||        \n"
                  "  ||        \n"
                  "______ \n"
                  "|    |\n")
    elif count == 3:
        print("  ______________ \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||        \n"
                  "  ||        \n"
                  "______ \n"
                  "|    |\n")
    elif count == 4:
        print("  ______________ \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||       \n"
                  "  ||        \n"
                  "  ||        \n"
                  "______ \n"
                  "|    |\n")
    else:
        print("  ______________ \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||     | \n"
                  "  ||     ???? \n"
                  "  ||    /|\ \n"
                  "  ||    / \ \n"
                  "  ||        \n"
                  "  ||        \n"
                  "_____ \n"
                  "|    |\n")


def start_the_game(word: str, count: int, level) -> None:
    if count == 5:
        print(f"The word is {word}. Better luck next Time")
        play_again = input("Do you want to play again Yes --> Y No --> N ")
        play_again = play_again[0].upper()
        if play_again == "Y":
            list_guess.clear()
            list_char.clear()
            list_underscore.clear()
            load_the_game(level)
        return
    char = input("Take a guess ")
    char = char[0]
    if not char.isalpha():
        print("Invalid input")
        start_the_game(word, count, level)
        return
    char = char.upper()
    if char in list_guess:
        print("You have already made this guess. Please make a different guess ")
        start_the_game(word, count, level)
        return
    list_guess.append(char)
    if char not in word:
        count += 1
        hangman(count)
        g_word = "guesses"
        if count == 4:
            g_word = "guess"
        if count != 5:
            print(f"Oops! Wrong guess. You have {5 - count} {g_word} remaining")
        start_the_game(word,count,level)
        return
    for i in range(len(list_char)):
        if char == list_char[i]:
            list_underscore[i] = char

    if "_" not in list_underscore:
        print(f"Congrats! You have guessed \"{word}\" correctly")
        if level == "HARD":
            print(f"Congrats {name[0]}! You have completed the game")
            return
        print("You have reached the next level")
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
            list_guess.clear()
            load_the_game(level)
            return
    else:
        temp_word = "".join(list_underscore)
        print(temp_word)
        start_the_game(word, count, level)


def load_the_game(level: str) -> None:
    typewriter(f"You are in level {level}. All the best {name[0]}\n")
    word_list = []
    index = random.choice([0, 1, 2])
    if level == "EASY":
        if index == 0:
            word_list = get_animal_list()[0]
        elif index == 1:
            word_list = get_countries_list()[0]
        else:
            word_list = get_games_list()[0]
    elif level == "MEDIUM":
        if index == 0:
            word_list = get_animal_list()[1]
        elif index == 1:
            word_list = get_countries_list()[1]
        else:
            word_list = get_games_list()[1]
    else:
        if index == 0:
            word_list = get_animal_list()[2]
        elif index == 1:
            word_list = get_countries_list()[2]
        else:
            word_list = get_games_list()[2]
    word = random.choice(word_list)
    for char in word:
        list_underscore.append("_")
        list_char.append(char)
    print("The word is "+"".join(list_underscore))
    if index == 0:
        print("The word is of type animal")
    elif index == 1:
        print("The word is of type country")
    else:
        print("The word is of type sport")
    start_the_game(word, 0, level)


def typewriter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !=" \n ":
            time.sleep(0.05)
        else:
            time.sleep(1)


def start() -> None:

    my_text = "Welcome to the Hangman Game! Please Enter your name "
    language = 'en'
    output = gTTS(my_text, lang=language, slow=False)
    output.save("output.mp3")
    typewriter("Welcome to the Hangman Game! Please Enter your name -> ")
    playsound.playsound("output.mp3")
    
   
    give_name = input()
    name.append(give_name)
    level = "EASY"
    load_the_game(level)


start()








