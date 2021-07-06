"""
Assignment 06
Atiq Sujela
CSE 30 Spring 2021
"""
import sys


def loadGrid(gridstr):
  g1 = gridstr.split('\n')
  g1 = list(filter(None, g1))
  return [list(c) for c in g1]


def loadDict(nm, gl, dp: str):
  with open(dp) as df:
    return {str(li.strip().upper()) for li in df if len(li.strip()) >= nm and len(li.strip()) <= gl}


def getRows(grida):
  return ["".join(li) for li in grida]


def getColumns(grida):
  """
  Creates columns from the main grida
  """
  c = []
  cstring = ""
  for i in range(len(grida)):
    for j in range(len(grida)):
      cstring += grida[j][i]
    c.append(cstring)
    cstring = ""
  return c


def parseString(wordStr, minNum):
  """
  This Function creates all possible substrings for a word
  """
  length = len(wordStr)
  temp = []
  for i in range(length):
    if length - i >= minNum:
      for j in range(length, minNum - 1, -1):
        if j - i >= minNum:
          if i == 0 and j == length:
            continue
          else:
            temp.append(wordStr[i:j])
        else:
          break
  return temp


def inDictionary(index1, index2, w):
  global dictionary
  if index2 >= index1:
    mid = index1 + (index2 - index1) // 2
    if dictionary[mid] == w:
      return True
    elif dictionary[mid] > w:
      return inDictionary(index1, mid - 1, w)
    else:
      return inDictionary(mid + 1, index2, w)
  else:
    return False


def searchWords(minNum, grida):
  """
  This function searches if a word is in a dictionary
  """
  global dictionary
  dict_size = len(dictionary)
  h = getRows(grida)
  c = getColumns(grida)
  d1 = getLDiagonal(minNum, grida)
  d2 = getRDiagonal(minNum, grida)
  gridlist = h + c + d1 + d2
  gridlist2 = reverseString(gridlist)
  gridlist = gridlist + gridlist2
  for i in gridlist:
    if len(i) > minNum:
      gridlist = gridlist + parseString(i, minNum)
  gridset = set(gridlist)
  gridset = sorted(gridset)
  return {word for word in gridset if inDictionary(0, dict_size, word)}


def getLDiagonal(minNum, grida):
  """
  Creates diagnals originating from the left
  from the main grida
  """
  ldiagonal = []
  dstring = ""
  c = 0
  for i in range(len(grida)):
    c = i
    dstring = ""
    for j in range(len(grida)):
      if c < len(grida):
        dstring += grida[c][j]
        c += 1
      else:
        break
    if len(dstring) > minNum:
      ldiagonal.append(dstring)
      dstring = ""
    else:
      if len(dstring) == minNum:
        ldiagonal.append(dstring)
      break
  for i in range(1, len(grida)):
    c = i
    dstring = ""
    for j in range(len(grida)):
      if c < len(grida):
        dstring += grida[j][c]
        c += 1
      else:
        break
    if len(dstring) > minNum:
      ldiagonal.append(dstring)
      dstring = ""
    else:
      if len(dstring) == minNum:
        ldiagonal.append(dstring)
      break
  return ldiagonal


def reverseString(arr):
  newi = ""
  new_arr = []
  for i in arr:
    newi = i[::-1]
    new_arr.append(i)
    new_arr.append(newi)
  return new_arr


def getRDiagonal(minNum, grida):
  """
  Creates diagnals originating from the right
  from the main grida
  """
  rdiagonal = []
  dstring = ""
  c = 0
  for i in range(len(grida) - 1, 0, -1):
    c = i
    dstring = ""
    for j in range(len(grida)):
      if c > -1:
        dstring += grida[c][j]
        c -= 1
      else:
        break
    if len(dstring) > minNum:
      rdiagonal.append(dstring)
      dstring = ""
    else:
      if len(dstring) == minNum:
        rdiagonal.append(dstring)
      break

  for i in range(1, len(grida)):
    c = i
    dstring = ""
    for j in range(len(grida) - 1, 0, -1):
      if c < len(grida):
        dstring += grida[j][c]
        c += 1
      else:
        break
    if len(dstring) > minNum:
      rdiagonal.append(dstring)
      dstring = ""
    else:
      if len(dstring) == minNum:
        rdiagonal.append(dstring)
      break
  return rdiagonal


if __name__ == '__main__':
  minimum_number = int(sys.argv[1])
  dict_path = sys.argv[2]
  grid_str = sys.stdin.read()
  grid = loadGrid(grid_str)
  dictionary = sorted(loadDict(minimum_number, len(grid), dict_path))
  answers = sorted(searchWords(minimum_number, grid))
  for word in answers:
    print(word)
