# PHASE 1
# Greetings

# import random so the bot can have random responses
import random as random
# create responses
human_greetings = ["Hi", "Hello", "Hi there", "Hi!", "Hello!", "Hola", "Hola!", 
                    "Greetings", "Greetings!", "Hey!", "Hey", "Hey there", "Hey There!"]
bot_greetings = ["Hola amigo!", "Hello!", "Hi!", "Hey!", "What's up!", 
            "Hi there!", "Hi There", "Hi There!",]
# create loop for:
print("Welcome to Chatbot_Simulator")

while True:
    chatting = input("\nYou: ")
    if chatting in human_greetings:
        chosen_bot_response = random.choice(bot_greetings)
        print("\nBot: " + chosen_bot_response)
    # It should still respond if the user makes a typo
    elif chatting not in human_greetings:
        chosen_bot_response = random.choice(bot_greetings)
        print("\nBot: " + chosen_bot_response)
# PHASE 1 COMPLETED

# PHASE 2
# Basic Conversation
# create human and bot conversation starters and responses






        