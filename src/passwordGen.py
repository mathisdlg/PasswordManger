#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author: Mathisdlg



import random as rnd


def getAuthorize(opt: dict):
    authorized = []

    for char in range(97, 123):
        authorized.append(chr(char))
        authorized.append(chr(char).upper())

    if opt["numbers"]:
        authorized += [ str(i) for i in range(0, 10)]
    if opt["special"]:
        authorized += [ char for char in "!#$%&+-./:;<=>?@[]_{|}~"]
        
    if opt["new"] != None:
        for cahr in opt["new"]:
            if char not in authorized:
                authorized.append(char)

    return authorized


def passwordGenerator(authorized: list):
    password = ""

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
    authorized = getAuthorize(opt)

    for i in range(100000):
        listPassword.append(passwordGenerator(authorized))

    print("Password generated")
    print(listPassword)