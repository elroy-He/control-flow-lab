# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):


alphabet = input('Please enter a letter from the alphabet (a-z or A-Z) ')
print(f"your input letter is {alphabet}")

while (not alphabet.isalpha()):
  alphabet = input('Please reenter a letter from the alphabet (a-z or A-Z) ')
# 2. Write the code that determines whether the letter entered is a vowel
vowels = ['a', 'e', 'i', 'o', 'u']
def isVowel(val):
  if (vowels.count(val.lower()) == 1):
    return True
  else:
    return False

vowelResult = isVowel(alphabet)

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

if (vowelResult == True):
  print(f" The letter {alphabet} is a vowel")
else:
  print(f" The letter {alphabet} is a constant" )
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':