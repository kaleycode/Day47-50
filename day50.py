import os, time, random

while True:
  print("⭐️Day 50: Idea Storage⭐️")
  print()
  print("Enter 1 to add an idea or Enter 2 to load a random idea")
  print()
  print("1: Add an idea")
  print("2: Load up a random idea")
  print()
  menu = input("> ")
  if menu == "1":
    f = open("my.ideas", "a+")
    idea = input("Input your idea: ")
    f.write(f"{idea}\n")
    f.close()
    print("Nice! Your idea has been stored.")
    time.sleep(1)
    os.system("clear")
  elif menu == "2":
    f = open("my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    print()
    time.sleep(1)
    os.system("clear")