"""
Rule-based decision engine for the chatbot
"""

import re
from typing import Tuple, Optional

class RuleEngine:
    """Handles all rule-based matching and decision making"""
    
    def __init__(self, config):
        self.config = config
        self.exit_keywords = config.EXIT_KEYWORDS
        self.greeting_keywords = config.GREETING_KEYWORDS
    
    def classify_intent(self, user_input: str) -> Tuple[str, Optional[str]]:
        """
        Classify user input into intent categories
        Returns: (intent, matched_pattern)
        """
        user_input = user_input.lower().strip()
        
        # Exit intent
        if any(keyword in user_input for keyword in self.exit_keywords):
            return "exit", None
        
        # Greeting intent
        if any(keyword in user_input for keyword in self.greeting_keywords):
            return "greeting", None
        
        # How are you intent
        if re.search(r'how are you|how\'s it going|how do you do', user_input):
            return "how_are_you", None
        
        # Name question intent
        if re.search(r'what is your name|who are you|your name', user_input):
            return "name_question", None
        
        # Help intent
        if any(word in user_input for word in ['help', 'commands', 'what can you do']):
            return "help", None
        
        # Thank you intent
        if 'thank' in user_input or 'thanks' in user_input:
            return "thanks", None
        
        # Weather intent
        if 'weather' in user_input or 'temperature' in user_input:
            return "weather", None
        
        # Time intent
        if 'time' in user_input or 'clock' in user_input:
            return "time", None
        
        # Funny/joke intent
        if any(word in user_input for word in ['joke', 'funny', 'laugh']):
            return "funny", None
        
        # Default intent
        return "default", None
    
    def get_response_for_intent(self, intent: str, response_loader) -> str:
        """Get appropriate response based on intent"""
        return response_loader.get_response(intent)