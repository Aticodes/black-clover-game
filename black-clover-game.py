import sys
import random

characters = {
    1: {"name": "Asta", "magic": "Anti Magic"},
    2: {"name": "Noelle", "magic": "Water Magic"},
    3: {"name": "Charmi", "magic": "Sheep Magic"},
    4: {"name": "Yuno", "magic": "Wind Magic"}
}

print("\nPlease select your character:")
print("1. Asta (Anti Magic, Commoner)")
print("2. Noelle (Water Magic, Royal)")
print("3. Charmi (Sheep Magic, Foodie)")
print("4. Yuno (Wind Magic, Commoner)")

try:
    user_choice = int(input("Enter your choice (1-4): "))
    if user_choice < 1 or user_choice > 4:
        sys.exit("Invalid choice! Please run the game again and choose a number between 1 and 4.")
except ValueError:
    sys.exit("Invalid input! Please enter a number.")

computer_choice = random.randint(1, 4)

if user_choice == computer_choice:
    print("\nSorry, both selected the same character. Asta says, 'I won’t fight myself!' 😅")
    sys.exit()

user_char = characters[user_choice]["name"]
user_magic = characters[user_choice]["magic"]
comp_char = characters[computer_choice]["name"]
comp_magic = characters[computer_choice]["magic"]

print(f"\nYou chose {user_char} ({user_magic})")
print(f"Computer chose {comp_char} ({comp_magic})")

print(f"\n🔥 Battle: {user_char} vs {comp_char} 🔥")

battle_outcomes = {
    (1, 2): "Asta wins! His anti-magic slashes through Noelle’s water dragon.",
    (3, 1): "Charmi wins! Her food-fueled sheep army overwhelmed Asta.",
    (1, 4): "It’s a tie! Asta vs Yuno — their rivalry is too intense to declare a winner.",
    (2, 3): "Charmi wins! Noelle couldn’t handle the sheer cuteness and food power.",
    (4, 2): "Yuno wins! His wind magic outmaneuvers Noelle's attacks.",
    (3, 4): "Yuno wins! Charmi was too distracted by food and blushed at Prince Yuno. 🍜💖"
}

outcome = battle_outcomes.get((user_choice, computer_choice)) or \
          battle_outcomes.get((computer_choice, user_choice))

if outcome:
    print(outcome)
else:
    print("Hmm... this battle combination doesn't have a defined outcome yet. 🤔 Stay tuned!")