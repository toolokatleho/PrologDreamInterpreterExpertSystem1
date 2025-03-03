"""
Core interpretation logic for the Dream Interpreter system.
Interfaces with the Prolog knowledge base to interpret dreams.
"""

import os
from pyswip import Prolog
import re

class DreamInterpreter:
    def __init__(self):
        self.prolog = Prolog()
        # Load the knowledge base
        # Change directory to script directory first
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        # Then consult using a relative path
        self.prolog.consult("knowledge_base.pl")

         # Fix for Windows paths - convert backslashes to forward slashes
         # kb_path = kb_path.replace("\\", "//")

        # Use raw string to properly handle Windows paths
        #self.prolog.consult(r"{}".format(kb_path))
        
        # Extract all symbols from the knowledge base
        self.symbols = self._extract_symbols()
        
    def _extract_symbols(self):
        # Extract all unique symbols from the Prolog knowledge base
        query = list(self.prolog.query("symbol(Symbol, _, _)"))
        symbols = set()
        for result in query:
            symbols.add(result["Symbol"].decode() if isinstance(result["Symbol"], bytes) 
                        else result["Symbol"])
        return symbols
        
    def extract_symbols(self, dream_description):
        """
        Extract known symbols from the dream description.
        
        Args:
            dream_description (str): User's dream description
            
        Returns:
            dict: Dictionary of symbols and their contexts
        """
        dream_description = dream_description.lower()
        found_symbols = {}
        
        # Check for each symbol in the description
        for symbol in self.symbols:
            # For multi-word symbols, replace underscores with spaces for matching
            search_symbol = symbol.replace('_', ' ')
            
            if search_symbol in dream_description:
                # Try to find context (words around the symbol)
                symbol_index = dream_description.find(search_symbol)
                start = max(0, symbol_index - 20)
                end = min(len(dream_description), symbol_index + len(search_symbol) + 20)
                context = dream_description[start:end]
                
                # Determine the context type
                context_type = self._determine_context(search_symbol, context)
                found_symbols[symbol] = context_type
                
        return found_symbols
    
    def _determine_context(self, symbol, context):
        """
        Determine the context type for a symbol based on surrounding text.
        
        Args:
            symbol (str): The symbol to analyze
            context (str): The context around the symbol
            
        Returns:
            str: The determined context type
        """
        # Simple rule-based context determination
        context_types = {
            "water": {
                "calm": ["calm", "peaceful", "still", "quiet"],
                "rough": ["rough", "turbulent", "stormy", "violent"],
                "rising": ["rising", "flooding", "overflow"]
            },
            "fire": {
                "controlled": ["controlled", "campfire", "fireplace", "candle"],
                "destructive": ["destructive", "wildfire", "burning", "out of control"],
                "warming": ["warming", "cozy", "comfort"]
            },
            "bird": {
                "flying": ["flying", "soaring", "sky"],
                "caged": ["caged", "trapped", "confined"]
            },
            "dog": {
                "friendly": ["friendly", "wagging", "playful"],
                "aggressive": ["aggressive", "barking", "biting", "growling"]
            },
            "house": {
                "familiar": ["familiar", "my", "home", "own"],
                "unfamiliar": ["unfamiliar", "strange", "unknown"]
            },
            "car": {
                "driving": ["driving", "steering", "control"],
                "passenger": ["passenger", "sitting", "not driving"],
                "broken": ["broken", "stalled", "crashed", "accident"]
            },
            "door": {
                "open": ["open", "opened", "opening"],
                "locked": ["locked", "closed", "shut", "wouldn't open"]
            },
            "running": {
                "chased": ["chased", "pursued", "following", "after me"],
                "exercise": ["exercise", "jogging", "track"]
            }
        }
        
        # Check if we have context rules for this symbol
        symbol_contexts = context_types.get(symbol)
        if not symbol_contexts:
            return "_"  # Default wildcard context
            
        # Check each context type
        for context_type, keywords in symbol_contexts.items():
            for keyword in keywords:
                if keyword in context:
                    return context_type
                    
        return "_"  # Default wildcard context
    
    def interpret_dream(self, dream_description):
        """
        Generate an interpretation based on the dream description.
        
        Args:
            dream_description (str): User's dream description
            
        Returns:
            dict: Dictionary containing extracted symbols and overall interpretation
        """
        extracted_symbols = self.extract_symbols(dream_description)
        
        if not extracted_symbols:
            return {
                "symbols": [],
                "interpretations": [],
                "overall": "I couldn't identify specific symbols in your dream. Please provide more details."
            }
        
        # Get interpretations for each symbol using Prolog queries
        interpretations = []
        for symbol, context in extracted_symbols.items():
            # Query the Prolog knowledge base
            query = f"interpret({symbol}, {context}, Interpretation)"
            results = list(self.prolog.query(query))
            
            if results:
                meaning = results[0]["Interpretation"]
                # Decode if bytes
                if isinstance(meaning, bytes):
                    meaning = meaning.decode()
                
                interpretations.append({
                    "symbol": symbol.replace('_', ' '),
                    "interpretation": meaning
                })
        
        # Generate overall interpretation
        if len(interpretations) == 1:
            symbol = interpretations[0]['symbol']
            interp = interpretations[0]['interpretation'].lower()
            overall = f"Your dream about {symbol} suggests {interp}."
        else:
            overall = "Your dream contains several symbols:\n"
            for item in interpretations:
                overall += f"- The {item['symbol']} suggests {item['interpretation'].lower()}.\n"
            overall += "\nThese symbols together might indicate you're processing emotions or situations related to " 
            overall += "these themes in your waking life."
        
        return {
            "symbols": [s.replace('_', ' ') for s in extracted_symbols.keys()],
            "interpretations": interpretations,
            "overall": overall
        }