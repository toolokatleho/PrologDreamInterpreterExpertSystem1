import tkinter as tk
from tkinter import scrolledtext, messagebox

class DreamInterpreterGUI:
    def __init__(self, root, interpreter):
        self.root = root
        self.interpreter = interpreter
        self.root.title("Dream Interpreter 🌙")
        self.root.geometry("600x400")
        self.root.configure(bg="#282c34")

        # Title Label
        self.title_label = tk.Label(root, text="🌙 Dream Interpreter Expert System 🌙", 
                                    font=("Arial", 14, "bold"), fg="white", bg="#282c34")
        self.title_label.pack(pady=10)

        # Input Area
        self.dream_entry_label = tk.Label(root, text="Describe Your Dream:", 
                                          font=("Arial", 12), fg="white", bg="#282c34")
        self.dream_entry_label.pack()
        
        self.dream_entry = tk.Entry(root, width=60, font=("Arial", 12))
        self.dream_entry.pack(pady=5)

        # Interpret Button
        self.interpret_button = tk.Button(root, text="🔮 Analyze Dream", 
                                          command=self.analyze_dream, 
                                          font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
        self.interpret_button.pack(pady=10)

        # Output Area (Scrollable)
        self.result_text = scrolledtext.ScrolledText(root, width=70, height=10, 
                                                     font=("Arial", 12), wrap=tk.WORD, bg="#4CAF50")
        self.result_text.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", 
                                     command=root.quit, 
                                     font=("Arial", 12, "bold"), bg="red", fg="white")
        self.exit_button.pack(pady=10)

    def analyze_dream(self):
        """Handles the dream analysis and displays results."""
        dream_description = self.dream_entry.get().strip()
        
        if not dream_description:
            messagebox.showwarning("Input Error", "Please enter a dream description!")
            return

        results = self.interpreter.interpret_dream(dream_description)

        # Display results in output area
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "🔮 DREAM ANALYSIS 🔮\n")
        self.result_text.insert(tk.END, "-"*50 + "\n")
        
        if not results["symbols"]:
            self.result_text.insert(tk.END, results["overall"] + "\n")
        else:
            self.result_text.insert(tk.END, "🔑 SYMBOLS DETECTED:\n")
            for symbol in results["symbols"]:
                self.result_text.insert(tk.END, f"  • {symbol}\n")
            
            self.result_text.insert(tk.END, "\n📝 INTERPRETATION:\n")
            self.result_text.insert(tk.END, results["overall"] + "\n")
        
        self.result_text.insert(tk.END, "-"*50 + "\nRemember: Dream interpretations are subjective. Trust your intuition!\n")

