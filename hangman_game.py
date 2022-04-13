import random

def get_words():
    words = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        words = [line.rstrip('\n') for line in f]
    return words

def get_random_word():
    word = random.choice(get_words())
    return word

def run():
    print(get_random_word())

if __name__ == '__main__':
    run()