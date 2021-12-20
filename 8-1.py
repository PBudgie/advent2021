def getFourDigits(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = line.split('|')[1].strip().split(' ')
    return rawLines

def isUniqueDigit(digit):
  if len(digit) in [2, 3, 4, 7]:
    return True
  return False

digits = getFourDigits('8-input.txt')
flattened = [x for sublist in digits for x in sublist]

totalUniqueDigits = 0
for digit in flattened:
  if isUniqueDigit(digit):
    totalUniqueDigits += 1
print(totalUniqueDigits)