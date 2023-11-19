import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть на элемент')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Найти элемент на странице')
    def find_my_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Дождаться открытия новой вкладки')
    def wait_for_new_tab(self, index):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(index))

    @allure.step('Дождаться открытия страницы {url}')
    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))
