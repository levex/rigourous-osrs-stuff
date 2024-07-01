#!/usr/bin/python3
import requests
import sys

PLAYER = sys.argv[1]
print(PLAYER, end="")
print(",", end="")

rep = requests.get("https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=%s" % PLAYER)
s = rep.text.split("\n")
print(s[-15].split(",")[1], end="")
print(",", end="")
print(s[-14].split(",")[1], end="")
print(",", end="")
print(s[-12].split(",")[1], end="")
print(",", end="")
print(s[-11].split(",")[1], end="")
print(",", end="")
print(s[-53].split(",")[1], end="")
print(",", end="")
print(s[-54].split(",")[1])
