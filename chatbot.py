import datetime

def get_current_time():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()
    return current_time

def get_current_date():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    return current_date


name = input("Bot: What is your name? ")

print("You:", name)
print(f"Bot: You said {name}")


print("Bot: I am ready to chat!")

message = ""

while not (message in ["bye", "goodbye", "quit", "exit"]):

    message = input("You: ").strip().lower()

    # response = get_response(message)

# print(response)

    if message in ["bye", "goodbye", "quit", "exit"]:
        print("Goodbye! Have a great day!")

    # elif "hi" in words or "hello" in words or "hey" in words:
        print("Bot: Hello! How can I help you?")

    elif message in ["what is your name", "what's your name", "who are you", "your name"]:
        print("Bot: My name is SimpleBot. I'm a rule-based chatbot.")

    elif message in ["how are you", "how are you doing", "are you okay"]:
        print("Bot: I'm doing great! Thanks for asking.")

    elif message in ["what can you do", "what are your capabilities", "help me", "what do you do"]:
        print("Bot: I can answer simple questions based on my predefined rules.")

    elif message in ["what is the time", "what time is it", "current time"]:
        result_time = get_current_time()
        print(f"Bot: The current time is {result_time}")

    elif message in ["what is today's date", "what is the date", "today's date", "current date"]:
        result_date = get_current_date()
        print(f"Bot: Today's date is {result_date}")

    elif "thanks" in message or "thank" in message:
        print("You're welcome!")

    else:
        print("Bot: I'm sorry, I don't understand that yet. Try asking about my name, capabilities, date, or time.")



def get_response(message):
    words = message.split()

    if message in ["bye", "goodbye", "quit", "exit"]:
        return "Goodbye! Have a great day!"
    elif "hi" in words or "hello" in words or "hey" in words:
        return "Hello! How can I help you?"
    elif message in ["what is your name", "what's your name", "who are you", "your name"]:
        return "My name is SimpleBot. I'm a rule-based chatbot."
    elif message in ["how are you", "how are you doing", "are you okay"]:
        return "I'm doing great! Thanks for asking."
    elif message in ["what can you do", "what are your capabilities", "help me", "what do you do"]:
        return "I can answer simple questions based on my predefined rules."
    elif message in ["what is the time", "what time is it", "current time"]:
        result_time = get_current_time()
        return f"The current time is {result_time}"
    elif message in ["what is today's date", "what is the date", "today's date", "current date"]:
        result_date = get_current_date()
        return f"Today's date is {result_date}"
    elif "thanks" in message or "thank" in message:
            return "You're welcome!"
    else:
        return "I'm sorry, I don't understand that yet. Try asking about my name, capabilities, date, or time."

response = get_response(message)