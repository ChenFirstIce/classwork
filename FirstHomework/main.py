import sys

def Tea():
    print("TeaTeaTea,yummy!")

def Coffee():
    print("Oh, poor guy! You must be reduced to do all the teamworke only by yourself")

def main():
    drink = input("What do you want to drink, tea or coffee?")

    if(drink == "tea"):
        Tea()
    elif(drink == "coffee"):
        Coffee();

if __name__ == "__main__":
    main()                 