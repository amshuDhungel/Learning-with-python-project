import random
num = random.randint(1,10)
for i in  range(3):
    user =  int(input("Guess the number: "))
    if user == num:
        print("Yes you guess the right number")
        print(f"you guess the right number it's {num}")
        break
    if user != num:
        print(f"you guess the incorrect number it's {num}")
