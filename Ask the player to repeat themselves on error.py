#https://github.com/webaverse-studios/CharacterCreator/issues/332
#fixes issue 332

import random

# Pre-defined responses and corresponding emotes
responses = [
    ("Huh?", "confused"),
    ("What?", "confused"),
    ("Eh?", "confused"),
    ("...", "silent"),
    ("Can you repeat that?", "neutral"),
    ("I didn't catch that.", "neutral"),
    ("Come again?", "neutral"),
    ("Could you say that again?", "neutral"),
    ("Pardon me?", "polite"),
    ("Excuse me?", "polite"),
    ("I'm not sure I understood.", "uncertain"),
    ("Sorry, I didn't understand.", "apologetic"),
    ("Please, could you rephrase that?", "polite"),
    ("I missed that. Can you say it again?", "neutral"),
    ("What was that?", "curious"),
    ("I didn't get that. Can you repeat?", "neutral"),
    ("One more time, please.", "polite"),
    ("Could you please repeat that?", "polite"),
    ("Sorry, can you say that again?", "apologetic"),
    ("My apologies, I didn't hear you clearly. Can you please repeat?", "apologetic"),
]

def handle_error():
    response, emote = random.choice(responses)
    print(f"{response} ({emote})")

# Get user input
user_input = input("Enter your message: ")

# Check if input is blank
if not user_input.strip():
    handle_error()
