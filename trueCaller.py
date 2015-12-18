from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

print "initializing display"
display = Display(visible=0, size=(800, 600))
display.start()
print "initialized display"
print "initializing yahoo"
browser = webdriver.Firefox()
browser.get('http://www.truecaller.com/sign-in/yahoo')
browser.implicitly_wait(20)
print "initialized yahoo"
print "loggin yahoo"
browser.find_element_by_name('username').send_keys( < username > )
browser.find_element_by_name('passwd').send_keys( < password > )
browser.find_element_by_id("login-signin").click()
wait = WebDriverWait(browser, 10)
wait.until(lambda driver: driver.current_url == "http://www.truecaller.com/sign-in/yahoo")
# browser.
print "loged yahoo"
browser.get("https://www.truecaller.com/in/<number>")

html = browser.page_source
soup = BeautifulSoup(html, "lxml")

mydivs = soup.find("div", {"class": "detailView__nameText"})
print mydivs.get_text().strip()
# print type(mydivs)
# mydivsSoup = BeautifulSoup(mydivs[0])
# print mydivsSoup.div
browser.quit()

display.stop()
