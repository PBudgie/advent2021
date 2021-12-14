def getStartingLanternfish(filename):
  with open(filename) as inputFile:
    charArr = inputFile.readline().split(',')
    return [int(x) for x in charArr]

def initializeDictionary(initialLanternfish):
  returnDictionary = {}
  for fishTimer in initialLanternfish:
    if fishTimer not in returnDictionary:
      returnDictionary[fishTimer] = 1
    else:
      returnDictionary[fishTimer] += 1
  return returnDictionary

def countLanternfish(dict):
  totalLanternfish = 0
  for numLanternfish in dict.values():
    totalLanternfish += numLanternfish
  return totalLanternfish

lanternfish = getStartingLanternfish('6-input.txt')
oldTimerDictionary = initializeDictionary(lanternfish)
newTimerDictionary = {}
for day in range(256):
  for key in oldTimerDictionary:
    if key == 0:
      newTimerDictionary[8] = oldTimerDictionary[0]
      if 6 in newTimerDictionary:
        newTimerDictionary[6] += oldTimerDictionary[0]
      else:
        newTimerDictionary[6] = oldTimerDictionary[0]
    else:
      if key == 7 and 6 in newTimerDictionary:
        newTimerDictionary[6] += oldTimerDictionary[key]
      else: 
        newTimerDictionary[key - 1] = oldTimerDictionary[key]
  # print(day, ' ', countLanternfish(newTimerDictionary), ' ', newTimerDictionary)
  oldTimerDictionary = newTimerDictionary
  newTimerDictionary = {}

print(countLanternfish(oldTimerDictionary))