#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASK forgiveness than permission
# (é mais facil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()
    # FileNotFoundError
    print(names.append)
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # Todo: usar retry
else:
    print("sucesso!")
finally:
    print("Execute isso sempre!)")
try:
    print(names[2])

except:
    print("[Error] Missing name in the list")
    sys.exit(1)
