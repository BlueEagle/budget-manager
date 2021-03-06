import os
import platform

income = 120.00
budget = {"tithing": 10, "savings": 50, "personal":10}

def clear():
  if(platform.system() == 'Linux' or platform.system() == "Darwin"): os.system('clear')
  if(platform.system() == 'WIndows'): os.system('cls')

def getDollarValue(value): # returns string dollar value
  value = str(int(value * 100))
  dollars = value[:-2]
  cents = value[-2:]
  # print(f"Dollar amount: {dollars}")
  # print(f"Cents: {cents}")
  value = f"${dollars}.{cents}"
  return value

def getPercentAvailability():
  availability = 100
  for budgetItem in budget:
    availability -= budget[budgetItem]
  return availability

def percentOf(percent, value):
  value = float(percent) * float(value) / float(100)
  return value

def getAvailability():
  return percentOf(getPercentAvailability(), income)

def addBudgetItem():
  clear()
  itemName = input('Enter the name of the budget item to add (or quit): ')
  clear()
  print(f'You are creating a budget item for: {itemName}\n\n')
  print(f'Please select one of the following options:\n')
  print("p - enter budget percent")
  print("d - enter budget dollar amount")
  print("q - quit")
  userSelection = input("\nPlease select an option: ")
  if (isAny(userSelection.lower(), 1, 'p', 'percent')):
    print('do percent stuff...')
  elif (isAny(userSelection.lower(), 2, 'd', 'dollar', 'dollars')):
    print('do dollars stuff')
  else:
    print('I don\'t know what you want!')


def displayOverview():
  print(f"Starting with a total of {getDollarValue(income)}.")
  for budgetItem in budget:
    print(f"You will pay {budget[budgetItem]}% toward {budgetItem} which is {getDollarValue(percentOf(budget[budgetItem], income))}.")
  print(f"Invested: {getDollarValue(income-getAvailability())} / {getDollarValue(income)} ({100-getPercentAvailability()}%)")
  print(f"Available: {getDollarValue(getAvailability())} ({getPercentAvailability()}%)")

# displayOverview()
# print(getDollarValue(getAvailability()))

def isAny(value, *matchingValues): # True if value matches any of the others
  for matchingValue in matchingValues:
    if(value == matchingValue): return True
  return False

def menu():
  def displayMenuOptions():
    clear()
    displayOverview()
    print("\n\nMenu (use numbers or keywords):")
    print("a - add a budget item.")
    print("r - remove a budget item.")
    print("m - modify a budget item.")
    print("q - quit.")
  
  while(True):
    displayMenuOptions()
    userSelection = input('\nPlease select an option: ')
    # print(f"User selected: {userSelection}")

    if (isAny(userSelection.lower(), '1', 'add', 'a')):
      addBudgetItem()
    elif (isAny(userSelection.lower(), '2', 'remove', 'r')):
      print('removing budget item!')
    elif (isAny(userSelection.lower(), '3', 'modify', 'm')):
      print('modifying budget item!')
    elif (isAny(userSelection.lower(), '4', 'q', 'quit')):
      print('quitting...')
      break
    else:
      print(f'Invalid input: {userSelection}')

    input("\nPress ENTER to continue...")
    
menu()