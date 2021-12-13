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

def markLine(lineCrossings, line):
  xIncrementer = 0
  if line[0][0] < line[1][0]:
    xIncrementer = 1
  elif line[0][0] > line[1][0]:
    xIncrementer = -1

  yIncrementer = 0
  if line[0][1] < line[1][1]:
    yIncrementer = 1
  elif line[0][1] > line[1][1]:
    yIncrementer = -1

  currPoint = line[0]
  while currPoint != line[1]:
    lineCrossings[currPoint[1]][currPoint[0]] += 1
    currPoint = [currPoint[0] + xIncrementer, currPoint[1] + yIncrementer]
  lineCrossings[currPoint[1]][currPoint[0]] += 1

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
  markLine(lineCrossings, line)

numPointsWithOverlap = countPointsWithTwoOverlaps(lineCrossings)
print(numPointsWithOverlap)