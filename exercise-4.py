# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:


a = input('Enter the lengths of three side of a triangle: \na: ')
b = input('b: ')
c = input('c: ')

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

while (not a.isnumeric() or not b.isnumeric() or not c.isnumeric()):
  a = input('Enter the lengths of three side of a triangle: \na: ')
  b = input('b: ')
  c = input('c: ')


def determineTriangle(val1, val2, val3):

  lst = [val1, val2, val3]
  dct = {}
  for val in lst:
    if (not val in dct):
      dct[val] = 1

  val1 = int(val1)
  val2 = int(val2)
  val3 = int(val3)


  if (val1 == val2 and val1 == val3):
    print(f"A triangle with sides of {val1}, {val2} & {val3} is a equalateral triangle")
  elif (val1 != val2 and val1 != val3):
    print(f"A triangle with sides of {val1}, {val2} & {val3} is a scalene triangle")
  elif (len(dct) == 2):
    print(f"A triangle with sides of {val1}, {val2} & {val3} is a isosceles triangle")

determineTriangle(a,b,c)

# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
