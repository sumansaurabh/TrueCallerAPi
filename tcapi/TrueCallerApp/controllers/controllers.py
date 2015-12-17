# Controller
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import logging

class Controller():

    def __init__(self, trueCaller):
        self.trueCaller=trueCaller

    def setUrl(self, location, number):
        # Must be initialized form configuration
        self.url = "https://www.truecaller.com/in/"+number
        
    def getTrueCallerData(self):
        
        logging.info("Getting URL")
        self.trueCaller.browser.get(self.url)
        logging.debug("Waiting for URL get to be finished")
        wait = WebDriverWait(self.trueCaller.browser, 10)
        wait.until(lambda browser: self.trueCaller.browser.current_url == self.url)
        logging.debug("Getting HTML Page source")
        html = self.trueCaller.browser.page_source
        soup = BeautifulSoup(html)
        userName = soup.find("div", {"class": "detailView__nameText"})
        logging.debug("searched userName is"+ userName.get_text().strip())
        return userName.get_text().strip()
