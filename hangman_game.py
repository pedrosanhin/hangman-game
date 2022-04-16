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


def judge(guess_right, lives):
    if guess_right:
        print("\nAcertaste una letra!")
    else:
        print("\nLa letra que introduciste fue incorrecta :c")
        lives-=1
    return lives

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

    # First print format
    os.system("cls")
    word = ""
    for letter in guessed_l:
        word+=letter+" "
    print(word+"\n"+
        "\nTe quedan {lives} vidas".format(lives=lives))

    while True:
        input_letter = input("\nIngresa una letra: ").upper()
        guessed_l, guessed_right = check_guess(word_l, guessed_l, input_letter)
        os.system("cls")
        word = ""
        for letter in guessed_l:
            word+=letter+" "
        print(word+"\n"+
            "\nTe quedan {lives} vidas".format(lives=lives))

        if guessed_l == word_l:
            print("\nFelicidades Ganaste!!!!")
            break

        if lives == 0:
            print("\nLo sentimos haz perdido :C"+
                "\nLa palabra era: "+ game_word+
                "\nTerminó el juego")
            input()
            break
        
        lives = judge(guessed_right, lives)
        


if __name__ == '__main__':
    run()