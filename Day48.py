import os, time

while True:
  print("⭐️ HIGH SCORE TABLE ⭐️")
  print()
  name = input("Enter your initials > ").upper()
  score = input("Enter your score > ")
  print()
  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()
  print("Added to high score table.")
  time.sleep(1)
  os.system("clear")