"""
Checking if condition

"""

def compare_equals(var1, var2, var3):
  if(int(var1) == int(var2)) or (int(var2) == int(var3)) or  (int(var3) == int(var1)):
    return True
  else:
    return False


print(compare_equals(1, 2, 3))