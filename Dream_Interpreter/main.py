"""
Main entry point for the Dream Interpreter Expert System.
Integrates Python with Prolog for dream interpretation.

"""
from tkinter import Tk
from gui_interface import DreamInterpreterGUI
from interpreter import DreamInterpreter
from user_interface import DreamInterpreterUI

def main():
    try:
        # Initialize the interpreter with Prolog integration
        interpreter = DreamInterpreter()
        
        # Initialize the user interface
        ui = DreamInterpreterUI(interpreter)
        
        # Start the interface
        ui.start_interface()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have installed the required dependencies:")
        print("1. SWI-Prolog: https://www.swi-prolog.org/download/stable")
        print("2. PySwip: pip install pyswip")

if __name__ == "__main__":
    root = Tk()
    interpreter = DreamInterpreter()
    app = DreamInterpreterGUI(root, interpreter)
    root.mainloop()
