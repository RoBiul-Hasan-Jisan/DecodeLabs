"""
Main chatbot class that orchestrates the rule-based system
"""

import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from chatbot.rules import RuleEngine
from chatbot.utils import Logger, ResponseLoader

class RuleBasedChatbot:
    """Main chatbot class"""
    
    def __init__(self):
        """Initialize the chatbot with all components"""
        self.config = config
        self.rule_engine = RuleEngine(self.config)
        self.response_loader = ResponseLoader(self.config.RESPONSES_FILE)
        self.logger = Logger(self.config.LOG_FILE_PATH) if self.config.ENABLE_LOGGING else None
        self.running = True
    
    def display_welcome(self):
        """Display welcome message"""
        welcome_art = """
   
                 RULE-BASED AI CHATBOT              
                DecodeLabs - Project 1               
        
        """
        print(welcome_art)
        print(f"🤖 {self.config.BOT_NAME}: Hello! I'm your Rule-Based AI Assistant.")
        print(f"   Version {self.config.BOT_VERSION}")
        print(f"   Type 'bye', 'exit', or 'quit' to end the conversation.\n")
    
    def get_response(self, user_input: str) -> str:
        """
        Generate response based on rule-based classification
        """
        # Classify intent
        intent, matched_pattern = self.rule_engine.classify_intent(user_input)
        
        # Handle exit intent specially
        if intent == "exit":
            self.running = False
            return "Goodbye! Have a great day. "
        
        # Get response for intent
        response = self.rule_engine.get_response_for_intent(intent, self.response_loader)
        
        return response
    
    def process_input(self, user_input: str) -> str:
        """
        Process user input and return bot response
        """
        if not user_input or not user_input.strip():
            return "I didn't catch that. Could you say something?"
        
        response = self.get_response(user_input)
        
        # Log conversation
        if self.logger:
            self.logger.log(user_input, response)
        
        return response
    
    def run(self):
        """Main execution loop"""
        self.display_welcome()
        
        while self.running:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Process input and get response
                response = self.process_input(user_input)
                
                # Display response
                print(f"🤖 {self.config.BOT_NAME}: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Chatbot: Goodbye! 👋")
                break
            except EOFError:
                print("\n🤖 Chatbot: Goodbye! 👋")
                break
            except Exception as e:
                print(f"⚠️ An error occurred: {e}")
                print("🤖 Chatbot: Let's continue our conversation.\n")
    
    def get_stats(self):
        """Display bot statistics"""
        if self.logger:
            history = self.logger.get_conversation_history()
            print(f"\n📊 Total interactions logged: {len(history)//2}")
        else:
            print("📊 Logging is disabled.")