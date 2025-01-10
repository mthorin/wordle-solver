from string import ascii_lowercase
import sys

def load_words():
    path = "words_wordle.txt"

    if len(sys.argv) > 1:
        path = sys.argv[1]

    with open(path) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def check_and_remove(words, check):
    to_remove = []
    for word in words:
        if check(word):
            to_remove.append(word)

    for word in to_remove:
        words.remove(word)

def get_input(in_string):
    new = None
    while not new:
        new = input(in_string)
        if len(new) != 5:
            print("Invalid input length! Try again.")
            new = None
    return new

def update_correct(words, letters):
    print("")
    print(f"Correct letters previously confirmed: {letters[0] if letters[0] else "_"}{letters[1] if letters[1] else "_"}{letters[2] if letters[2] else "_"}{letters[3] if letters[3] else "_"}{letters[4] if letters[4] else "_"}")
    new = get_input("Enter new correct letters (use _ if no change): ")
    
    for i in range(5):
        letter = new[i].lower()
        if letter in ascii_lowercase and not letters[i]:
            letters[i] = letter
            check_and_remove(words, lambda word: word[i] != letter)

    print(words)


def update_incorrect(words, letters):
    print("")
    print(f"Incorrect letters previously confirmed: {letters}")
    new = input("Enter incorrect letters: ")
    
    for char in new:
        letter = char.lower()
        if letter in ascii_lowercase:
            if letter not in letters:
                letters.append(letter)
                check_and_remove(words, lambda word: letter in word)

    print(words)

def update_yellow(words, letters):
    print("")
    print("Incorrect letters previously confirmed:")
    for i in range(len(letters)):
        print(f"{letters[i][0] if letters[i][0] else "_"}{letters[i][1] if letters[i][1] else "_"}{letters[i][2] if letters[i][2] else "_"}{letters[i][3] if letters[i][3] else "_"}{letters[i][4] if letters[i][4] else "_"}")
    new = get_input("Enter yellow letters (use _ if not yellow): ")
    
    input_list = []

    for i in range(5):
        letter = new[i].lower()
        if letter in ascii_lowercase:
            input_list.append(letter)
            check_and_remove(words, lambda word: letter not in word or word[i] == letter)
        else:
            input_list.append(None)

    letters.append(input_list)

    print(words)

def generate_best_word(all_words, possible_words, correct_letters):
    if len(possible_words) < 3:
        print("")
        print(f"Suggested word to guess is {next(iter(possible_words))}")
        return

    letter_values = [dict(), dict(), dict(), dict(), dict()]

    for char in ascii_lowercase:
        letter_values[0][char] = 0
        letter_values[1][char] = 0
        letter_values[2][char] = 0
        letter_values[3][char] = 0
        letter_values[4][char] = 0

    for word in possible_words:
        for i in range(5):
            if word[i] in letter_values[i]:
                letter_values[i][word[i]] += 1

    for i in range(5):
        if correct_letters[i]:
            letter_values[i][correct_letters[i]] = 0

    best_word = None
    best_value = 0

    for word in all_words:
        value = 0
        for i in range(5):
            value += letter_values[i][word[i]]
        
        if value > best_value:
            best_value = value
            best_word = word

    print("")
    print(f"Suggested word to guess is {best_word}")

def main():
    possible_words = load_words()
    all_words = possible_words.copy()

    correct_letters = [None, None, None, None, None]
    incorrect_letters = []
    yellow_letters = []

    generate_best_word(all_words, possible_words, correct_letters)
    update_correct(possible_words, correct_letters)

    while None in correct_letters:
        update_yellow(possible_words, yellow_letters)
        update_incorrect(possible_words, incorrect_letters)
        generate_best_word(all_words, possible_words, correct_letters)
        update_correct(possible_words, correct_letters)

if __name__ == '__main__':
    main()