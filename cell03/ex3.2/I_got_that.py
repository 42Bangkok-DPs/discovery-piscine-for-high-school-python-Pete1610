#!/usr/bin/env python3
print("What you gotta say? : Hello")

while True:
    user_input = input("I got that! Anything else? : ")
    if user_input.strip().upper() == "STOP":
        break
