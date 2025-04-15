import random
from phrase import Phrase

# Create your Game class logic in here.
class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Whatever will be will be"), Phrase("Who dares wins"), Phrase("Hakunamatata"), Phrase("Marcy is the best"), Phrase("I miss the old days")]
        self.active_phrase = None
        self.guesses = [" "]

    def reset_game(self):
        #Resets the game for a new round
        self.missed =0
        self.guesses = [" "]
        self.active_phrase = None

# When the came starts, opens welcome and then sets the active_phrase to the random_phrase created.
    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
#I have to set the missed to 5 as it starts on 0
        while self.missed < 5:
            self.active_phrase.display(self.guesses)
            print(f"\nYou have {5 - self.missed} guesses remaining.")

            #If the letter guessed is not in the active phrase then the missed counter goes up.
            guess = self.get_guess()
            if not self.active_phrase.check_letter(guess):
                self.missed += 1
                print(f"Sorry, {guess} is not in the phrase")

                #This determines the game over condition
                if self.missed >= 5:
                    play_again = self.game_over(won = False)
                    return play_again
                else:
                    print(f"Nice! {guess} is in the phrase")

            #This determines the win condition
            if self.active_phrase.check_complete(self.guesses):
                play_again = self.game_over(won = True)
                return play_again

    def get_random_phrase(self):
        #This pulls a random phrase from the list of phrases available to the Game class.
        random_phrase = random.choice(self.phrases)
        return random_phrase


    def welcome(self):
        print("\n"+ "="*94 + "\nWelcome to PhraseHunter, are you ready to bang your head against the wall in pure frustration?")
        print("Come on Down and guess away!\n" + "="*94+"\n\n")

    def get_guess(self):

        #This method gets the guess from a user and records it in the guesses attribute
        while True:
            try:
                guess = input ("Guess a letter:     ")
                if len(guess) != 1:
                    print("Please enter a single letter.")
                    continue

                #Checks for uppercase
                if not guess.isalpha():
                    print("Please enter a letter from A-Z")
                    continue

                #Checks for guesses you have already done
                if guess in self.guesses:
                    print(f"You already guessed the letter '{guess}'.")
                    continue

                #adds the guess to the list of guesses
                self.guesses.append(guess)
                return guess

            #In case I am retarded and missed something.
            except Exception as e:
                print(f"An error occured: {e}, please try again.")

    #This one I had to get some help with the won= false flag.
    def game_over(self, won = False):

        #setting win statement
        if won:
            print("\n" + "="*40 +f'\nCongratulations, You Guessed the phrase!\n"{self.active_phrase}"\nYou won son!')
        else:
            print(f"\nGame Over!\n The phrase was: {self.active_phrase}")
        #Resetting the counters and phrase for another game so it doesnt use the previous games

        while True:
            play_again = input ("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                return True
            elif play_again.lower() == "n":
                return False
            else:
                print("Please answer 'y' or 'n'")
                continue


#Fin!!!
