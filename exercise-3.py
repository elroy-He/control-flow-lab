# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:

dogAge = input('Input a dog''s age in human years: ')

# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each

def convertAge(val):
  if (val <= 2):
    return val * 10
  else:
    return (val-2) * 10

# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
while (not dogAge.isnumeric()):
  dogAge = input('Input a dog''s age in human years: ')

age = convertAge(int(dogAge))
print(f"The dog's age in dog years is {age}")
# Hint:  Use the int() function to convert the string returned from input() into an integer