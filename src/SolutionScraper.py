from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import re
import userPass

def login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.chess.com/login")
    payload=userPass.getUserPass()
    userelem = driver.find_element_by_id("username")
    userelem.clear()
    userelem.send_keys(payload[0])
    pswdelem = driver.find_element_by_id("password")
    pswdelem.clear()
    pswdelem.send_keys(payload[1])
    pswdelem.send_keys(Keys.RETURN)
    return driver
    
def urlToSolution(driver,url):
    driver.get(url)  
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    problemhtml = soup.find(id="puzzle-features")
    solutionData=problemhtml.get('data-puzzle')
#This regular expression,\[FULL \\\"(.+?)\\\"\], should work but isn't 
#so substring is a ghetto fix
    try: 
        solution = re.search("\[FULL (.+?)\"\]", solutionData).group(1)[2:-1]
    except:
#again (1\. .+)\\n\d" should work but isn't
        solution = re.search("(1\. .+)", solutionData).group(1)[0:-11]
    return solution