import sys
sys.path.append("../src/")
import FENtoPiecelistConverter as FEN

def __test1():
  print("\nTEST 1:")
  whitePieces,blackPieces = FEN.fenToAlgebraicPiecelist('1r4kR/1p2nrb1/p2qp1p1/4NpQ1/3P4/3B2P1/PP3P2/1K5R', lambda_map=lambda s: s)
  for whitePiece in whitePieces:
    print(whitePiece)
  print('\n')
  for blackPiece in blackPieces:
    print(blackPiece)

def __test2():
  print("\nTEST 2:")
  whitePieces,blackPieces = FEN.fenToRawPiecelist('1r4kR/1p2nrb1/p2qp1p1/4NpQ1/3P4/3B2P1/PP3P2/1K5R', lambda_map=lambda s: s.lower())
  for whitePiece in whitePieces:
    print(whitePiece)
  print('\n')
  for blackPiece in blackPieces:
    print(blackPiece)

def test_all():
  print("FEN TO PIECE LIST TEST:")
  __test1()
  __test2()
