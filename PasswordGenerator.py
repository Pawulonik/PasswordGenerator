#!/usr/bin/env python3

import random
import string



def generator(complexity,length):

    if (complexity == 1):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(length))
    if (complexity == 2):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(length))
    if (complexity == 3):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))
    if (complexity == 4):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(length))
    else:
        print("Wrong input!")

def options():
    try:
        complexity = int(input("Password complexity: "))
        length = int(input("Password length: "))
        count = int(input("Password count: "))
    except ValueError:
        print("Wrong input!")
        exit()

    passwdList = [None] * (count)

    for i in range (count):

        passwdList[i] = generator(complexity,length)
        print(passwdList[i] + "\n")



    savePasswords(passwdList)

def savePasswords(List):

    flag = str(input("Do you want to save passwords to a file? [y] - Yes [n] - No : "))

    if(flag is 'y'):
        file = open('passwd.txt','w')

        for i in range (len(List)):
            file.write(List[i])
            file.write("\n")
        print("Passwords saved to 'passwd.txt'.")

    else:
        return


def main():

    print("\n")
    print("     _____                                    _  _____                           _               ")
    print("    |  __ \                                  | |/ ____|                         | |              ")
    print("    | |__) |_ _ ___ _____      _____  _ __ __| | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __   ")
    print("    |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|  ")
    print("    | |  | (_| \__ \__ \ \ V  V/ (_) | | | (_| | |__| |  __/ | | |  __/ | | (_| | || (_) | |     ")
    print("    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|     ")
    print("     by redfr0g")
    print("\n")
    print("Password complexity: ")
    print("[1] - Lowercase")
    print("[2] - Lowercase + Uppercase")
    print("[3] - Lowercase + Uppercase + Digits")
    print("[4] - Lowercase + Uppercase + Digits + Special Characters")
    print("\n")



    options()

main()

