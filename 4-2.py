def getFileAsString(filename):
  file = open(filename)
  data = file.read()
  file.close()
  return data

def getNumsAndBoards(rawInput):
  inputChunks = rawInput.split('\n\n')
  numbersCalled = inputChunks[0].split(',')
  numbersCalled = [int(numberCalled) for numberCalled in numbersCalled]
  
  bingoBoards = inputChunks[1:]
  for i in range(len(bingoBoards)):
    bingoBoards[i] = bingoBoards[i].split('\n')
    for j in range(len(bingoBoards[i])):
      bingoBoards[i][j] = bingoBoards[i][j].strip().split(' ')
      bingoBoards[i][j] = list(filter(lambda val: val != '', bingoBoards[i][j]))
      bingoBoards[i][j] = [int(boardNumber) for boardNumber in bingoBoards[i][j]]

  return (numbersCalled, bingoBoards)

def isWinner(boardMarks):
  # Check all rows
  for i in range(5):
    if 0 not in [boardMarks[i][x] for x in range(5)]:
      return True
  # Check all columns
  for i in range(5):
    if 0 not in [boardMarks[x][i] for x in range(5)]:
      return True
  # No bingo found
  return False

def isBoardWinner(boardMarks, lastCalled):
  j,i = lastCalled
  # Check row
  rowOfLastMarked = [boardMarks[i][x] for x in range(5)]
  if 0 not in rowOfLastMarked:
    return True
  # Check column
  colOfLastMarked = [boardMarks[x][j] for x in range(5)]
  if 0 not in colOfLastMarked:
    return True
  # No bingo found
  return False

def markBoardsAndFindWinners(bingoBoards, boardMarks, numberCalled):
  indexOfWinners = []
  for boardNum in range(len(bingoBoards)):
    for i in range(5):
      for j in range(5):
        if bingoBoards[boardNum][j][i] == numberCalled:
          boardMarks[boardNum][j][i] = 1
          indexOfWinners = [x for x in range(len(bingoBoards)) if isBoardWinner(boardMarks[x], (j,i))]
  return indexOfWinners

def getBoardScore(board, marks, lastNumCalled):
  unmarkedSum = 0
  for i in range(5):
    for j in range(5):
      if (marks[i][j] == 0):
        unmarkedSum += board[i][j]
  print(unmarkedSum, '*', lastNumCalled)
  return unmarkedSum * lastNumCalled

# Main program
# DEFINITELY VERY UGLY, would love to clean up
numbersCalled, bingoBoards = getNumsAndBoards(getFileAsString('4-input.txt'))
boardMarks = [[[0 for i in range(5)] for j in range(5)] for k in range(len(bingoBoards))]

for numCalled in numbersCalled:
  winners = markBoardsAndFindWinners(bingoBoards, boardMarks, numCalled)
  bingoBoards = [bingoBoards[x] for x in range(len(bingoBoards)) if x not in winners]
  boardMarks = [boardMarks[x] for x in range(len(boardMarks)) if x not in winners]
  if len(bingoBoards) == 1:
    if not isWinner(boardMarks[0]):
      continue
    else:
      print(getBoardScore(bingoBoards[0], boardMarks[0], numCalled))
      break