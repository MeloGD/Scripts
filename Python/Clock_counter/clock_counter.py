#!/usr/bin/env python3
# I had to write a file with the hours and minuts in a HH:MM format, so I 
# decided that it was quicker to develop this script than writing them down 
# myself, one by one.

first_half = ""
second_half = ""
filename = "output.txt"
minuts = 0

file = open(filename, "w")

for hours in range(24):
  if hours < 10 and hours == 0:
    first_half = str(hours) + "0" 
  elif hours < 10:
    first_half = "0" + str(hours)
  else:
    first_half = str(hours)
  for times in range(4):
    if minuts == 0: 
      second_half = str(minuts) + "0"
      file.write(first_half + ":" + second_half + "\n")
    if minuts == 15:
      second_half = str(minuts)
      file.write(first_half + ":" + second_half + "\n")
    if minuts == 30:
      second_half = str(minuts)
      file.write(first_half + ":" + second_half + "\n")
    if minuts == 45:
      second_half = str(minuts)
      file.write(first_half + ":" + second_half + "\n")
    minuts += 15
  minuts = 0  
  
file.close()
  




