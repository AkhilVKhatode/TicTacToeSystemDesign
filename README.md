# TicTacToeSystemDesign

This project is a simple command-line implementation of the classic **Tic-Tac-Toe** game using object-oriented design in Python. It showcases clean modular code with separate classes for the game board, players, and game flow.

## Features

- Interactive 2-player game via terminal
- Modular class-based architecture
- Input validation and error handling
- Detects wins, draws, and invalid moves

## Class Structure

- **Board**
  - Initializes and manages the 3x3 grid
  - Updates board state
  - Checks for a winner or full board
- **Player**
  - Accepts input from the user
  - Ensures valid moves
- **Game**
  - Controls game flow
  - Alternates turns between players
  - Handles win/draw announcements
