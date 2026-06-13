"""
Unit tests for the RuleBasedChatbot
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.bot import RuleBasedChatbot

class TestRuleBasedChatbot(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.chatbot = RuleBasedChatbot()
    
    def test_greeting_responses(self):
        """Test various greeting inputs"""
        greetings = ['hello', 'hi', 'hey', 'greetings', 'howdy']
        for greeting in greetings:
            response = self.chatbot.get_response(greeting)
            self.assertIsNotNone(response)
            self.assertNotEqual(response, self.chatbot.config.DEFAULT_RESPONSE)
    
    def test_exit_commands(self):
        """Test exit commands"""
        exit_commands = ['bye', 'exit', 'quit', 'goodbye']
        for cmd in exit_commands:
            response = self.chatbot.get_response(cmd)
            self.assertIn("Goodbye", response)
            self.assertFalse(self.chatbot.running)
            self.chatbot.running = True  # Reset for next test
    
    def test_help_command(self):
        """Test help command"""
        response = self.chatbot.get_response('help')
        self.assertIsNotNone(response)
    
    def test_thanks_response(self):
        """Test thank you responses"""
        response = self.chatbot.get_response('thank you')
        self.assertIn("welcome", response.lower())
    
    def test_empty_input(self):
        """Test empty input handling"""
        response = self.chatbot.process_input("")
        self.assertIsNotNone(response)
    
    def test_default_response(self):
        """Test unknown input returns default response"""
        response = self.chatbot.get_response("asdfghjkl123456")
        self.assertEqual(response, "I'm not sure how to respond to that.")

if __name__ == "__main__":
    unittest.main()