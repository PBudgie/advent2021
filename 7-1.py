def getCrabPositions(filename):
  with open(filename) as inputFile:
    crabPositions = inputFile.readline().split(',')
    return [int(crab) for crab in crabPositions]

def getFuelToAlignTo(crabPositions, positionToAlignTo):
  totalFuel = 0
  for crabPosition in crabPositions:
    totalFuel += abs(crabPosition - positionToAlignTo)
  return totalFuel

crabPositions = getCrabPositions('7-input.txt')
minPosition = min(crabPositions)
maxPosition = max(crabPositions)

minFuel = getFuelToAlignTo(crabPositions, minPosition)
for position in range(minPosition, maxPosition):
  fuelForThisPosition = getFuelToAlignTo(crabPositions, position)
  if fuelForThisPosition < minFuel:
    minFuel = fuelForThisPosition
print(minFuel)