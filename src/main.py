#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author: Mathisdlg



import os
import hashlib as hl
import passwordGen as pg

if os.name == "nt":
    OS = "Windows"
else:
    OS = "Linux"

OPT = {
    "length": 20,
    "numbers": True,
    "special": True,
    "new": None,
}


def clear():
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    clear()
    print("Password Generator")
    print("By: Mathisdlg")
    print("Github: mathisdlg\n")
    
    print("Authorized characters:")
    print(pg.passwordGenerator(OPT))
