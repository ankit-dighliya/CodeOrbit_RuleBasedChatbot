# 🤖 SimpleBot — Rule-Based Chatbot

A beginner-friendly rule-based chatbot built with Python. SimpleBot uses conditional statements, string processing, functions, lists, and random responses to interact with users through the terminal.

This project was created to practice Python programming concepts and strengthen problem-solving and logical thinking skills.

---

## 📌 Project Overview

SimpleBot is a command-line chatbot that responds to user messages based on predefined rules.

It can recognize common conversations such as greetings, questions about its name and capabilities, date and time requests, feelings, thank-you messages, and farewell commands.

The chatbot does not use Artificial Intelligence or Machine Learning. It follows predefined rules written using Python.

---

## ✨ Features

- 👋 Responds to greetings
- 🌅 Handles good morning, afternoon, and evening messages
- 🌙 Responds to good night messages
- 🧑 Remembers and responds with the user's name
- 🤖 Explains its identity and capabilities
- 😊 Responds to "How are you?" type questions
- 👍 Understands simple positive responses
- 😔 Responds to simple negative/sad messages
- 🕐 Provides the current time
- 📅 Provides the current date
- 🙏 Gives randomized responses to thank-you messages
- 🎲 Gives randomized greeting responses
- 👋 Supports multiple farewell commands
- 🧹 Removes punctuation from user input
- 🔄 Continues conversation using a `while` loop
- ❓ Provides a fallback response for unknown messages

---

## 🛠️ Technologies Used

- **Python 3**
- `datetime` — for current date and time
- `random` — for randomized responses
- `string` — for punctuation handling

---

## 🧠 Python Concepts Practiced

This project helped practice several important Python concepts:

- Variables
- Strings and string methods
- Lists
- `if`, `elif`, and `else`
- `while` loops
- Functions
- Function parameters and return values
- String splitting with `split()`
- Boolean operators (`and`, `or`)
- Membership operators (`in`)
- `random.choice()`
- `datetime`
- String formatting
- `translate()` and `str.maketrans()`
- Code organization with `main()`
- `if __name__ == "__main__"`

---

## ⚙️ How It Works

The chatbot follows a simple rule-based approach:

```text
User Input
    ↓
Clean Input
    ↓
Split Message into Words
    ↓
Check Predefined Rules
    ↓
Find Matching Condition
    ↓
Generate Response
    ↓
Display Response



📂 Project Structure
CodeOrbit_RuleBasedChatbot/
│
├── .gitignore
├── chatbot.py
└── README.md




👨‍💻 Author

Ankit Kumar

B.Tech — Artificial Intelligence & Machine Learning

This project was created as part of my Python learning and problem-solving practice.