#!/usr/bin/env python3

for i in range(99, 0, -1):
    if(i == 2):
        print("{} bottles of beer on the wall, {} bottles of beer, take one down, pass it around, {} bottle of beer on the wall".format(i, i, i-1))
    elif(i == 1):
        print("{} bottle of beer on the wall, {} bottle of beer, take one down, pass it around, no bottles of beer on the wall".format(i, i))
    else:
        print("{} bottles of beer on the wall, {} bottles of beer, take one down, pass it around, {} bottles of beer on the wall".format(i, i, i-1))

