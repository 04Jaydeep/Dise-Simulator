import random as rd

again=True

while again:
    print(rd.randint(1, 6))
    Another_roll=input("Want To Roll The Dise Again? (Y/N): ")
    if Another_roll == "y" or "Y":
        continue
    else:
        break