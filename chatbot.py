import datetime
import random
import string 

def get_current_time():
    """Return the current time."""
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%I:%M:%S %p")


def get_current_date():
    """Return today's date."""
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%d-%m-%Y")

greeting_responses = [
    "Hello! How can I help you?",
    "Hi there! What can I do for you?",
    "Hey! Nice to chat with you."
    ]

thank_responses = [
    "You're welcome!",
    "Glad I could help!",
    "Anytime!"
    ]

sad_responses = [
    "I'm sorry to hear that. I hope things get better.",
    "I hope you feel better soon.",
    "I'm here if you want to talk."
    ]

def get_response(message, name):
    """Return a response based on the user's message."""

    words = message.split()

    if message in [
    "bye",
    "goodbye",
    "quit",
    "exit",
    "see you",
    "see ya",
    "talk to you later"
    ]:
        return "Goodbye! Have a great day!"

    elif "hi" in words or "hello" in words or "hey" in words:
        return random.choice(greeting_responses)

    elif "good" in message and (
            "morning" in message
            or "afternoon" in message
            or "evening" in message
        ):
        return "Good to see you! How can I help you?"

    elif "good" in message and "night" in message:
        return "Good night! Have a great day tomorrow!"

    elif "my" in message and "name" in message:
        return f"Your name is {name}."

    elif (
            ("name" in message and "your" in message)
            or ("who" in message and "you" in message)
        ):
        return "My name is SimpleBot. I'm a rule-based chatbot."

    elif (
            ("how" in message and "are" in message and "you" in message)
            or ("are" in message and "you" in message and "okay" in message)
        ):
        return "I'm doing great! Thanks for asking."

    elif ("im" in words or ("i" in words and "am" in words)) and (
        "good" in words or "fine" in words
        ):
         return "That's great to hear! How can I help you?" 

    elif "sad" in words or "unhappy" in words or "upset" in words:
        return random.choice(sad_responses)

    elif (
            ("help" in message and "me" in message)
            or ("what" in message and "do" in message)
            or "capabilities" in message
        ):
        return "I can answer simple questions based on my predefined rules."

    elif "time" in message and (
    "what" in message
    or "whats" in message
    or "current" in message
    or "tell" in message
    ):
        return f"The current time is {get_current_time()}"

    elif "date" in message and (
        "what" in message
        or "today" in message
        or "current" in message
        or "whats" in message
    ):
        return f"Today's date is {get_current_date()}"

    elif "thanks" in message or "thank" in message:
        return random.choice(thank_responses)

    elif message in ["yes", "yeah", "yep", "sure", "of course"]:
        return "Great! I'm glad to hear that."

    elif message in ["no", "nope", "nah"]:
        return "That's okay!"

    else:
        return (
    "I'm sorry, I don't understand that yet. "
    "You can ask about my name, capabilities, date, time, or just chat with me."
    )
    

def main():
    """Run the SimpleBot chatbot."""
    name = input("Bot: What is your name? ")

    print("You:", name)
    print(f"Bot: You said {name}")

    print("Bot: I am ready to chat!")

    message = ""

    while message not in [
        "bye",
        "goodbye",
        "quit",
        "exit",
        "see you",
        "see ya",
        "talk to you later"
    ]:
        message = input("You: ").strip().lower()

        message = message.translate(
            str.maketrans("", "", string.punctuation)
        )

        response = get_response(message, name)

        print(f"Bot: {response}")

if __name__ == "__main__":
    main()