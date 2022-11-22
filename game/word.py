import random
class Word:
    

    def __init__(self):
        """Constructs a new Word.
        
        Args:
            self (word): an instance of word.
        """
        self.word_list = ["the","quick","brown","fox","jumped","over","the","lazy","dog"]
        self.word_picked = ""
        self.guesses = ""
        
    
    def pick_word(self):
        """Picks a word from a list.
        
        Args:
            self (word): an instance of word.
        """
        self.word_picked = random.choice(self.word_list)

    def return_word(self):
        """Returns the word picked.
        
        Args:
            self (word): an instance of word.
        """
        return self.word_picked

    def guess(self, choice, para_obj):
        """Takes users choice and paracute object and processes the guess logic
        
        Args:
            self (word): an instance of word.
            choice: the players choice
            para_obj: a parachute object
        """
        self.guesses += choice
        
        if not choice in self.word_picked:
            para_obj.next_chute()

    
    def print_word(self):
        """Prints the word with dashes
        
        Args:
            self (word): an instance of word.
        """
        for letter in self.word_picked:
            if letter in self.guesses:
                print(letter, end = " ")
            else:
                print("_", end = " ")
        print()

    def check_win(self):
        """Checks to see if the player wins
        
        Args:
            self (word): an instance of word.
        """
        inc = 0
        for letter in self.word_picked:
            if letter in self.guesses:
                inc += 1
        if inc >= len(self.word_picked):
            return True
        else:
            return False



