def load_words():
    with open('words_wordle.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def main():
    words = load_words()


if __name__ == '__main__':
    main()