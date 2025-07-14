from pages.base import Base
from selenium.webdriver.common.by import By

class LoginPage(Base):
    # Selectores de la pagina de Login.
    nameField_str = "[data-qa='signup-name']"  
    emailField_str = "[data-qa='signup-email']"  
    signupField_button = "[data-qa='signup-button']"  

    def __init__(self, driver):
        """
            Constructor de la página de Login de instancia de WebDriver.
        """
        self.driver = driver

    
    # Métodos get que retornan los elementos WebElement.
    def get_nameField(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.nameField_str)

    def get_emailField(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.emailField_str)

    def get_signupField_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.signupField_button)