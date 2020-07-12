income = 120.00
budget = {"tithing": 10, "savings": 50, "personal":10}

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

print(getPercentAvailability())