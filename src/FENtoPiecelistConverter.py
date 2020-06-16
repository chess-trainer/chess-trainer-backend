files="abcdefgh"
def getPiecelist(fen):
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
                if curChar == 'p':
                    blackPiecelist.append(files[filecounter-1] + str(rowcounter))
                else:
                    blackPiecelist.append(curChar.upper() + files[filecounter-1] + str(rowcounter))
            else:
                if curChar == 'P':
                    whitePiecelist.append(files[filecounter-1] + str(rowcounter))
                else:
                    whitePiecelist.append(curChar + files[filecounter-1] + str(rowcounter))
            filecounter+=1
    return (whitePiecelist, blackPiecelist)

# Test
# whitePieces,blackPieces = getPiecelist('1r4kR/1p2nrb1/p2qp1p1/4NpQ1/3P4/3B2P1/PP3P2/1K5R')   
# for whitePiece in whitePieces:
#     print(whitePiece)
# print('\n')
# for blackPiece in blackPieces:
#     print(blackPiece)     
