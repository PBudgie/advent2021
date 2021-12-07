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

def findWinner(boardMarks, lastCalled):
  i,j = lastCalled
  # Check row
  rowOfLastMarked = [boardMarks[i][x] for x in range(5)]
  if 0 not in rowOfLastMarked:
    return True
  # Check column
  colOfLastMarked = [boardMarks[x][j] for x in range(5)]
  if 0 not in colOfLastMarked:
    return True
  """
  # Check first diagonal, if on diagonal
  if i == j:
    diagonalOfLastMarked = [boardMarks[x][x] for x in range(5)]
    if 0 not in diagonalOfLastMarked:
      return True
  # Check second diagonal, if on diagonal
  if i + j == 4:
    diagonalOfLastMarked = [boardMarks[x][4-x] for x in range(5)]
    if 0 not in diagonalOfLastMarked:
      return True
  """
  # No bingo found
  return False

def markBoardsAndFindWinner(bingoBoards, boardMarks, numberCalled):
  for boardNum in range(len(bingoBoards)):
    for i in range(5):
      for j in range(5):
        if bingoBoards[boardNum][i][j] == numberCalled:
          boardMarks[boardNum][i][j] = 1
          foundWinner = findWinner(boardMarks[boardNum], (i,j))
          if foundWinner:
            return boardNum
  return -1

def getBoardScore(board, marks, lastNumCalled):
  unmarkedSum = 0
  for i in range(5):
    for j in range(5):
      if (marks[i][j] == 0):
        unmarkedSum += board[i][j]
  print(unmarkedSum, '*', lastNumCalled)
  return unmarkedSum * lastNumCalled

# Main program
numbersCalled, bingoBoards = getNumsAndBoards(getFileAsString('4-input.txt'))
boardMarks = [[[0 for i in range(5)] for j in range(5)] for k in range(len(bingoBoards))]

for numCalled in numbersCalled:
  winner = markBoardsAndFindWinner(bingoBoards, boardMarks, numCalled)
  if winner != -1:
    print(getBoardScore(bingoBoards[winner], boardMarks[winner], numCalled))
    break