from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = By.XPATH, "//button[contains(@class, 'App_CookieButton_')]"  # Кнопка "Да все привыкли"
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    ORDER_BUTTON_BIG = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    QUESTIONS = By.CLASS_NAME, "accordion"  # Вопросы о важном
    QUESTION_LOCATOR = By.XPATH, "//*[@id = 'accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]/p'
    YANDEX_LOGO = [By.XPATH, ".//img[@alt = 'Yandex']"]   # логотип "Яндекс" в шапке главной страницы
    SAMOKAT_LOGO = [By.XPATH, ".//img[@alt = 'Scooter']"]  # логотип "Самокат" в шапке главной страницы
