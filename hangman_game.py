from random import choice
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


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


def print_scene(var_dict):
    os.system("cls")
    used_letter_msj=""
    guessed_right_msj=""
    word=""
    scene_str=""

    hangman_pics = HANGMANPICS[::-1]

    hanged_man=hangman_pics[var_dict.get("lives")]

    scene_str+=hanged_man+"\n"

    #Making the word with spaces
    for letter in var_dict.get("guessed_l"):
        word+=letter+" "
    scene_str+=word+"\n"

    #To create message if letter is already used
    if var_dict.get("used_already"):
        used_letter_msj="Ya utilizaste esta letra, vuelve a intentar\n"
        scene_str+=used_letter_msj

    #To create an error message if input_letter was not valid
        scene_str+=var_dict.get("error")+"\n"

    #To create message if the letter was guessed right or not
    if var_dict.get("guessed_right") == None:
        guessed_right_msj=""
    elif var_dict.get("guessed_right"):
        guessed_right_msj="¡Acertaste una letra!\n"
    else:
        guessed_right_msj="Mala suerte, la letra no era correcta :C\n"
    scene_str+=guessed_right_msj

    # Lives counter
    scene_str+=f"""Vidas: {var_dict.get("lives")}\n"""

    if not (var_dict.get("guessed_l") == var_dict.get("word_l") or var_dict.get("lives") == 0):
        scene_str+="\nIngresa una letra"

    if var_dict.get("guessed_l") == var_dict.get("word_l"):
        scene_str+="\nFelicidades Ganaste!!!!"

    if var_dict.get("lives") == 0:
        scene_str+=f"""\nLo sentimos haz perdido :C 
La palabra era: {var_dict.get("game_word")}
Terminó el juego"""
    
    print(scene_str)


def check_guess(word_l, guessed_l, input_letter):
    guessed_right=False
    for i in range(0, len(word_l)):
        if input_letter == word_l[i]:
            guessed_l[i] = input_letter
            guessed_right=True

    return guessed_l, guessed_right


def run():

    # Game variables
    game_word = normalize(get_random_word()).upper()
    #game_word = "Hola".upper()
    lives = 6
    used_letters=[]
    word_l = [i for i in game_word]
    guessed_l = ["_" for i in word_l]
    guessed_right=True
    scene_dict={
        "lives": lives,
        "game_word": game_word,
        "guessed_l": guessed_l,
        "word_l": word_l,
        "used_letters": used_letters,
        "used_already": False,
    }

    # First print format
    print_scene(scene_dict)

    while True:
        try:
            input_letter = input("").upper()
            if input_letter.isdigit():
                raise ValueError("No puedes ingresar valores numéricos, solo letras")
            if len(input_letter)!=1:
                raise ValueError("Solo puedes ingresar una letra")
            scene_dict["error"]=None
        except ValueError as ve:
            scene_dict["error"] = str(ve)

        scene_dict["input_letter"] = input_letter
        if input_letter in used_letters:
            scene_dict["used_already"] = True
        else:
            scene_dict["used_already"] = False
            used_letters.append(input_letter)
        guessed_l, guessed_right = check_guess(word_l, guessed_l, input_letter)
        scene_dict["guessed_l"] = guessed_l
        scene_dict["guessed_right"] = guessed_right
        word = ""
        for letter in guessed_l:
            word+=letter+" "
        if not guessed_right:
            lives-=1
            scene_dict["lives"]=lives

        print_scene(scene_dict)

        if guessed_l == word_l or lives == 0:
            input()
            break
        

if __name__ == '__main__':
    run()