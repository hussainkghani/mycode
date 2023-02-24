#!/usr/bin/env python3

count = 0
with open("dracula.txt", "r") as foo:
    for line in foo:
        if "vampire" in line.upper():
            count += 1
print(count)

