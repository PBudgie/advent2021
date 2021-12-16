def getCrabPositions(filename):
  with open(filename) as inputFile:
    crabPositions = inputFile.readline().split(',')
    return [int(crab) for crab in crabPositions]

def getFuelToAlignTo(crabPositions, positionToAlignTo):
  # Update this method
  totalFuel = 0
  for crabPosition in crabPositions:
    distToMove = abs(crabPosition - positionToAlignTo)
    fuelToMove = distToMove * (distToMove + 1) / 2
    totalFuel += fuelToMove
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