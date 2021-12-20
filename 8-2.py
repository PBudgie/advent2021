def getInput(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = line.strip().split('|')
      rawLines[i][0] = rawLines[i][0].strip()
      rawLines[i][1] = rawLines[i][1].strip()
    return rawLines

def findSegmentsForDigit(patterns, digit):
  for pattern in patterns:
    if digit == 1 and len(pattern) == 2:
      return pattern
    elif digit == 7 and len(pattern) == 3:
      return pattern
    elif digit == 4 and len(pattern) == 4:
      return pattern

input = getInput('8-test.txt')
for display in input:
  tenPatterns = display[0].split(' ')
  fourDigits = display[1].split(' ')
  segmentsForOne = set(findSegmentsForDigit(tenPatterns, 1).split())
  segmentsForSeven = set(findSegmentsForDigit(tenPatterns, 7))
  segmentsForFour = set(findSegmentsForDigit(tenPatterns, 4))

  print(segmentsForSeven)
  topSegment = segmentsForSeven.difference(segmentsForOne) #This set difference doesn't work