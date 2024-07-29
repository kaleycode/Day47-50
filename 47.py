import os, time, random

car = {}
car["Tesla"] = {"Speed": 100, "Safety": 70, "Cool Factor": 60, "Driver Behavior": 40}
car["Volvo"] = {"Speed": 55, "Safety": 90, "Cool Factor": 60, "Driver Behavior": 90}
car["Truck"] = {"Speed": 80, "Safety": 40, "Cool Factor": 40, "Driver Behavior": 2}

while True: 
    print("This Vs That\nCar Edition")
    print()
    print()
    for key in car:
        print(key)
    print()
    rand = random.choice(list(car.keys()))
    print("The computer has chosen", rand)
    print()
    userPick = input("Pick your car\n").title()
    print()
    print("Choose car stat: Speed, Safety, Cool Factor, or Driver Behavior")
    answer = input("> ").title()
    print(f"{userPick}: {car[userPick][answer]}")
    print(f"{rand}: {car[rand][answer]}")
    if car[userPick][answer] > car[rand][answer]:
        print()
        print("The",userPick, "wins!")
    elif car[userPick][answer] < car[rand][answer]:
        print()
        print("The",rand, "wins!")
    else:
        print("It's a draw")
    time.sleep(5.5)
    os.system("clear")