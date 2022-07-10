import random


def findWord():
    words = open("answords.txt", "r")
    words = words.readlines()
    poswords = open(
        "possiblewords.txt", "r"
    )
    poswords = poswords.readlines()
    answer = random.choice(words)  # chooses a random word to be used as an answer
    return answer, poswords


def ShowAttempt(numAtts, word, colors):
    print(
        "\n" * 50 + "  Wordle " + str(numAtts) + "/6"
    )  # clear screen + tells you how many attempts you have out of 6
    guess = str(word.upper() + " " + colors)
    guesses.append(guess)
    for guess in guesses:
        print(guess)
    numAtts += 1
    if (
        str(word.upper() + " " + "🟩🟩🟩🟩🟩") in guesses
    ):  # win and send the link of the defintion of the word
        print("Congrats! You won. The answer was " + answer.upper() + ".")
        print(
            "Here is the definition of "
            + answer.replace("\n", "")
            + ": https://www.google.com/search?q="
            + answer.replace("\n", "")
            + "+definition+english"
        )
        exit()
    elif (
        numAtts == 7
    ):  # lose and send the link of the defintion of the word
        print("Aw man... You lost. The answer was " + answer.upper() + ".")
        print(
            "Here is the definition of "
            + answer.replace("\n", "")
            + ": https://www.google.com/search?q="
            + answer.replace("\n", "")
            + "+definition+english"
        )
        exit()
    else:
        DoAttempt(numAtts)


def checkLetters(atts, word):
    colors = ""  
    for word_index, word_letter in enumerate(word):
        matched_colors = "⬛"
        for letter_index, answer_letter in enumerate(answer):
            if (
                word_letter == answer_letter and word_index == letter_index
            ):  # in other words, if the letter in the guess is in the same spot as the letter in the answer, 
                # this if statement is true.
                matched_colors = "🟩"
                break
            elif (
                word_letter != answer_letter
                and word_index == letter_index
                and answer.count(word_letter) > 0
                and answer.count(word_letter) >= word.count(word_letter)
            ):  # in other words, if the letter in the guess is in the answer but not in the right place while following a green/yellow rule, 
                # this if statement is true.
                matched_colors = "🟨"
                break
        colors += matched_colors
    ShowAttempt(atts, word, colors)


def DoAttempt(atts):
    try:
        guess = input("Guess a five letter word: ")
        if (
            len(guess) != 5
        ):  # if the guess is not 5 letters long, it tells you then asks you to guess another 5 letter word
            print("Not a 5 letter word.")
            DoAttempt(atts)
        if (
            guess + "\n" not in poswords
        ):  # if the guess is not a word, it tells you then asks you to guess another 5 letter word
            print("Not in the guess list.")
            DoAttempt(atts)
        checkLetters(atts, guess)
    except KeyboardInterrupt:
        print("\nHey, you interrupted the code using your keyboard somehow.")
        exit()


guesses = []  # this will be used for the ShowAttempt() function
attempt = 1
answer, poswords = findWord()
print("\n" * 50)  # clear screen
DoAttempt(attempt)
