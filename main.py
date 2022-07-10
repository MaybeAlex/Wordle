import random
def findWord():
    words = open("answords.txt", "r")
    words = words.readlines()
    poswords = open("possiblewords.txt", "r")
    poswords = poswords.readlines()
    answer = random.choice(words)
    return answer, poswords
def ShowAttempt(atts, word, colors):
    print("\n"*15 +"Wordle " + str(atts) + "/6")
    guess = str(word.upper() + " " + colors)
    guesses.append(guess)
    for guess in guesses:
        print(guess)
    atts += 1
    if str(word.upper() + " " + "🟩🟩🟩🟩🟩") in guesses:
        print("Congrats! You won. The answer was " + answer.upper() + ".")
        exit()
    elif atts == 7:
        print("Aw man... You lost. The answer was " + answer.upper() + ".")
        exit()
    else:
        DoAttempt(atts)
def checkLetters(atts, word):
    colors = ""
    for word_index, word_letter in enumerate(word):
        matched_colors = "⬛"
        for letter_index, answer_letter in enumerate(answer):   
            if word_letter == answer_letter and word_index == letter_index:
                matched_colors = "🟩"
                break
            elif word_letter != answer_letter and word_index == letter_index and answer.count(word_letter) > 0 and answer.count(word_letter) >= word.count(word_letter):
                matched_colors = "🟨"
                break
        colors += matched_colors
    ShowAttempt(atts, word, colors)
def DoAttempt(atts):
    guess = str(input("Guess?: "))
    if len(guess) != 5:
        print("Not a 5 letter word.")
        DoAttempt(atts)
    if guess + "\n" not in poswords:
        print("Not in the guess list.")
        DoAttempt(atts)
    checkLetters(atts, guess)
guesses = []
attempt = 1
answer, poswords = findWord()
print("\n"*15)
DoAttempt(attempt)