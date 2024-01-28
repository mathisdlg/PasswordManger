#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author: Mathisdlg



import random as rnd


def getAuthorize(opt: dict): # TODO: Optimize the creation of the list
    authorized = []

    for char in range(97, 123):
        authorized.append(chr(char))
        authorized.append(chr(char).upper())

    if opt["numbers"]:
        for i in range(0, 10):
            authorized.append(str(i))
    if opt["special"]:
        for char in "!#$%&+-./:;<=>?@[\\]_{|}~":
            authorized.append(str(char))
        
    if opt["new"] != None:
        for cahr in opt["new"]:
            if char not in authorized:
                authorized.append(char)

    return authorized


def passwordGenerator(opt: dict):
    password = ""
    authorized = getAuthorize(opt)

    for i in range(opt["length"]):
        password += rnd.choice(rnd.choice(authorized))

    return password



if __name__ == "__main__":
    opt = {
        "length": 20,
        "numbers": True,
        "special": True,
        "new": None,
    }
    listPassword = []
    for i in range(1000000):
        listPassword.append(passwordGenerator(opt))
    
    print("Password generated")
    print(listPassword)