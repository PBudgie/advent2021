def getLinesAsCharArray(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = list(rawLines[i].strip())
    return rawLines

report = getLinesAsCharArray('3-input.txt')
totalLength = len(report)
lengthOfBinaryNumbers = len(report[0])
mostCommonBits = ''
leastCommonBits = ''
for i in range(lengthOfBinaryNumbers):
  numOnes = [report[x][i] for x in range(totalLength)].count('1')
  numZeroes = totalLength - numOnes

  if numOnes > numZeroes:
    mostCommonBits += '1'
    leastCommonBits += '0'
  else:
    mostCommonBits += '0'
    leastCommonBits += '1'
  
gamma = int(mostCommonBits, 2)
epsilon = int(leastCommonBits, 2)
print(gamma * epsilon)