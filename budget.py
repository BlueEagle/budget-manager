income = 120.00


def getDollarValue(value): # returns string dollar value
  value = str(int(value * 100))
  dollars = value[:-2]
  cents = value[-2:]
  # print(f"Dollar amount: {dollars}")
  # print(f"Cents: {cents}")
  value = f"${dollars}.{cents}"
  return value

print(f'{getDollarValue(income)}')