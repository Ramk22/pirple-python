"""
List operations in python3
"""

myUniqueList = ["ram", 27, "male", 1992, 185, 75]
myLeftovers = []


def addToList(data):
  if data not in myUniqueList:
    myUniqueList.append(data)
    return True

  else:
    myLeftovers.append(data)
    return False


print(addToList("rk"))
print(addToList("rk"))
print(addToList("ram"))
print(addToList("bng"))

print(myUniqueList)
print(myLeftovers)