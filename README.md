# Python-Chatbot
A simple Python chatbot built using if‑else statements, designed to simulate basic conversation and demonstrate control flow.
#  Build a Chatbot using if-else

## Description
This repository contains the submission for Task 8 of the Python Developer Internship. The objective was to create a simple rule-based chatbot using Python's control flow and loops.

The script simulates a basic conversation where the bot responds to specific user inputs (intents) using conditional logic.

## Features
* **Continuous Conversation:** Uses a `while` loop to keep the chat running until the user decides to exit.
* **Case Insensitivity:** Handles user input using the `.lower()` method to ensure commands like "Hello" and "hello" are treated the same.
* **Rule-Based Logic:** Uses `if-elif-else` statements to identify specific keywords (e.g., "weather", "name", "bye").
* **Graceful Exit:** Allows the user to stop the program by typing "bye" or "exit".

## How to Run
1.  Ensure you have Python installed.
2.  Clone this repository.
3.  Run the script using the command line:
    ```bash
    python chatbot.py
    ```

## Usage Example
```text
Chatbot: Hello! I am a simple rule-based chatbot.
You: Hello
Chatbot: Hi there! How can I help you today?
You: What is the weather?
Chatbot: I can't look outside, but it's always sunny in the digital world!
You: bye
Chatbot: Goodbye! Have a great day.
