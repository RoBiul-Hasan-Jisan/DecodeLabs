"""
Unit tests for RuleEngine
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from chatbot.rules import RuleEngine

class TestRuleEngine(unittest.TestCase):
    
    def setUp(self):
        self.rule_engine = RuleEngine(config)
    
    def test_classify_greeting(self):
        """Test greeting classification"""
        intent, _ = self.rule_engine.classify_intent("hello")
        self.assertEqual(intent, "greeting")
        
        intent, _ = self.rule_engine.classify_intent("hey there")
        self.assertEqual(intent, "greeting")
    
    def test_classify_exit(self):
        """Test exit classification"""
        intent, _ = self.rule_engine.classify_intent("bye")
        self.assertEqual(intent, "exit")
        
        intent, _ = self.rule_engine.classify_intent("goodbye")
        self.assertEqual(intent, "exit")
    
    def test_classify_how_are_you(self):
        """Test how are you classification"""
        intent, _ = self.rule_engine.classify_intent("how are you")
        self.assertEqual(intent, "how_are_you")
    
    def test_classify_name_question(self):
        """Test name question classification"""
        intent, _ = self.rule_engine.classify_intent("what is your name")
        self.assertEqual(intent, "name_question")

if __name__ == "__main__":
    unittest.main()