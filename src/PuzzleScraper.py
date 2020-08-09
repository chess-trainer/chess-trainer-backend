from bs4 import BeautifulSoup
import requests
import re
from FENtoPiecelistConverter import fenToAlgebraicPiecelist
import SolutionScraper

class problem:
    def __init__(self, fen, attributes,url,solution):
        self.FEN = fen
        self.algWhitePiecelist, self.algBlackPieceList = fenToAlgebraicPiecelist(fen, lambda_map=lambda s: s)
        self.ID = int(attributes[0].text.strip())
        self.Rating = int(attributes[1].text.strip())
        self.Attempts = int(attributes[2].text.strip())
        self.PassPercent = attributes[3].text.strip()
        self.NumMoves = int(attributes[4].text.strip())
        self.AvgTime = attributes[5].text.strip()
        self.PlayAsColor = attributes[6].text.strip()
        self.URL= url
        self.Solution=solution
    
        
problems=[]
page = requests.get('https://www.chess.com/puzzles/problems?page=1')
soup = BeautifulSoup(page.content, 'html.parser')
pagemax = soup.find(id='view-tactics-problems').get('data-total-pages')
driver = SolutionScraper.login()
for pagenum in range(1, int(pagemax) + 1):
    if pagenum!=1:
        page = requests.get('https://www.chess.com/puzzles/problems?page=' + str(pagenum))
        soup = BeautifulSoup(page.content, 'html.parser')
    problemshtml = soup.find_all(class_='v-board-popover')    
    for problemhtml in problemshtml:
        try:
            fen = re.search("fen: '(.+?) ", problemhtml.get('v-board-popover')).group(1)
        except AttributeError:
            fen =''
        #The attributes are id, Rating, Attempts, PassPercent, NumMoves, AvgTime, PlayAsColor
        attributes = problemhtml.find_all('a')
        url=attributes[0].get('href')
        solution = SolutionScraper.urlToSolution(driver,url)
        problems.append(problem(fen,attributes,url,solution))
driver.close()

