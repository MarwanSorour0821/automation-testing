import selenium

class BaseClass():
    def __init__(self) -> None:
        self.driver = selenium.webdriver.Chrome()
