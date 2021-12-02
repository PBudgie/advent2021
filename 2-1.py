def getInstructions(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = rawLines[i].strip().split()
      rawLines[i][1] = int(rawLines[i][1])
    return rawLines

"""
instructions = [['forward', 5],
  ['down', 5],
  ['forward', 8],
  ['up', 3],
  ['down', 8],
  ['forward', 2]]
"""

instructions = getInstructions('2-input.txt')

horizontal = 0
depth = 0

for ins in instructions:
  if(ins[0] == "up"):
    depth -= ins[1]
  elif(ins[0] == "down"):
    depth += ins[1]
  elif(ins[0] == "forward"):
    horizontal += ins[1]

print(str(horizontal * depth))