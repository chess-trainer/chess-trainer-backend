from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import re

#Could make username and password parameters
def login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.chess.com/login")
    #Need to create a disposable account or hide password
    userelem = driver.find_element_by_id("username")
    userelem.clear()
    userelem.send_keys("kiblitz")
    pswdelem = driver.find_element_by_id("password")
    pswdelem.clear()
    pswdelem.send_keys("temporary123")
    pswdelem.send_keys(Keys.RETURN)
    return driver
    
def urlToSolution(driver,url):
    driver.get(url)  
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    problemhtml = soup.find(id="puzzle-features")
    solutionData=problemhtml.get('data-puzzle')
#This regular expression should work but it isn't \[FULL \\\"(.+?)\\\"\]
#so substring is a ghetto fix
    solution = re.search("\[FULL (.+?)\"\]", solutionData).group(1)[2:-1]
    return solution
