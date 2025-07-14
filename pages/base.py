
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Base:
    # Clase base para los Page Objects.
    URL = "http://automationexercise.com/"

    """
    Métodos que inicializan y retorna una instancia de WebDriver para Chrome,
    también proporciona métodos para cerrar el driver.
    """
    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def quit_driver(self, driver):
        driver.quit()

    """
    Métodos utilitarios para la gestión del driver y acciones comunes sobre elementos.
    """
    def open_page(self, driver):
        # Abre la URL principal del sitio en el navegador.
        driver.get(self.URL)

    def enter_text(self, element, text):
        # Ingresa texto en un campo de entrada (input).
        element.clear()
        element.send_keys(text)

    def clickElement(self, element):
        # Hace clic sobre un elemento WebElement.
        element.click()