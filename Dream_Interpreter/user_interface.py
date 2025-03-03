"""
Simple text-based user interface for the Dream Interpreter system.
"""

class DreamInterpreterUI:
    def __init__(self, interpreter):
        self.interpreter = interpreter
    
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("\n" + "="*60)
        print("🌙 PROLOG DREAM INTERPRETER EXPERT SYSTEM 🌙".center(60))
        print("="*60)
        print("\nWelcome to the Dream Interpreter!")
        print("Describe your dream in detail, and I'll analyze the symbols.")
        print("Type 'exit' to quit the program.\n")
    
    def display_interpretation(self, results):
        """
        Display the interpretation results in a formatted way.
        
        Args:
            results (dict): The interpretation results from the interpreter
        """
        print("\n" + "-"*60)
        print("🔮 DREAM ANALYSIS 🔮".center(60))
        print("-"*60)
        
        if not results["symbols"]:
            print("\n" + results["overall"])
            return
        
        print("\n🔑 SYMBOLS DETECTED:")
        for symbol in results["symbols"]:
            print(f"  • {symbol}")
        
        print("\n📝 INTERPRETATION:")
        print(results["overall"])
        print("\n" + "-"*60)
        print("Remember: Dream interpretations are subjective. Trust your intuition!")
        print("-"*60 + "\n")
    
    def start_interface(self):
        """Start the interactive interface loop"""
        self.display_welcome()
        
        while True:
            dream_description = input("Describe your dream (or type 'exit'): ")
            
            if dream_description.lower() == 'exit':
                print("\nThank you for using the Dream Interpreter. Goodbye!")
                break
                
            if not dream_description.strip():
                print("Please enter a dream description.")
                continue
                
            results = self.interpreter.interpret_dream(dream_description)
            self.display_interpretation(results)