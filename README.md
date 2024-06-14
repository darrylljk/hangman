# Hangman Game

Welcome to the Hangman Game! This is a classic two-player game where Player 1 sets a word, and Player 2 tries to guess it. With each incorrect guess, a part of the hangman is drawn. The game ends when Player 2 correctly guesses the word or the hangman is fully drawn.

## Features

- **Two-Player Mode**: Player 1 sets the word, and Player 2 guesses it.
- **Graphical Representation**: Incorrect guesses result in parts of the hangman being drawn on the canvas.
- **Real-Time Feedback**: The current state of the word and guessed letters are displayed after each guess.
- **Word and Letter Guessing**: Player 2 can guess individual letters or the entire word.

## Requirements

- Python 3.x
- `tkinter` (part of the standard Python library)

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/hangman.git
    cd hangman
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    ```

3. **Install Required Packages**:
    ```sh
    pip install tkinter
    ```

## Running the Game

To start the game, run the following command:
```sh
python hangman.py
