import logging
import os

from pyvirtualdisplay import Display
from selenium import webdriver
import yaml


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TrueCaller():

    """TrueCaller Module injected as dependency"""

    def __init__(self, *args, **kwargs):
        """Initializing TrueCaller APi"""

        logger.info('Initializing TrueCaller')

        logger.debug("Initalizing Display")
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        logger.debug("Initalized Display")

        logger.debug("Initalizing Firefox")
        self.browser = webdriver.Firefox()
        logger.debug("Initalized Firefox")
        self.url()
        self.__YAHOO_USERNAME = os.environ[self.username]
        self.__YAHOO_PASSWORD = os.environ[self.password]

    def initializeLogin(self):
        """Initalizing login for accessing TrueCaller"""

        logger.debug("Sigining In to Yahoo")
        self.browser.get(self.url)
        #self.wait = WebDriverWait(self.browser, 20)
        #self.wait.until(lambda driver: driver.current_url == self.url)
        
        self.browser.find_element_by_name('username').send_keys(self.__YAHOO_USERNAME)
        self.browser.find_element_by_name('passwd').send_keys(self.__YAHOO_PASSWORD)
        self.browser.find_element_by_id("login-signin").click()

        

        logger.debug("Sigined In to Yahoo")
        logger.info("TrueCaller Initalized")
        
    def url(self):
        with open('tcapi/TrueCallerApp/modules/TrueCallerInit/config.yaml', 'r') as f:
            doc = yaml.load(f)
        self.url = doc["truecaller"]["login"]
        self.username = doc["truecaller"]["username"]
        self.password = doc["truecaller"]["password"]
        