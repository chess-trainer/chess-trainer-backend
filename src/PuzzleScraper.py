from bs4 import BeautifulSoup
import requests
import re

page = requests.get('https://www.chess.com/puzzles/problems?fbclid=IwAR1GA26iG8uMy5gxWRp1X8X3nYBzSExelBBsKjEZev2Gl9JKxxlkGjIZaSU')
soup = BeautifulSoup(page.content, 'html.parser')

problems = soup.find_all(class_='v-board-popover')

for problem in problems:
    problem.get('v-board-popover')
    try:
        FEN = re.search("fen: '(.+?) ", problem.get('v-board-popover')).group(1)
    except AttributeError:
        FEN =''
    ID, Rating, Attempts, PassPercent, NumMoves, AvgTime, PlayAs = problem.find_all('a')
    print(FEN)
    print(Rating.text.strip())
    print(NumMoves.text.strip())
    print(PlayAs.text.strip())

    
