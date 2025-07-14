
from pages.base import Base
from selenium.webdriver.common.by import By

class HomePage(Base):
    # Selectores de la página de Inicio.
    loginAndSignupButton_str = "Signup / Login"

    def __init__(self, driver):
        """
        Constructor de la página de Home de instancia de WebDriver.
        """
        self.driver = driver

    # Métodos get que retornan los elementos WebElement.
    def get_loginAndSignupButton(self):
        return self.driver.find_element(By.LINK_TEXT, self.loginAndSignupButton_str)