def load_words():
    with open('words_wordle.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def check_and_remove(words, check):
    to_remove = []
    for word in words:
        if check(word):
            to_remove.append(word)

    for word in to_remove:
        words.remove(word)

def update_correct(words, letters):
    print(f"Correct letters previously confirmed:            {letters[0] if letters[0] else "_"}{letters[1] if letters[1] else "_"}{letters[2] if letters[2] else "_"}{letters[3] if letters[3] else "_"}{letters[4] if letters[4] else "_"}")
    new = input("Enter new correct letters (use _ if no change) : ")
    
    for i in range (5):
        if new[i] == "_":
            continue
        letter = new[i].lower()
        if letter.isalpha():
            letters[i] = letter
            check_and_remove(words, lambda word: word[i] != letter)

    print(words)


def update_incorrect(words, letters):
    pass

def update_yellow(words, letters):
    pass

def generate_best_word(words, correct, incorrect, yellow):
    pass

def main():
    possible_words = load_words()

    correct_letters = [None, None, None, None, None]
    incorrect_letters = []
    yellow_letters = [[],[],[],[],[]]

    while None in correct_letters:
        update_correct(possible_words, correct_letters)
        update_incorrect(possible_words, incorrect_letters)
        update_yellow(possible_words, yellow_letters)
        generate_best_word(possible_words, correct_letters, incorrect_letters, yellow_letters)

if __name__ == '__main__':
    main()