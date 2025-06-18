negative_reponses = ["Not really good", "Meh", 'Could be better', "I'm hanging in there", "Not great"]
positive_respones = ["Good", "Not bad", "I'm doing great", "Today's being a good day."]

question = input("How's your day being going so far? ")

if question in negative_reponses:
    print("Oh well I hope the rest of your day goes better!")

elif question in positive_respones:
    print("Oh I'm glad to hear that!")