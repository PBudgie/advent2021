import copy

def getMap(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = list(line.strip())
      rawLines[i] = [int(x) for x in rawLines[i]]
    return rawLines

def isLowPoint(heightMap, coord):
  maxI = len(heightMap) - 1
  maxJ = len(heightMap[0]) - 1
  i,j = coord
  
  if i-1 >= 0 and heightMap[i][j] >= heightMap[i-1][j]: # Check up
    return False
  if i+1 <= maxI and heightMap[i][j] >= heightMap[i+1][j]: # Check down
    return False
  if j-1 >= 0 and heightMap[i][j] >= heightMap[i][j-1]: # Check left
    return False
  if j+1 <= maxJ and heightMap[i][j] >= heightMap[i][j+1]: # Check right
    return False
  return True

def findBasinSize(heightMap, lowPoint):
  maxI = len(heightMap) - 1
  maxJ = len(heightMap[0]) - 1
  i,j = lowPoint

  pointsInBasin = set()
  oldEdge = set([(i,j)])
  newEdge = set([(i, j)])

  while len(newEdge) > 0:
    newEdge = set()
    for edgePoint in oldEdge:
      pointsInBasin.add(edgePoint)
      currI = edgePoint[0]
      currJ = edgePoint[1]
      if currI-1 >= 0 and heightMap[currI-1][currJ] != 9 and (currI-1, currJ) not in pointsInBasin: # Check up
        newEdge.add((currI-1, currJ))
      if currI+1 <= maxI and heightMap[currI+1][currJ] != 9 and (currI+1, currJ) not in pointsInBasin: # Check down
        newEdge.add((currI+1, currJ))
      if currJ-1 >= 0 and heightMap[currI][currJ-1] != 9 and (currI, currJ-1) not in pointsInBasin: # Check left
        newEdge.add((currI, currJ-1))
      if currJ+1 <= maxJ and heightMap[currI][currJ+1] != 9 and (currI, currJ+1) not in pointsInBasin: # Check right
        newEdge.add((currI, currJ+1))
    oldEdge = newEdge
  return len(pointsInBasin)

# Find all low points, since they belong to the basins
heightMap = getMap('9-input.txt')
lowPoints = []
for i in range(len(heightMap)):
  for j in range(len(heightMap[i])):
    if(isLowPoint(heightMap, (i,j))):
      lowPoints.append((i,j))

# Find their corresponding basin sizes
allBasinSizes = []
for lowPoint in lowPoints:
  allBasinSizes.append(findBasinSize(heightMap, lowPoint))

# Sort and find the largest 3 basin sizes
allBasinSizes.sort()
print(allBasinSizes[-1] * allBasinSizes[-2] * allBasinSizes[-3])