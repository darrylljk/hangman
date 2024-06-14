import tkinter as tk
from tkinter import messagebox
import string

class HangmanGame:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to the Hangman Game")
        self.word = ""
        self.guessesd_letters = set()
