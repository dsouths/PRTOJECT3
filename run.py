import random

word_list = ["Qatar", "Ecuador", "Senegal", "Netherlands", "England", "Iran", "USA", "Wales", "Argentina", "SaudiArabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain", "CostaRica", "Germany", "Japan", "Belgium", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "SouthKorea"]
def display_hangman(attempts):
        stages = [  # final state:
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |     \|/ 
                   |      | 
                   |     / \ 
                   - 
                """, 
                # 5
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |     \|/ 
                   |      | 
                   |     /  
                   - 
                """, 
                # 4
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |     \|/ 
                   |      | 
                   |       
                   - 
                """, 
                # 3
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |     \| 
                   |      | 
                   |      
                   - 
                """, 
                # 2
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |      | 
                   |      | 
                   |      
                   - 
                """, 
                # 1 
                """ 
                   -------- 
                   |      | 
                   |      O 
                   |     
                   |       
                   |      
                   - 
                """, 
                # initial state 
                """ 
                   -------- 
                   |      | 
                   |       
                   |     
                   |       
                   |      
                   - 
                """ 
    ] 
        return stages[attempts] 


#this function returns a random word from the word list & returns upper case to stop upper/lower case errors occuring later
def pick_word():
    word = random.choice(word_list)
    return word.upper()
    
#function to play game with chosen random word
def play_game(word):
    #keeps track of the guessed letters & words
    guessed_letters = []
    guessed_words = []
    #keeps track of the game state
    guessed = False
    #replaces word with same amount of dashes as letters in word
    dashed_word = "_" * len(word)
    #max attempts player has to guess word
    attempts = 6
    
    print("\n*****************Welcome to the World Cup 22 Edition of Hangman!*****************\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Kick off by guessing a letter & then the name of the team playing in the tournament\n")
    print(display_hangman(attempts))

    while not guessed and attempts > 0:
        guess = input("Pick a letter or word: ").upper() 
        if len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("What a miss!! You already guessed this WORD!!", guess)
            elif guess != word:
                print("WHAT A MISS", guess, "is NOT the word!") 
                attempts -= 1 
                guessed_words.append(guess)
            else: 
                guessed = True 
                dashed_word = word
        elif len(guess) == 1 and guess in 'ABCDEFGHIJKLMNOPQRSTUVEXYZ':
            if guess not in 'ABCDEFGHIJKLMNOPQRSTUVEXYZ':
                print('YELLOW CARD!! Please enter a LETTER.')
            elif guess in guessed_letters:
                print("You already guessed this LETTER, better change tactics!!", guess)
            elif guess not in word:
                print(guess, "is not in the word.") 
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
                if "_" not in dashed_word: 
                    guessed = True   
        else:
            print("NOT a valid guess!") 
        print(dashed_word) 
        print(display_hangman(attempts))
        
    
    if guessed: 
        print("RESULT!!! You have won the match & guessed the word correctly! Olé Olé Olé...")
    else:
        print("Sorry, you ran out of tries & lost the match! The word was " + word + ". Better luck next time!")
    

def main(): 
    word = pick_word() 
    play_game(word) 
    while input("Play Again? (Y/N) ").upper() == "Y": 
        word = pick_word() 
        play_game(word) 
if __name__ == "__main__": 
    main()