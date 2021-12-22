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

heightMap = getMap('9-input.txt')
totalRisk = 0
for i in range(len(heightMap)):
  for j in range(len(heightMap[i])):
    if(isLowPoint(heightMap, (i,j))):
      totalRisk += (heightMap[i][j] + 1)
print(totalRisk)