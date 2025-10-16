# Tic-Tac-Toe Game 🎮

A simple yet engaging terminal-based Tic-Tac-Toe game where you compete against the computer. Challenge your strategy skills and see if you can outsmart the AI!

## Features ✨

- **Player vs Computer Gameplay** - Test your skills against a computer opponent
- **Complete Game Logic** - Detects wins, losses, and draws automatically
- **Input Validation** - Prevents invalid moves and out-of-range selections
- **Clean Terminal UX** - Strategic screen clearing keeps the gameplay smooth and clutter-free
- **Replay Functionality** - Play multiple rounds without restarting the program
- **Error Handling** - Robust exception handling for user inputs

## How to Play 🕹️

1. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

2. Choose your symbol: **X** or **O**

3. Press Enter to start the game

4. When it's your turn, enter a number from **1-9** to place your symbol:
   ```
   +-------+-------+-------+
   |       |       |       |
   |   1   |   2   |   3   |
   |       |       |       |
   +-------+-------+-------+
   |       |       |       |
   |   4   |   5   |   6   |
   |       |       |       |
   +-------+-------+-------+
   |       |       |       |
   |   7   |   8   |   9   |
   |       |       |       |
   +-------+-------+-------+
   ```

5. The computer will make its move automatically

6. First to get three in a row (horizontally, vertically, or diagonally) wins!

7. Play again or exit when the game ends

## Game Rules 📋

- The game board has 9 positions (numbered 1-9)
- Players alternate turns: Computer → You → Computer → You...
- The game ends after 4 rounds (8 moves total) if no winner is found
- Win by getting three of your symbols in a row, column, or diagonal
- If all 9 positions are filled with no winner, it's a draw

## Requirements 📦

- Python 3.x
- No external dependencies required (uses only standard library)

## File Structure 📁

```
tic-tac-toe/
│
├── tic-tac-toe.py      # Main game file
└── README.md           # This file
```

## Game Flow 🔄

```
Start Game
    ↓
Choose X or O
    ↓
Computer plays
    ↓
Check for winner?
    ├─ Yes → End Game (Win/Loss)
    └─ No → Your turn
         ↓
    You play
         ↓
    Check for winner?
         ├─ Yes → End Game (Win/Loss/Draw)
         └─ No → Repeat
             ↓
        Play Again? → Yes: Restart | No: Exit
```

## Future Enhancements 🚀

- **AI Strategy** - Implement intelligent computer moves instead of random selection
- **Difficulty Levels** - Easy, Medium, and Hard modes with varying AI behavior
- **Game Statistics** - Track wins, losses, and draws across sessions
- **Enhanced UI** - Better visual design with colors and animations
- **Score Leaderboard** - Keep a running score of player performance

## Technical Details 🔧

### Key Functions

| Function | Purpose |
|----------|---------|
| `clearScreen()` | Clears terminal for better UX |
| `drawBoard()` | Displays the current game board |
| `computer()` | Computer makes a move |
| `player()` | Handles player input and validation |
| `winner()` | Checks for winning conditions |
| `freeFields()` | Returns list of available board positions |
| `playGame()` | Main game loop |

### Winning Combinations

The game checks 8 possible winning combinations:
- 3 rows
- 3 columns
- 2 diagonals

## Known Limitations ⚠️

- Computer plays randomly (no strategy)
- Single-player only (no player vs player mode)
- No persistent game history

## Tips to Win 💡

- Control the center (position 5) - it's part of 4 winning combinations
- Watch for the computer's threats and block them
- Set up multiple winning opportunities ("forks") when possible
- Pay attention to corners - they're part of 3 winning combinations each

## License 📄

This project is open source and free to use.

---

**Enjoy the game and have fun! 🎯**