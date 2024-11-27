import random
import itertools

class Board:
    """
    Class to track all guesses and their corresponding feedback.
    """
    def __init__(self):
        # Initialize an empty list to store tuples of (guess, feedback)
        self.history = []

    def add(self, guess, feedback):
        # Add the guess and feedback to the history
        self.history.append((guess, feedback))

    def display(self):
        # Display the history of guesses and feedback
        print("Guess history:")
        for idx, (guess, feedback) in enumerate(self.history):
            guess_str = ', '.join(guess)
            print(f"Turn {idx+1}: Guess: [{guess_str}], Feedback (Black pegs, White pegs): {feedback}")

class Verifier:
    """
    Class to compare a guess with the secret code and provide feedback.
    """
    def __init__(self, secret_code):
        # Store the secret code
        self.secret_code = secret_code

    def get_feedback(self, guess):
        """
        Compares the guess with the secret code and returns the number of black pegs and white pegs.
        """
        # Calculate black pegs (correct color and position)
        black_pegs = sum(a == b for a, b in zip(guess, self.secret_code))

        # Calculate white pegs (correct color, wrong position)
        # Create copies of secret_code and guess to manipulate
        secret_code_copy = list(self.secret_code)
        guess_copy = list(guess)

        # Remove black pegs from consideration
        for i in range(len(guess_copy)-1, -1, -1):
            if guess_copy[i] == secret_code_copy[i]:
                del guess_copy[i]
                del secret_code_copy[i]

        # Count white pegs
        white_pegs = 0
        for color in guess_copy:
            if color in secret_code_copy:
                white_pegs += 1
                secret_code_copy.remove(color)

        return black_pegs, white_pegs

class Player:
    """
    Class to suggest the next guess based on the history and hypothesis list.
    """
    def __init__(self, hypothesis_list):
        # Initialize the hypothesis list with all possible codes
        self.hypothesis_list = hypothesis_list

    def update_hypothesis(self, last_guess, feedback):
        """
        Update the hypothesis list by removing codes that are inconsistent with the feedback.
        """
        new_hypothesis = []

        for code in self.hypothesis_list:
            # Simulate the feedback if 'code' was the secret code
            simulated_verifier = Verifier(code)
            simulated_feedback = simulated_verifier.get_feedback(last_guess)

            # If the simulated feedback matches the actual feedback, keep the code
            if simulated_feedback == feedback:
                new_hypothesis.append(code)

        # Update the hypothesis list
        self.hypothesis_list = new_hypothesis

    def suggest_next_guess(self):
        """
        Suggest the next guess from the hypothesis list.
        For simplicity, pick the first code in the list.
        """
        if self.hypothesis_list:
            return self.hypothesis_list[0]
        else:
            return None  # No possible guesses left

def main():
    # Input parameters
    print("Welcome to Mastermind Solver!")
    try:
        num_colors = int(input("Enter the number of possible colors (e.g., 8): "))
        code_length = int(input("Enter the length of the secret code (e.g., 5): "))
    except ValueError:
        print("Invalid input. Using default values: 8 colors, code length 5.")
        num_colors = 8
        code_length = 5

    # Define the list of colors
    base_colors = ['green', 'red', 'pink', 'orange', 'white', 'black', 'yellow', 'blue']
    colors = base_colors[:num_colors]

    # If num_colors exceeds the predefined colors, add numbered colors
    if num_colors > len(base_colors):
        additional_colors = [str(i) for i in range(9, num_colors+1)]
        colors.extend(additional_colors)

    # Generate all possible codes
    # Use itertools.product to generate all combinations with repetition
    all_possible_codes = list(itertools.product(colors, repeat=code_length))

    # Randomly generate the secret code
    secret_code = random.choice(all_possible_codes)
    # For debugging purposes, you can print the secret code
    # print(f"Secret code: {secret_code}")

    # Initialize the Board
    board = Board()

    # Initialize the Player with all possible codes as the hypothesis list
    player = Player(all_possible_codes.copy())

    # Randomly generate the first guess
    guess = random.choice(all_possible_codes)
    # Remove the guess from the hypothesis list
    player.hypothesis_list.remove(guess)

    # Initialize the Verifier with the secret code
    verifier = Verifier(secret_code)

    # Game loop
    max_turns = 12  # Maximum number of turns allowed
    turn = 1
    while turn <= max_turns:
        print(f"\nTurn {turn}:")
        guess_str = ', '.join(guess)
        print(f"Player's guess: [{guess_str}]")

        # Get feedback for the guess
        feedback = verifier.get_feedback(guess)
        print(f"Feedback (Black pegs, White pegs): {feedback}")

        # Update the Board
        board.add(guess, feedback)

        # Check if the guess is correct
        if feedback[0] == code_length:
            print(f"\nCongratulations! The code was broken in {turn} turns!")
            board.display()
            break

        # Update the hypothesis list based on the feedback
        player.update_hypothesis(guess, feedback)
        print(f"Possible codes remaining: {len(player.hypothesis_list)}")

        # Suggest the next guess
        guess = player.suggest_next_guess()

        if guess is None:
            print("No possible guesses left. The game cannot proceed.")
            break

        # Remove the guess from the hypothesis list
        if guess in player.hypothesis_list:
            player.hypothesis_list.remove(guess)

        turn += 1

    else:
        print("\nSorry, the code was not broken within the maximum number of turns.")
        print(f"The secret code was: {', '.join(secret_code)}")
        board.display()

if __name__ == "__main__":
    main()
