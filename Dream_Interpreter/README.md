Prolog Dream Interpreter Expert System
A simple expert system for interpreting dream symbols and generating dream analysis, using Prolog for the knowledge base and inference engine.
Overview
This project combines Python and Prolog to create a dream interpretation system that:

Extracts recognized symbols from user dream descriptions
Uses a Prolog knowledge base to store dream symbol meanings
Queries the Prolog engine to get interpretations
Presents the results through a Python interface

Requirements

Python 3.6 or higher
SWI-Prolog: https://www.swi-prolog.org/download/stable
PySwip: pip install pyswip

Installation

Install SWI-Prolog for your operating system
Make sure SWI-Prolog is in your system PATH
Install PySwip: pip install pyswip
Clone or download this repository

Usage

Run the program:
Copypython main.py

Enter your dream description when prompted
Review the interpretation of symbols found in your dream
Continue with more dreams or type 'exit' to quit

Project Structure

main.py - Entry point for the application
knowledge_base.pl - Prolog database of dream symbols and interpretations
interpreter.py - Python interface to the Prolog inference engine
user_interface.py - Handles user interaction and display

How It Works

The Python interface extracts potential symbols from the dream description
These symbols are sent to the Prolog engine as queries
Prolog uses pattern matching and unification to find the relevant interpretations
The results are sent back to Python for formatting and display

Extending the System
To expand this mini project:

Add more symbols and interpretations to the Prolog knowledge base
Implement more sophisticated Prolog rules for complex reasoning
Add user feedback to refine interpretations over time
Create a graphical user interface
Implement more context-sensitivity in the interpretation rules