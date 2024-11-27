import random
from itertools import product


class Board:
    """
    Tracks all guesses and their associated scores (black and white pegs).
    """
    def __init__(self):
        self.history = []  # Stores tuples of (guess, (black_pegs, white_pegs))

    def add_guess(self, guess, score):
        """
        Adds a guess and its score to the history.
        :param guess: List[str] - The guessed code (colors).
        :param score: Tuple[int, int] - The number of black and white pegs.
        """
        self.history.append((guess, score))


class Verifier:
    """
    Compares a guess with the secret code to calculate black and white pegs.
    """
    @staticmethod
    def verify(guess, secret):
        """
        Compares guess with secret and returns black and white pegs.
        :param guess: List[str] - The guessed code.
        :param secret: List[str] - The secret code.
        :return: Tuple[int, int] - (black_pegs, white_pegs)
        """
        black_pegs = sum(g == s for g, s in zip(guess, secret))  # Exact matches
        whites = sum(min(guess.count(c), secret.count(c)) for c in set(guess))  # Matches ignoring position
        white_pegs = whites - black_pegs  # White pegs exclude exact matches
        return black_pegs, white_pegs


class Player:
    """
    Suggests new guesses based on game history and hypothesis list.
    """
    def __init__(self, colors, code_length):
        """
        Initializes the player with all possible guesses.
        :param colors: List[str] - The available colors.
        :param code_length: int - Length of the code.
        """
        self.hypothesis_list = list(product(colors, repeat=code_length))

    def suggest_code(self):
        """
        Suggests a random code from the hypothesis list.
        :return: List[str] - A suggested code.
        """
        return random.choice(self.hypothesis_list)

    def update_hypothesis(self, guess, score):
        """
        Updates the hypothesis list by keeping only valid codes.
        :param guess: List[str] - The guessed code.
        :param score: Tuple[int, int] - The score (black_pegs, white_pegs) for the guess.
        """
        verifier = Verifier()
        self.hypothesis_list = [
            code for code in self.hypothesis_list
            if verifier.verify(code, guess) == score
        ]


def main():
    # Game parameters
    colors = ["blue", "green", "red", "white", "black", "pink", "orange", "yellow"]  # Available colors
    code_length = 5  # Length of the code

    # Initialize the game objects
    secret_code = [random.choice(colors) for _ in range(code_length)]
    board = Board()
    player = Player(colors, code_length)
    verifier = Verifier()

    print("Secret code has been generated. Try to guess it!")

    # Game loop
    attempts = 0
    while True:
        attempts += 1
        guess = player.suggest_code()
        score = verifier.verify(guess, secret_code)
        board.add_guess(guess, score)

        print(f"Attempt {attempts}: Guess = {guess}, Score = {score}")

        if score[0] == code_length:
            print(f"Congratulations! The secret code {secret_code} was cracked in {attempts} attempts.")
            break

        player.update_hypothesis(guess, score)


# Run the program
if __name__ == "__main__":
    main()
