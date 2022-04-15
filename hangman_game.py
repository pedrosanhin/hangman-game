from random import choice
import os

def normalize(word):
    replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word


def get_words():
    words = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        words = [line.rstrip('\n') for line in f]
    return words


def get_random_word():
    word = choice(get_words())
    return word


def judge(guess_right):
    if guess_right:
        print("Acertaste la letra!")
    else:
        print("La letra que introduciste fue incorrecta :c")


def check_guess(word_l, guessed_l, input_letter):
    guessed_right=False
    for i in range(0, len(word_l)):
        if input_letter == word_l[i]:
            guessed_l[i] = input_letter
            guessed_right=True

    judge(guessed_right)
    return guessed_l


def run():
    game_word = normalize(get_random_word()).upper()
    #game_word = "Hola".upper()
    used_letters=[]
    word_l = [i for i in game_word]
    guessed_l = ["_" for i in word_l]

    print(guessed_l)
    while True:
        input_letter = input("Ingresa una letra: ").upper()
        guessed_l = check_guess(word_l, guessed_l, input_letter)

        print(guessed_l)

        if guessed_l == word_l:
            print("Ganaste!!!!")
            break
        


if __name__ == '__main__':
    run()