"""
Utility functions for the chatbot
"""

import json
import random
import os
from datetime import datetime
from typing import Dict, List, Any

class Logger:
    """Handles conversation logging"""
    
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self._ensure_log_directory()
    
    def _ensure_log_directory(self):
        """Create logs directory if it doesn't exist"""
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
    
    def log(self, user_input: str, bot_response: str):
        """Log conversation to file"""
        try:
            with open(self.log_file_path, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] User: {user_input}\n")
                f.write(f"[{timestamp}] Bot: {bot_response}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Warning: Could not write to log file - {e}")
    
    def get_conversation_history(self) -> List[str]:
        """Read conversation history from log file"""
        if not os.path.exists(self.log_file_path):
            return []
        
        with open(self.log_file_path, 'r', encoding='utf-8') as f:
            return f.readlines()

class ResponseLoader:
    """Loads and manages responses from JSON file"""
    
    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path
        self.responses = self._load_responses()
    
    def _load_responses(self) -> Dict[str, List[str]]:
        """Load responses from JSON file"""
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {self.json_file_path} not found. Using empty responses.")
            return {}
        except json.JSONDecodeError:
            print(f"Warning: {self.json_file_path} is not valid JSON. Using empty responses.")
            return {}
    
    def get_response(self, category: str) -> str:
        """Get random response from a category"""
        if category in self.responses and self.responses[category]:
            return random.choice(self.responses[category])
        return "I'm not sure how to respond to that."