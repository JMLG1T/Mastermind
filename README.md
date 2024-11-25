# Mastermind Algorithm Comparison


An experimental project comparing different algorithms and strategies for solving the classic code-breaking game Mastermind.

## What is Mastermind? 🎯

Mastermind is a classic code-breaking game where one player (the codemaker) creates a secret code of colored pegs, and the other player (the codebreaker) attempts to guess the code through deductive reasoning. After each guess, the codemaker provides feedback:
- Black pegs indicate correct color and position
- White pegs indicate correct color but wrong position

For example, if the secret code is `[Red, Blue, Green, Yellow]` and the guess is `[Red, Yellow, Blue, Purple]`:
- Red is in correct position (1 black peg)
- Yellow and Blue are correct colors but wrong positions (2 white pegs)

![Mastermind Board Game](https://www.hasbro.com/common/productimages/en_IN/A3D0F2E3A4954E178138F27E2921F2DF/FE21BEFDC8F54E9498A6477D07D1E547.png)

Traditional game settings:
- 6 possible colors
- 4 positions
- Colors can be repeated
- 12 attempts to guess the code

## Project Goals 🎯

This repository implements and compares different algorithms for solving Mastermind, focusing on their efficiency and performance. We explore various strategies, from simple to sophisticated approaches:

1. **Random Strategy (Baseline)**
   - Simple random guessing
   - Used as a baseline for comparison

2. **Minimax Strategy**
   - Minimizes the maximum possible remaining candidates
   - Classic approach from Donald Knuth's 1977 paper

3. **Maximum Entropy Strategy**
   - Chooses moves that maximize information gain
   - Uses entropy calculations to reduce uncertainty most effectively

4. **Genetic Algorithm Approach**
   - Evolutionary strategy to evolve better guesses
   - Incorporates feedback to guide the evolution of solutions

5. **Pattern Matching Strategy**
   - Learns from previous games
   - Uses pattern recognition to make informed guesses

## Features ✨

- 🎮 Interactive game mode for human players
- 🤖 Algorithm comparison suite
- 📊 Performance visualization and statistics
- 🏃‍♂️ Batch testing capabilities
- 📈 Detailed analysis of each strategy's performance

## Getting Started 🚀

```bash
# Clone the repository
git clone https://github.com/username/mastermind.git

# Install dependencies
pip install -r requirements.txt

# Run the comparison suite
python compare_algorithms.py

# Play interactive game
python play_game.py
```

## Performance Metrics 📊

Algorithms are compared based on:

- Average number of guesses to solve
- Worst-case performance
- Distribution of solve times
- Memory usage
- Computational complexity

## Implementation Details 🛠️

Each algorithm is implemented as a separate strategy class inheriting from a base `MastermindSolver` interface:

```python
class MastermindSolver(ABC):
    @abstractmethod
    def make_guess(self, previous_guesses, previous_feedback):
        pass

    @abstractmethod
    def update_knowledge(self, guess, feedback):
        pass
```

## Future Enhancements 🔮

- [ ] Implement reinforcement learning approach
- [ ] Add distributed computing support for large-scale comparisons
- [ ] Create interactive web interface for visualization
- [ ] Add support for variable board sizes and color counts
- [ ] Implement real-time strategy comparison visualization

## Contributing 🤝

Contributions are welcome! Whether you want to:
- Implement a new solving strategy
- Improve existing algorithms
- Add visualization features
- Fix bugs or improve documentation

Please check out our [Contributing Guidelines](CONTRIBUTING.md).

## References 📚

1. Knuth, D. E. (1977). The Computer as Master Mind. Journal of Recreational Mathematics, 9(1), 1-6.
2. Kooi, B. (2005). Yet another Mastermind strategy. ICGA Journal, 28(1), 13-20.
3. Bestavros, A., & Belal, A. (1986). Mastermind: A game of diagnosis strategies. Bulletin of the Faculty of Engineering, Alexandria University, 25(3), 211-220.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created with 💡 by [Your Name] - Let's solve Mastermind together!
