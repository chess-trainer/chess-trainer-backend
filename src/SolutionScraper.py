from bs4 import BeautifulSoup
import requests

#Need to create a disposable account or hide password
payload = {
    '_username': 'kiblitz',
    '_password': 'temporary123'
}

def urlToSolution(url):
    with requests.Session() as session:
        test=session.post('https://www.chess.com/login_check', data=payload)
        print(test.status_code)
        
        homepage= session.get('https://www.chess.com/home')
        print(homepage.text)
        page = session.get(url)
#         print(test.text)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        problemhtml = soup.find(id="puzzle-features")
        print(problemhtml.prettify()) 
        solutionData=problemhtml.get('data-puzzle')
        print(solutionData)
    
    #test to
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     problemhtml = soup.find(id="puzzle-features")
#     print(problemhtml.prettify())
#     solutionData=problemhtml.get('data-puzzle')
#     print(solutionData)
#     
    
urlToSolution('https://www.chess.com/puzzles/problem/793')