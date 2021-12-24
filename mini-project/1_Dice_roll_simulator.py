import random

while True:
    print ("\n1.Roll the dice    2.Exit")
    user = int(input("What do you want to do\n"))
    if user == 1:
        num = random.randint(1,6)
        print(num)
    else:
        break