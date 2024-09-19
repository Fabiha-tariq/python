class NumberGuessingGame:
    def __init__(self, level):
        self.level = level
        self.guesses = 0
    
    def play(self):
        raise NotImplementedError("Subclasses must implement this method")

# Level 1 class
class Level1(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=1)
        self.number_to_guess = 4
        self.max_guesses = 3

    def play(self):
        print("Welcome to Level 1: Guess a number between 1 and 10")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 2 class
class Level2(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=2)
        self.number_to_guess = 14
        self.max_guesses = 4

    def play(self):
        print("Welcome to Level 2: Guess a number between 1 and 20")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 3 class
class Level3(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=3)
        self.number_to_guess = 25
        self.max_guesses = 5

    def play(self):
        print("Welcome to Level 3: Guess a number between 1 and 30")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 4
class Level4(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=4)
        self.number_to_guess = 33
        self.max_guesses = 6

    def play(self):
        print("Welcome to Level 4: Guess a number between 1 and 40")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 5
class Level5(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=5)
        self.number_to_guess = 45
        self.max_guesses = 8

    def play(self):
        print("Welcome to Level 5: Guess a number between 1 and 50")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 6
class Level6(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=6)
        self.number_to_guess = 51
        self.max_guesses = 10

    def play(self):
        print("Welcome to Level 6: Guess a number between 1 and 60")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 7
class Level7(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=7)
        self.number_to_guess = 64
        self.max_guesses = 12

    def play(self):
        print("Welcome to Level 7: Guess a number between 1 and 70")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 8
class Level8(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=8)
        self.number_to_guess = 77
        self.max_guesses = 6

    def play(self):
        print("Welcome to Level 8: Guess a number between 1 and 80")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 9
class Level9(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=9)
        self.number_to_guess = 89
        self.max_guesses = 6

    def play(self):
        print("Welcome to Level 9: Guess a number between 1 and 90")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False

# Level 10
class Level10(NumberGuessingGame):
    def __init__(self):
        super().__init__(level=10)
        self.number_to_guess = 96
        self.max_guesses = 6

    def play(self):
        print("Welcome to Level 10: Guess a number between 1 and 100")
        while self.guesses < self.max_guesses:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            if guess == self.number_to_guess:
                print(f"Congratulations! You've guessed the number")
                return True
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        print("Sorry, you're out of guesses. The correct number was ", number_to_guess)
        return False


# Game controller class to control game 
class GameController:
    def __init__(self):
        self.levels = [Level1(), Level2(), Level3(), Level4(), Level5(), Level6(),Level7(),Level8(),Level9(),Level10()]  # Add more levels here
        self.current_level = 0

    def start_game(self):
        while self.current_level < len(self.levels):
            current_game = self.levels[self.current_level]
            print("Starting Level" , current_game.level)
            if current_game.play():
                self.current_level += 1
                if self.current_level < len(self.levels):
                    print("Moving to Level" , self.current_level + 1, "!!!")
            else:
                print("Game Over!")
                break
        if self.current_level == len(self.levels):
            print("Congratulations! You've completed all levels!")
            print("/n **************   Go Back Press F5 and Start Game Again   **************")

game = GameController()
game.start_game()
