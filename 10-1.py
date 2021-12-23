def getLines(filename):
  with open(filename) as inputFile:
    rawLines = inputFile.readlines()
    for i, line in enumerate(rawLines):
      rawLines[i] = line.strip()
    return rawLines

# Returns appropriate points if expressoin is corrupted,
# and 0 if expression is correct or incomplete.
def getCorruptedPoints(expression): 
  operatorStack = []
  for i in range(len(expression)):
    currChar = expression[i]
    if currChar in ['(', '[', '{', '<']:
      operatorStack.append(expression[i])
    elif currChar in [')', ']', '}', '>']:
      lastStackOperator = operatorStack.pop()
      if currChar == ')' and lastStackOperator != '(':
        return 3
      elif currChar == ']' and lastStackOperator != '[':
        return 57
      elif currChar == '}' and lastStackOperator != '{':
        return 1197
      elif currChar == '>' and lastStackOperator != '<':
        return 25137
  return 0

expressions = getLines('10-input.txt')
errorScore = 0
for expression in expressions:
  errorScore += getCorruptedPoints(expression)
print(errorScore)