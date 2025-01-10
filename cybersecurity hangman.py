import turtle, random, draw
from instruction import words, instruction
from time import sleep

tries = 7
missedLetters = ''
correctLetters = ''
secretWord = random.choice(words)
gameIsDone = False
def wait():
    for i in range(5):
        print('.', end = ' ')
        sleep(.5)
    print()

def displayBoard(missedLetters, correctLetters, secretWord):
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()


draw.beginGame()
instruction()
print('The word has', len(secretWord), 'letters')
print("You will have 7 tries to win this game!!")
print("Let me think of a word")
wait()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('============================================')
        guess = input("Guess a letter: ")
        guess = guess.lower()
        print('Let me check')
        wait()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +
              '"! You have won!')
            gameIsDone = True
    else:
        print('You guessed a wrong letter!!!')
        tries -= 1
        print('Tries left' ,tries)
        missedLetters = missedLetters + guess
        draw.drawHangman(missedLetters)

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == 7:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
 
    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            instruction()
            tries = 7
            missedLetters = ''
            correctLetters = ''
            secretWord = random.choice(words)
            gameIsDone = False
            print('The word has', len(secretWord), 'letters')
            print("You will have 7 tries to win this game!!")
            draw.beginGame()
        else:
            break
