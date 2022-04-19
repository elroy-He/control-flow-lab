# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

mon = input('Enter the month of the year (Jan - Dec): ')
while (len(mon) != 3):
  mon = input('Enter the month of the year (Jan - Dec): ')

day = input('Enter the day of the month: ')
while (not (0 < int(day) and int(day) <= 31)):
  day = input('Enter the day of the month: ')

winter = ['jan', 'feb']
spring = ['april', 'may']
summer = ['july', 'aug']
fall = ['oct', 'nov']


def determineSeason(val1, val2):
  val1 = val1.lower()
  val2 = int(val2)

  if (winter.count(val1) == 1 or (val1 == 'dec' and val2 >= 21) or (val1 == 'mar' and day <= 19)) :
    print(f"{val1} {val2} is in winter")
  elif (spring.count(val1) == 1 or (val1 == 'mar' and val2 >= 20) or (val1 == 'jun' and day <= 20)):
    print(f"{val1} {val2} is in spring")
  elif(summer.count(val1) == 1 or (val1 == 'jubn' and val2 >= 21) or (val1 == 'sep' and day <= 21)):
    print(f"{val1} {val2} is in summer")
  else:
    print(f"{val1} {val2} is in fall")

determineSeason(mon, day)

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.