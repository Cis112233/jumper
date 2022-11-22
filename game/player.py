from word import Word


class Player():
    """Creates a player
        
    Args:
        self (word): an instance of word.
    """
    def __init__(self,word_obj):
        """Creates initial variables
        
        Args:
            self (word): an instance of word.
            self
        """
        self.guess = ""
        self.word_object = word_obj
        self.word_object.pick_word()

    def guess_letter(self, para_obj):
        """Handles the guess objects
        
        Args:
            self (word): an instance of word.
            para_obj: a parachute object
        """
        self.guess = input("Enter a letter [a-z]: ").lower()
        self.word_object.guess(self.guess, para_obj)
        return self.word_object

