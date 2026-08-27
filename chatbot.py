import datetime

name = input("Bot: What is your name? ")

print("You:", name)
print(f"Bot: You said {name}")


print("Bot: I am ready to chat!")

message = ""

while message != "bye":

    message = input("You: ").strip().lower()
    x = datetime.datetime.now()
    current_date = x.date()
    current_time = x.time()
    if message == "bye":
        print("Goodbye! Have a great day!")
    elif message in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
    elif message in ["what is your name", "what's your name", "who are you", "your name"]:
        print("Bot: My name is SimpleBot. I'm a rule-based chatbot.")
    elif message in ["how are you", "how are you doing", "are you okay"]:
        print("Bot: I'm doing great! Thanks for asking.")
    elif message in ["what can you do", "what are your capabilities", "help me", "what do you do"]:
        print("Bot: I can answer simple questions based on my predefined rules.")
    elif message in ["what is the time", "what time is it", "current time"]:
        print(f"Bot: The current time is {current_time}")
    elif message in ["what is today's date", "what is the date", "today's date", "current date"]:
        print(f"Bot: Today's date is {current_date}")
    elif ("thanks" or "thank") in message:
        print("You're welcome!")
    else:
        print(f"Bot: You said {message}")
