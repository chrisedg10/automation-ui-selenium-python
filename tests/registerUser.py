import pytest
from pages.base import Base
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    """
    Fixture de configuración para inicializar la página base y el driver de Selenium.
    """
    base_page = Base()
    driver = base_page.get_driver()
    base_page.open_page(driver)
    yield driver
    base_page.quit_driver(driver)

def test_register_user(driver):
    """
    Test para registrar un nuevo usuario.
    """
    base = Base()

    # Inicializa la página de inicio y hacer clic en el botón de login/signup
    home_page = HomePage(driver)
    base.clickElement(home_page.get_loginAndSignupButton())

    # Inicializa la página de login y completar el formulario de registro
    login_page = LoginPage(driver)
    login_page.enter_text(login_page.get_nameField(), "Test User")
    login_page.enter_text(login_page.get_emailField(), "testUser@test.com")
    login_page.clickElement(login_page.get_signupField_button())