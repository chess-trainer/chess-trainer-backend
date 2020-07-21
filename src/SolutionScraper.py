from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

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