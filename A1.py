import math

woord = input("Voer woord in: ")

lowerMiddleIndex = math.floor((len(woord)+1)/2)
upperMiddleIndex = math.ceil((len(woord)+3)/2)

print(woord[lowerMiddleIndex:upperMiddleIndex])