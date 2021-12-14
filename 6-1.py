def getStartingLanternfish(filename):
  with open(filename) as inputFile:
    charArr = inputFile.readline().split(',')
    return [int(x) for x in charArr]

lanternfish = getStartingLanternfish('6-input.txt')

for i in range(80):
  for fishId in range(len(lanternfish)):
    if lanternfish[fishId] == 0:
      lanternfish[fishId] = 7
      lanternfish.append(8)
    lanternfish[fishId] -= 1
print(len(lanternfish))