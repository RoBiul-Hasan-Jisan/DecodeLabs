
"""
Entry point for the Rule-Based AI Chatbot
DecodeLabs - Project 1
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot.bot import RuleBasedChatbot

def main():
    """Main function to run the chatbot"""
    try:
        # Create and run chatbot instance
        chatbot = RuleBasedChatbot()
        chatbot.run()
        
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()