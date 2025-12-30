import random

# Possible personalities of the rock
personalities = [
    "Chill 😌",
    "Grumpy 😠",
    "Wise 🧠",
    "Lazy 😴",
    "Energetic ⚡",
    "Mysterious 🌀"
]

class PetRock:
    def __init__(self, name):
        self.name = name
        self.personality = random.choice(personalities)

    def react_to_mood(self, user_mood):
        # Small chance personality changes randomly
        if random.random() < 0.3:
            self.personality = random.choice(personalities)

        reactions = {
            "happy": "The rock seems brighter today.",
            "sad": "The rock stays silent, supporting you.",
            "angry": "The rock absorbs your anger calmly.",
            "tired": "The rock encourages you to rest.",
            "excited": "The rock vibrates slightly with excitement."
        }

        reaction = reactions.get(user_mood.lower(), "The rock stares into the void.")
        return reaction

    def status(self):
        print(f"\n🪨 {self.name}'s current personality: {self.personality}")

# --- Main Program ---
print("Welcome to Virtual Pet Rock Simulator 🪨")

rock_name = input("Name your pet rock: ")
rock = PetRock(rock_name)

while True:
    rock.status()
    mood = input("\nHow are you feeling? (happy/sad/angry/tired/excited or 'quit'): ")

    if mood.lower() == "quit":
        print(f"\n{rock.name} will remain here forever. Goodbye 👋")
        break

    response = rock.react_to_mood(mood)
    print(f"\n{rock.name} reacts: {response}")
