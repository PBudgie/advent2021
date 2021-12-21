def getInput(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = line.strip().split('|')
      rawLines[i][0] = rawLines[i][0].strip()
      rawLines[i][1] = rawLines[i][1].strip()
    return rawLines

DIGITS_BY_INDEX = [
  {0,1,2,4,5,6}, # 0
  {2,5}, # 1
  {0,2,3,4,6}, # 2
  {0,2,3,5,6}, # 3
  {1,2,3,5}, # 4
  {0,1,3,5,6}, # 5
  {0,1,3,4,5,6}, # 6
  {0,2,5}, # 7
  {0,1,2,3,4,5,6}, # 8
  {0,1,2,3,5,6}, # 9
]

def findSegmentsForDigit(patterns, digit):
  for pattern in patterns:
    if digit == 1 and len(pattern) == 2:
      return set(list(pattern))
    elif digit == 7 and len(pattern) == 3:
      return set(list(pattern))
    elif digit == 4 and len(pattern) == 4:
      return set(list(pattern))

def isValidSegmentMap(patterns, segmentMap):
  for pattern in patterns:
    lightedSegments = set([segmentMap.index(x) for x in set(list(pattern))])
    if lightedSegments not in DIGITS_BY_INDEX:
      return False
  return True

def findSegmentMap(patterns, segment0, segments13, segments25, segments46):
  for segment1 in segments13:
    for segment2 in segments25:
      for segment4 in segments46:
        segment3 = segments13.difference(segment1).pop()
        segment5 = segments25.difference(segment2).pop()
        segment6 = segments46.difference(segment4).pop()
        segmentMap = [segment0, segment1, segment2, segment3, segment4, segment5, segment6]
        if isValidSegmentMap(patterns, segmentMap) == True:
          return segmentMap

def decodeDigit(digit, segmentMap):
  lightedSegments = set([segmentMap.index(x) for x in set(list(digit))])
  return DIGITS_BY_INDEX.index(lightedSegments)

input = getInput('8-input.txt')
total = 0

for display in input:
  tenPatterns = display[0].split(' ')
  fourDigits = display[1].split(' ')
  segmentsForOne = findSegmentsForDigit(tenPatterns, 1)
  segmentsForSeven = findSegmentsForDigit(tenPatterns, 7)
  segmentsForFour = findSegmentsForDigit(tenPatterns, 4)

  # Find possible segments
  segment0 = segmentsForSeven.difference(segmentsForOne).pop()
  segments13 = segmentsForFour.difference(segmentsForOne)
  segments25 = segmentsForOne
  segments46 = {'a','b','c','d','e','f','g'}.difference(segmentsForSeven).difference(segmentsForFour)

  # Find the correct map of segments
  correctSegmentMap = findSegmentMap(tenPatterns, segment0, segments13, segments25, segments46)

  # Decode digits using correct segment map
  firstDigit = decodeDigit(fourDigits[0], correctSegmentMap)*1000
  secondDigit = decodeDigit(fourDigits[1], correctSegmentMap)*100
  thirdDigit = decodeDigit(fourDigits[2], correctSegmentMap)*10
  fourthDigit = decodeDigit(fourDigits[3], correctSegmentMap)
  total += firstDigit + secondDigit + thirdDigit + fourthDigit

print(total)