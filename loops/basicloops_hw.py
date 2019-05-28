"""
fizz buzz
"""
for num in range(1,101):
  for i in range(2,num):
    if (num%i) == 0:
      if (num%3 == 0) and (num%5 == 0):
        print("FizzBuzz")
      elif (num%3 == 0):
        print("Fizz")
      elif (num%5 == 0):
        print("Buzz")
      else:
        print(num)
      break
  else:
    print("prime")
    continue
