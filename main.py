import random
def findWord():
    words = open("answords.txt", "r")  # all the possible answer words
    words = words.readlines() # reads it
    poswords = open("possiblewords.txt", "r")  # all the possible words the user can guess
    poswords = poswords.readlines() # reads it
    answer = random.choice(words) # chooses a random word to be used as an answer
    return answer, poswords # returns both
def ShowAttempt(atts, word, colors):
    print("\n"*15 +"Wordle " + str(atts) + "/6") # skips 15 lines, then tells you how many attempts you have out of 6
    guess = str(word.upper() + " " + colors) # makes a guess variable with the word, then the colors
    guesses.append(guess) # appends the guess variable to the guesses list
    for guess in guesses: # this for loop prints every guess in the guesses list
        print(guess)
    atts += 1 # adds an attempt 
    if str(word.upper() + " " + "🟩🟩🟩🟩🟩") in guesses: # if the player got the answer, win and send the link of the defintion of the word
        print("Congrats! You won. The answer was " + answer.upper() + ".")
        print("Here is the definition of " + answer.replace("\n", "") + ": https://www.google.com/search?q=" + answer.replace("\n", "") + "+definition+english")
        exit()
    elif atts == 7: # if the player has not gotten the answer in 6 guesses, lose and send the link of the defintion of the word
        print("Aw man... You lost. The answer was " + answer.upper() + ".")
        print("Here is the definition of " + answer.replace("\n", "") + ": https://www.google.com/search?q=" + answer.replace("\n", "") + "+definition+english")
        exit()
    else:
        DoAttempt(atts) # continue the loop
def checkLetters(atts, word):
    colors = "" # this is what we will be sending to ShowAttempt() later on
    for word_index, word_letter in enumerate(word):
        matched_colors = "⬛" # this is what we will get if both of the if statements are false
        for letter_index, answer_letter in enumerate(answer):   
            if word_letter == answer_letter and word_index == letter_index: # in other words, if the letter in the guess is in the same spot as the letter in the answer, this if statement is true.
                matched_colors = "🟩"
                break
            elif word_letter != answer_letter and word_index == letter_index and answer.count(word_letter) > 0 and answer.count(word_letter) >= word.count(word_letter):  # in other words, if the letter in the guess is in the answer but not in the right place while following a green/yellow rule, this if statement is true.
                matched_colors = "🟨"
                break
        colors += matched_colors # adds the color we found to colors
    ShowAttempt(atts, word, colors) # to then send it to ShowAttempt()
def DoAttempt(atts): 
    guess = str(input("Guess?: ")) # asks you to guess a 5 letter word
    if len(guess) != 5: # if the guess is not 5 letters long, it tells you then asks you to guess another 5 letter word
        print("Not a 5 letter word.")
        DoAttempt(atts)
    if guess + "\n" not in poswords: # if the guess is not a word, it tells you then asks you to guess another 5 letter word
        print("Not in the guess list.") 
        DoAttempt(atts)
    checkLetters(atts, guess) # checks the letters with colors
guesses = [] # this will be used for the ShowAttempt() function
attempt = 1
answer, poswords = findWord() # gets the answer and all the possible words from the findWord() function
print("\n"*15) #skips 15 lines
DoAttempt(attempt)
