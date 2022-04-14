from random import choice
import os

GUESSED_WORD=""
USED_LETTERS=[]

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

def generate_guessed_word(word, letter):
    GUESSED_WORD=""
    for i in range(0, len(word)):
        if letter == word[i]:
            GUESSED_WORD+=letter+" "
        else:
            GUESSED_WORD+="_ "
    return GUESSED_WORD

def generate_scene(word, letter):
    title = "¡Adivina la palabra!\n"
    letters_space = generate_guessed_word(word, letter)
    letters_space+="\n"
    instruction = "Ingresa una letra: "

    return title+letters_space+instruction

def run():
    game_word = normalize(get_random_word()).upper()

    game_word=game_word.upper()

    scene = generate_scene(game_word, "o".upper())

    print(scene)

    scene = generate_scene(game_word, "l".upper())

    print(scene)



if __name__ == '__main__':
    run()