# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.

def fibo(n):
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

for n in range(50):
  val = fibo(n)
  print(f"term: {n} / number: {val}")
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
