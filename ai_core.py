import requests
import os
import json

print("Zeus Booting...")

name = "Zeus"


def load_config(file):
    with open(file, "r") as f:
        return f.read()


zeus_identity = load_config("config/identity.txt")
zeus_personality = load_config("config/personality.txt")


def load_memory():
    try:
        with open("memory/memories.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_memory():
    with open("memory/memories.json", "w") as f:
        json.dump(memory, f, indent=4)


def load_conversation():
    try:
        with open("memory/conversation.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_conversation():
    with open("memory/conversation.json", "w") as f:
        json.dump(conversation, f, indent=4)


conversation = load_conversation()

if not isinstance(conversation, list):
    conversation = []

memory = load_memory()


def format_memory():
    if not memory:
        return "No stored memories."

    lines = []

    for category, entries in memory.items():
        lines.append(f"{category.upper()}:")

        if isinstance(entries, dict):
            for key, value in entries.items():
                lines.append(f"- {value}")
        else:
            lines.append(f"- {entries}")

    return "\n".join(lines)


def remember(category, key, value):
    if category not in memory:
        memory[category] = {}

    memory[category][key] = value
    save_memory()

    return "Memory saved."


def ask_qwen(message):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:7b",
                "prompt": (
                    zeus_identity
                    + "\n\n"
                    + zeus_personality
                    + "\n\nCurrent memories:\n"
                    + format_memory()
                    + "\n\nConversation history:\n"
                    + str(conversation[-10:])
                    + "\n\nUser: "
                    + message
                ),
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except Exception as e:
        return f"Qwen connection error: {e}"


def respond(message):
    if message.lower().startswith("remember:"):
        info = message[9:].strip()

        if not info:
            return "What would you like me to remember?"

        remember("important", str(len(memory["important"]) + 1), info)
        return f"I'll remember that: {info}"

    reply = ask_qwen(message)

    conversation.append({
        "user": message,
        "zeus": reply
    })

    save_conversation()

    return reply


print(f"{name} online.")
print("Type 'quit' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "quit":
        print("AI shutting down.")
        break

    print("Zeus:", respond(user))
