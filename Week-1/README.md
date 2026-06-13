#  Rule-Based AI Chatbot - DecodeLabs Project 1

##  Overview
A production-ready rule-based chatbot that simulates basic human interaction through pure programmatic if-else decision-making.

##  Features
-  Handles greetings and exit commands
-  Pure if-else rule-based logic (no ML)
-  Continuous conversation loop
-  Conversation logging
-  Extensible rule system
-  Comprehensive test suite

##  Project Structure
```bash
rule-based-chatbot/
│
├── chatbot/
│   ├── __init__.py
│   ├── bot.py              # Main chatbot logic
│   ├── rules.py            # Rule definitions and responses
│   └── utils.py            # Helper functions
│
├── data/
│   └── responses.json      # External response database
│
├── tests/
│   ├── __init__.py
│   ├── test_bot.py         # Unit tests
│   └── test_rules.py
│
├── logs/
│   └── conversation.log    # Auto-generated chat logs
│
├── main.py                 # Entry point
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
├── README.md              # Documentation
└── .gitignore             # Git ignore file

```
---


##  Quick Start

### Installation
```bash
# Clone or download the project
cd rule-based-chatbot

```
---
### Run the Chatbot
```bash
python main.py
```

### Run Tests
```bash

python -m unittest discover tests

```

---

## Example Conversation

``` bash
You: hello
Bot: Hello there! How can I help you today?

You: how are you
Bot: I'm just a bunch of rules, but I'm functioning perfectly! 

You: tell me a joke
Bot: Why did the programmer quit his job? Because he didn't get arrays! 

You: bye
Bot: Goodbye! Have a great day. 

```

---

## Extending the Bot
### Adding New Rules

1.Open data/responses.json

2.Add new intent category with responses

3.Update classify_intent() in chatbot/rules.py


## How to Run

```bash
# 1. Create the project structure
mkdir -p rule-based-chatbot/{chatbot,data,tests,logs}

# 2. Copy all the files into their respective directories

# 3. Navigate to project root
cd rule-based-chatbot

# 4. Run the chatbot
python main.py

# 5. Run tests (optional)
python -m unittest discover tests -v
```
---

## Qualification Checklist

| Requirement            | Status      | Implementation                                                     |
| ---------------------- | ----------- | ------------------------------------------------------------------ |
| Handle greetings       |   Completed | Implemented greeting intent detection                              |
| Handle exit commands   |   Completed | Implemented exit intent handling                                   |
| If-else logic          |   Completed | Used `classify_intent()` method for rule-based decision making     |
| Continuous loop        |   Completed | Maintained conversation flow using `while self.running` loop       |
| Professional structure |   Completed | Built with modular design, testing, and documentation              |
| No deep learning       |   Completed | Developed using a pure rule-based approach without neural networks |
