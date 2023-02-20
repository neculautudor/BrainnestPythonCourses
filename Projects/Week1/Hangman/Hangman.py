'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''


class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.tries_left = 6 # to check if user lost or not
        self.partial_word = ['_'] * len(word) # used for printing, multiplied _ for as many characters as the word has
        self.letters_guessed = 0 # used to check if the user won or not

        self.guessed_letters_set = set()
        self.used_letters_set = set()
        # i used sets so that there will be no duplicates



    def run_game(self):
        while True:
            print(f'You have {self.tries_left} tries left')
            print(f"Used letters: {' '.join(self.used_letters_set)}")
            print(f'Word: {self.printable_word(self.partial_word)}')
            input_letter = input('Guess a letter: ')
            if input_letter == 'quit':
                print('Exited the game!')
                break
            if len(input_letter) > 1:
                print('Wrong input, please type only one letter')
                continue # we ignore the rest of the loop and start again
            elif not input_letter.isalpha(): # check if the user wrote a letter or not
                print('Wrong input, please type only characters')
                continue
            # if the input is correct, we proceed with the game
            self.used_letters_set.add(input_letter)
            good_letter = False # used to check if the user is wrong
            for index, letter in enumerate(self.word):
                if letter == input_letter: # check if the character on each index is the same as what the user chose
                    self.partial_word[index] = letter
                    self.letters_guessed += 1
                    if letter not in self.guessed_letters_set:
                        self.guessed_letters_set.add(letter)
                    good_letter = True # if the letter is in the word, we set good_letter to true so we don't decrement the tries left
            if not good_letter:
                self.tries_left -= 1
            if self.letters_guessed == len(self.word): # if the user guessed the number of letters the word has, he won
                print(f'You guessed the word {self.word} !')
                break
            elif not self.tries_left:
                print('\nGame Over, you lost!')
                break

    def printable_word(self, list):
        return ' '.join(list)


if __name__ == '__main__':
    game = HangmanGame('java')
    game.run_game()
