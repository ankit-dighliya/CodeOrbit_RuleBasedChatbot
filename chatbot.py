
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
    else:
        print(f"Bot: You said {message}")
