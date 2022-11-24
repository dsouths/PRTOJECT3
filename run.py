import random
import gspread
import google.oauth2.service.account import Credentials
from hangman import display_hangman

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')

word_list = SHEET.worksheet("word_list")


# function returns a random word from the word list & in upper
def pick_word():
    word = random.choice(word_list)
    return word.upper()


# function to play game with chosen random word
def play_game(word):
    # replaces word with same amount of dashes as letters in word
    dashed_word = "~" * len(word)
    # keeps track of the game state
    guessed = False
    # keeps track of the guessed letters & words
    guessed_letters = []
    guessed_words = []
    # max attempts player has to guess word
    attempts = 6
    print("\n**Welcome to the World Cup 22 Edition of Hangman!*\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Guess the name of the team playing in the World Cup\n")
    print(display_hangman(attempts))
    print(dashed_word)
    while not guessed and attempts > 0:
        guess = input("Pick a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('YELLOW CARD!! Please enter a LETTER.')
            elif guess in guessed_letters:
                print("You guessed this LETTER, better change tactics!", guess)
                print(guessed_letters)
            elif guess not in word:
                print(guess, "is NOT in the word.")
                print(guessed_words)
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("GGGGGOAL,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(dashed_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                dashed_word = "".join(word_as_list)
                if "~" not in dashed_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"What a miss!! You already guessed this WORD!! {guess}")
            elif guess != word:
                print("WHAT A MISS {guess}, is NOT the word!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                dashed_word = word
        else:
            print("NOT a valid guess!")
        print(dashed_word)
        print(display_hangman(attempts))
    if guessed:
        print("RESULT!!! You guessed the word correctly! Olé Olé Olé...")
    else:
        print(f"You ran out of tries & lost the match! The word was {word}!")


def main():
    word = pick_word()
    play_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = pick_word()
        play_game(word)


if __name__ == "__main__":
    main()
