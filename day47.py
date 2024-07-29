import os, time, random
character = {}
character["Harry"] = {"Intelligence": 20, "Wisdom": 20, "Sense Of Humor": 80, "Baldness Level": 0}
character["Hermione"] = {"Intelligence": 200, "Wisdom": 50, "Sense Of Humor": 50, "Baldness Level": 0}
character["Dumbledore"] = {"Intelligence": 250, "Wisdom": 100, "Sense Of Humor": 50, "Baldness Level": 0}
character["Voldemort"] = {"Intelligence": 250, "Wisdom": 1, "Sense Of Humor": 10, "Baldness Level": 101}
character["Ron"] = {"Intelligence": 15, "Wisdom": 10, "Sense Of Humor": 90, "Baldness Level": 0}



while True:
  print("This VS That\nCharacter Edition!")
  print()
  print("Let's see who will win!")
  print()

  for key in character:
    print(key)
  print()
  user = input("Pick your character\n> ").title()
  comp = random.choice(list(character.keys()))
  print("The computer has picked", comp)
  print("Choose your stat: Intelligence, Wisdom, Sense of Humor, & Baldness Level")
  answer = input("> ").title()
  print(f"{user}: {character[user][answer]}")
  print(f"{comp}: {character[comp][answer]}")
  if character[user][answer] > character[comp][answer]:
    print()
    print(user, "wins!")
  elif character[user][answer] < character[comp][answer]:
    print()
    print(comp, "wins!")
  else:
    print("It's a draw")
  time.sleep(5.5)
  os.system("clear")