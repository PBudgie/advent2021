def getLines(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = line.strip()
    return rawLines

def getClosingBracket(openBracket):
  if openBracket == '(':
    return ')'
  elif openBracket == '[':
    return ']'
  elif openBracket == '{':
    return '}'
  elif openBracket == '<':
    return '>'

def getPointsForString(string):
  totalScore = 0
  for i in range(len(string)):
    if string[i] == ')':
      totalScore = 5*totalScore + 1
    elif string[i] == ']':
      totalScore = 5*totalScore + 2
    elif string[i] == '}':
      totalScore = 5*totalScore + 3
    elif string[i] == '>':
      totalScore = 5*totalScore + 4
  return totalScore

# Returns points if expression is incomplete
# and 0 if expression is complete or corrupted
def getCompletionPoints(expression):
  operatorStack = []
  for i in range(len(expression)):
    currChar = expression[i]
    if currChar in ['(', '[', '{', '<']:
      operatorStack.append(expression[i])
    elif currChar != getClosingBracket(operatorStack.pop()):
      return 0
  
  completionString = ''
  while len(operatorStack) > 0:
    completionString += getClosingBracket(operatorStack.pop())
  return getPointsForString(completionString)

expressions = getLines('10-input.txt')
completionPoints = []
for expression in expressions:
  currExpressionPoints = getCompletionPoints(expression)
  if currExpressionPoints != 0:
    completionPoints.append(currExpressionPoints)
completionPoints.sort()
print(completionPoints[int(len(completionPoints) / 2)])