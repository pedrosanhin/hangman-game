from random import choice

def get_words():
    words = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        words = [line.rstrip('\n') for line in f]
    return words

def get_random_word():
    word = choice(get_words())
    return word

def generate_scene(word):
    title = "¡Adivina la palabra!\n"
    letters_space = ""
    for i in range(0, len(word)):
        letters_space+="_ "
    letters_space+="\n"
    instruction = "Ingresa una letra: "

    print(title+letters_space+instruction)

def run():
    generate_scene(get_random_word())

if __name__ == '__main__':
    run()