import copy

def getLinesAsBitArray(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = list(rawLines[i].strip())
      rawLines[i] = list(map(int, rawLines[i]))
    return rawLines

def getMostCommonBit(listOfNumbers, bitIndex):
  totalLength = len(listOfNumbers)
  numOnes = [listOfNumbers[x][bitIndex] for x in range(totalLength)].count(1)
  numZeroes = totalLength - numOnes

  if numOnes > numZeroes:
    return 1
  elif numOnes < numZeroes:
    return 0
  else:
    return -1

def getOppositeBit(bit):
  if bit == 1:
    return 0
  elif bit == 0:
    return 1
  else:
    return -1

def hasBitInIndex(number, bit, index):
  if number[index] == bit:
    return True
  else:
    return False

def getOxygenGeneratorRating(listOfNumbers):
  currentList = copy.deepcopy(listOfNumbers)
  bitPointer = 0
  while len(currentList) > 1:
    mostCommonBit = getMostCommonBit(currentList, bitPointer)
    if mostCommonBit == -1:
      mostCommonBit = 1
    currentList = list(filter(lambda num: hasBitInIndex(num, mostCommonBit, bitPointer), currentList))
    bitPointer += 1
  
  binaryOxygenGeneratorRating = ''.join([str(x) for x in currentList[0]])
  return int(binaryOxygenGeneratorRating, 2)

def getCarbonScrubberRating(listOfNumbers):
  currentList = copy.deepcopy(listOfNumbers)
  bitPointer = 0
  while len(currentList) > 1:
    leastCommonBit = getOppositeBit(getMostCommonBit(currentList, bitPointer))
    if leastCommonBit == -1:
      leastCommonBit = 0
    currentList = list(filter(lambda num: hasBitInIndex(num, leastCommonBit, bitPointer), currentList))
    bitPointer += 1

  binaryCarbonScrubberRating = ''.join([str(x) for x in currentList[0]])
  return int(binaryCarbonScrubberRating, 2)

  

report = getLinesAsBitArray('3-input.txt')
print(getOxygenGeneratorRating(report) * getCarbonScrubberRating(report))