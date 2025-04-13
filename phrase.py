# Create your Phrase class logic here.
class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __str__(self):
        return self.phrase
# Create the underlined display of the phrase
    def display(self, guesses):
        #Start with nothing and add a _ plus a space for every character in the random phrase.
        displayed_phrase = ""
        for char in self.phrase:
            if char in guesses or char == " ":
                displayed_phrase += char + " "
            else:
                displayed_phrase += "_ "
        print(displayed_phrase)

#makes sure letter is lowercase to match the lowercase phrase.
    def check_letter(self, letter):
        letter = letter.lower()
        return letter in self.phrase
# This will return false until the phrase letters are all in the guesses list.
    def check_complete(self, guesses):
        for char in self.phrase:
            if char == " ":
                continue
            if char not in guesses:
                return False
        return True

