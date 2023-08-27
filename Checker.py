import tkinter as tk
from tkinter import scrolledtext, messagebox
import difflib

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")

        self.setup_ui()

    def setup_ui(self):
        self.original_text_label = tk.Label(self.root, text="Original Text:")
        self.original_text_label.pack()

        self.original_text = scrolledtext.ScrolledText(self.root, height=5, wrap=tk.WORD)
        self.original_text.pack()

        self.submitted_text_label = tk.Label(self.root, text="Submitted Text:")
        self.submitted_text_label.pack()

        self.submitted_text = scrolledtext.ScrolledText(self.root, height=5, wrap=tk.WORD)
        self.submitted_text.pack()

        self.check_button = tk.Button(self.root, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.pack()

    def calculate_similarity(self, text1, text2):
        similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
        return similarity_ratio

    def check_plagiarism(self):
        original_text = self.original_text.get("1.0", tk.END)
        submitted_text = self.submitted_text.get("1.0", tk.END)

        similarity = self.calculate_similarity(original_text, submitted_text)
        threshold = 0.8

        if similarity >= threshold:
            result = "Plagiarism detected!\nSimilarity: {:.2f}".format(similarity)
        else:
            result = "No plagiarism detected.\nSimilarity: {:.2f}".format(similarity)

        messagebox.showinfo("Plagiarism Check Result", result)

def main():
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
