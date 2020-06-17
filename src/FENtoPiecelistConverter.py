from enum import Enum

class Notation(Enum):
  RAW=0
  ALGEBRAIC=1

def __fenToPiecelist(fen, lambda_map=lambda s: s, notation_type=Notation.RAW):
  files="abcdefgh"
  whitePiecelist=[]
  blackPiecelist=[]
  ranks = fen.split('/')
  rowcounter= 9
  for rank in ranks:
    rowcounter-=1
    filecounter = 1
    for curChar in rank:
      if curChar.isdigit():
        filecounter+= int(curChar)
        continue
      elif curChar.islower():
        if notation_type == Notation.ALGEBRAIC and curChar == 'p':
          blackPiecelist.append(files[filecounter-1] + str(rowcounter))
        else:
          blackPiecelist.append((lambda_map (curChar)) + files[filecounter-1] + str(rowcounter))
      else:
        if notation_type == Notation.ALGEBRAIC and curChar == 'P':
          whitePiecelist.append(files[filecounter-1] + str(rowcounter))
        else:
          whitePiecelist.append((lambda_map (curChar)) + files[filecounter-1] + str(rowcounter))
      filecounter+=1
  return (whitePiecelist, blackPiecelist)
 
def fenToAlgebraicPiecelist(fen, lambda_map=lambda s: s):
  return __fenToPieceList(fen, lambda_map=lambda_map, notation_type=Notation.ALGEBRAIC)

def fenToRawPiecelist(fen, lambda_map=lambda s: s):
  return __fenToPieceList(fen, lambda_map=lambda_map, notation_type=Notation.RAW)
