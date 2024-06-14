import tkinter as tk
from tkinter import messagebox
import string

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = ""
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.setup_ui()

    def setup_ui(self):
        self.intro_label = tk.Label(self.root, text="Player 1: Enter a word for Player 2 to guess")
        self.intro_label.pack()
        
        self.word_entry = tk.Entry(self.root, show="*")
        self.word_entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Submit Word", command=self.submit_word)
        self.submit_button.pack()

        self.word_frame = tk.Frame(self.root)
        
        self.display_label = tk.Label(self.word_frame, text="_ " * len(self.word))
        self.display_label.pack()

        self.letter_guess_entry = tk.Entry(self.word_frame)
        
        self.letter_guess_button = tk.Button(self.word_frame, text="Guess Letter", command=self.guess_letter)
        
        self.word_guess_entry = tk.Entry(self.word_frame)
        
        self.word_guess_button = tk.Button(self.word_frame, text="Guess Word", command=self.guess_word)

        self.incorrect_label = tk.Label(self.word_frame, text=f"Incorrect guesses left: {self.max_incorrect_guesses}")
        
        self.guessed_label = tk.Label(self.word_frame, text="Guessed letters: ")

        self.canvas = tk.Canvas(self.word_frame, width=200, height=200)
        self.canvas.pack()
        self.draw_hangman_structure()

    def submit_word(self):
        self.word = self.word_entry.get().lower()
        if not self.word.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid word (only letters).")
            return
        
        self.word_entry.pack_forget()
        self.submit_button.pack_forget()
        self.intro_label.pack_forget()
        
        self.word_frame.pack()
        self.display_label.config(text="_ " * len(self.word))
        self.letter_guess_entry.pack()
        self.letter_guess_button.pack()
        self.word_guess_entry.pack()
        self.word_guess_button.pack()
        self.incorrect_label.pack()
        self.guessed_label.pack()

    def display_word(self):
        displayed_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.display_label.config(text=displayed_word)

    def guess_letter(self):
        guess = self.letter_guess_entry.get().lower()
        self.letter_guess_entry.delete(0, tk.END)
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You have already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        self.guessed_label.config(text=f"Guessed letters: {' '.join(self.guessed_letters)}")

        if guess in self.word:
            self.display_word()
            if all(letter in self.guessed_letters for letter in self.word):
                messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word}")
                self.reset_game()
        else:
            self.incorrect_guesses += 1
            self.draw_next_hangman_part()
            self.incorrect_label.config(text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
            if self.incorrect_guesses == self.max_incorrect_guesses:
                messagebox.showinfo("Game Over", f"Game Over! The word was: {self.word}")
                self.reset_game()

    def guess_word(self):
        guess = self.word_guess_entry.get().lower()
        self.word_guess_entry.delete(0, tk.END)

        if guess == self.word:
            messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word}")
            self.reset_game()
        else:
            self.incorrect_guesses += 1
            self.draw_next_hangman_part()
            self.incorrect_label.config(text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
            if self.incorrect_guesses == self.max_incorrect_guesses:
                messagebox.showinfo("Game Over", f"Game Over! The word was: {self.word}")
                self.reset_game()

    def draw_hangman_structure(self):
        self.canvas.create_line(50, 180, 150, 180, width=2)  # Base
        self.canvas.create_line(100, 180, 100, 50, width=2)   # Pole
        self.canvas.create_line(100, 50, 150, 50, width=2)    # Top bar
        self.canvas.create_line(150, 50, 150, 70, width=2)    # Rope

    def draw_next_hangman_part(self):
        parts = [
            lambda: self.canvas.create_oval(140, 70, 160, 90, width=2),  # Head
            lambda: self.canvas.create_line(150, 90, 150, 130, width=2), # Body
            lambda: self.canvas.create_line(150, 100, 130, 110, width=2), # Left Arm
            lambda: self.canvas.create_line(150, 100, 170, 110, width=2), # Right Arm
            lambda: self.canvas.create_line(150, 130, 130, 160, width=2), # Left Leg
            lambda: self.canvas.create_line(150, 130, 170, 160, width=2)  # Right Leg
        ]

        if self.incorrect_guesses <= len(parts):
            parts[self.incorrect_guesses - 1]()

    def reset_game(self):
        self.word = ""
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.canvas.delete("all")
        self.draw_hangman_structure()

        self.word_frame.pack_forget()
        
        self.intro_label.pack()
        self.word_entry.pack()
        self.word_entry.delete(0, tk.END)
        self.submit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
