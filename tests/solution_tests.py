import sys
sys.path.append("../src/")
import SolutionScraper as solScrape

def __test1(driver):
  print("\nTEST 1:")
  solution = solScrape.urlToSolution(driver,'https://www.chess.com/puzzles/problem/793')
  print(solution)

def __test2(driver):
  print("\nTEST 2:")
  solution = solScrape.urlToSolution(driver,'https://www.chess.com/puzzles/problem/111714')
  print(solution)

def __test3(driver):
  print("\nTEST 3:")
  solution = solScrape.urlToSolution(driver,'https://www.chess.com/puzzles/problem/1127606')
  print(solution)
  
def __test4(driver):
  print("\nTEST 4:")
  solution = solScrape.urlToSolution(driver,'https://www.chess.com/puzzles/problem/39373')
  print(solution)

def test_all():
  print("URL TO SOLUTION TEST:")
  driver= solScrape.login()
  __test1(driver)
  __test2(driver)
  __test3(driver)
  __test4(driver)
  driver.close()