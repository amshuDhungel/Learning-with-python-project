import string
import random


if __name__ == "__main__":
    s1=string.ascii_letters
    #print(s1)
    s2=string.ascii_lowercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)
passlen= int(input("enter the length of password: "))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("Your password is: ")
print("".join(s[0:passlen]))
    


