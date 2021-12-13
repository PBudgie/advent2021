def getLines(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = rawLines[i].strip().split(' -> ')
      rawLines[i][0] = rawLines[i][0].split(',')
      rawLines[i][0] = [int(x) for x in rawLines[i][0]]
      rawLines[i][1] = rawLines[i][1].split(',')
      rawLines[i][1] = [int(x) for x in rawLines[i][1]]
    return rawLines

def getMaxDimensions(lines):
  maxX = 0
  maxY = 0
  for line in lines:
    for point in line:
      if point[0] > maxX:
        maxX = point[0]
      if point[1] > maxY:
        maxY = point[1]
  return (maxX + 1, maxY + 1)

def isValidLine(line):
  if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
    return True
  else:
    return False

def markLine(lineCrossings, line):
  minX = min(line[0][0], line[1][0])
  maxX = max(line[0][0], line[1][0])
  minY = min(line[0][1], line[1][1])
  maxY = max(line[0][1], line[1][1])
  for x in range(minX, maxX + 1):
      for y in range(minY, maxY + 1):
        lineCrossings[y][x] += 1

def countPointsWithTwoOverlaps(lineCrossings):
  total = 0
  for row in lineCrossings:
    for point in row:
      if point >= 2:
        total += 1
  return total

lines = getLines('5-input.txt')
maxX, maxY = getMaxDimensions(lines)
lineCrossings = [[0 for x in range(maxX)] for y in range(maxY)]

for line in lines:
  if isValidLine(line):
    markLine(lineCrossings, line)

numPointsWithOverlap = countPointsWithTwoOverlaps(lineCrossings)
print(numPointsWithOverlap)