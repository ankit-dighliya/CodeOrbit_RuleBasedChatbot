import datetime

name = input("Bot: What is your name? ")

print("You:", name)
print(f"Bot: You said {name}")


print("Bot: I am ready to chat!")

message = ""

while message != "bye":

    message = input("You: ").strip().lower()
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
    else:
        print(f"Bot: You said {message}")


'''
import datetime

x = datetime.datetime.now()
current_date = x.date()
current_time = x.time()
print(f"The current date is {current_date}")
print(f"The current time is {current_time}")
'''