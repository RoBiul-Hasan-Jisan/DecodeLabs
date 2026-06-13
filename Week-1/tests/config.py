"""
Configuration settings for the Rule-Based Chatbot
"""

# Bot settings
BOT_NAME = "DecodeBot"
BOT_VERSION = "1.0.0"

# Exit keywords (case-insensitive)
EXIT_KEYWORDS = ['bye', 'exit', 'quit', 'goodbye', 'see you', 'cya']

# Greeting keywords
GREETING_KEYWORDS = ['hello', 'hi', 'hey', 'greetings', 'sup', 'howdy']

# Conversation settings
ENABLE_LOGGING = True
LOG_FILE_PATH = "logs/conversation.log"

# Response settings
DEFAULT_RESPONSE = "I'm not sure how to respond to that yet. Try saying 'hello' or 'help'."

# File paths
RESPONSES_FILE = "data/responses.json"