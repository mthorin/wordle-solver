def load_words():
    with open('words_wordle.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def update_correct(words, letters):
    pass

def update_incorrect(words, letters):
    pass

def update_yellow(words, letters):
    pass

def generate_best_word(words, correct, incorrect, yellow):
    pass

def main():
    words = load_words()

    correct_letters = [None, None, None, None, None]
    incorrect_letters = []
    yellow_letters = [[],[],[],[],[]]

    while None in correct_letters:
        update_correct(words, correct_letters)
        update_incorrect(words, incorrect_letters)
        update_yellow(words, yellow_letters)
        generate_best_word(words, correct_letters, incorrect_letters, yellow_letters)

if __name__ == '__main__':
    main()