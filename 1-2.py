def getLinesAsInt(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = int(rawLines[i].strip())
    return rawLines

# @param end is NOT inclusive
def getSum(arr, start, end):
  sum = 0
  for i in range(start, end):
    sum += arr[i]
  return sum

def countWindowIncreases(nums):
  totalWindowIncreases = 0
  previousWindowSum = getSum(nums, 0, 2)
  for i in range(3, len(nums)):
    currentWindowSum = getSum(nums, i-3, i)
    if(currentWindowSum > previousWindowSum):
      totalWindowIncreases += 1
    previousWindowSum = currentWindowSum
  return totalWindowIncreases

numbers = getLinesAsInt("1-input.txt")
# numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
print(countWindowIncreases(numbers))