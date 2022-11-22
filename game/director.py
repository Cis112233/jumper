from player import Player
from parachute import Parachute
from word import Word

class director:

    def __init__(self):
        """Creates initial state.
        
        Args:
            self (Director): an instance of Director.
        """
        self.parachute = Parachute()
        self.words = Word()
        self.words.pick_word()
        self.player = Player(self.words)

    def play_game(self):
        """Plays the game.
        
        Args:
            self (Director): an instance of Director.
        """
        inc = 0
        while(not self.words.check_win()):
            inc += 1
            self.words.print_word()
            self.parachute.print_chute()
            self.player.guess_letter(self.parachute)
            self.parachute.print_chute()

            if self.words.check_win():
                self.words.print_word()
                print("You win!")
                break

            if inc >= len(self.words.return_word()) - 1:
                print("You lose.")
                break
            
