
class Parachute:
    
    def __init__(self):
        """Creates initial variable
        
        Args:
            self (parachute): an instance of parachute.
        """
        self.parachute_state = 0
    
    def next_chute(self):
        """Incriments chute
        
        Args:
            self (parachute): an instance of parachute.
        """
        self.parachute_state += 1
    
    def print_chute(self):
        """Prints differenc chutes based on parachute_state
        
        Args:
            self (parachute): an instance of parachute.
        """
        if self.parachute_state == 0:
            print("  ___")
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print()
            print("^^^^^^^")

        elif self.parachute_state == 1:
            print()
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print()
            print("^^^^^^^")

        elif self.parachute_state == 2:
            print()
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print()
            print("^^^^^^^")

        elif self.parachute_state == 3:
            print()
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print()
            print("^^^^^^^")

        elif self.parachute_state == 4:
            print()
            print("   x")
            print("  /|\\")
            print("  / \\")
            print()
            print("^^^^^^^")
