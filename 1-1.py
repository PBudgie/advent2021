def getLinesAsInt(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = int(rawLines[i].strip())
    return rawLines

def countIncreases(nums):
  totalIncreases = 0
  for i in range(1, len(nums)):
    if(nums[i] > nums[i-1]):
      totalIncreases += 1
  return totalIncreases

numbers = getLinesAsInt("1-input.txt")
print(str(countIncreases(numbers)))