from selenium.webdriver.common.by import By
class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"  # Поле ввода имени
    LAST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"  # Поле ввода фамилии
    METRO_STATION_INPUT = By.CLASS_NAME, "select-search__input"  # Поле ввода названия станции метро
    METRO_STATION_LIST = By.XPATH, "//ul/li" # Выпадающий список станций метро
    PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"  # Кнопка "Далее"
    RENT_FORM = By.XPATH, "//div[text()='Про аренду']"  # Раздел "Про аренду"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода адреса
    BLACK_CHECKBOX = By.ID, "black"  # Черный цвет самоката
    GREY_CHECKBOX = By.ID, "grey"  # Серый цвет самоката
    DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # Поле 'Когда привезти самокат'
    CALENDAR = By.XPATH, "//div[@class='react-datepicker']"  # Календарь
    RENT_TIME_LIST = By.CLASS_NAME, "Dropdown-root"  # Список выбора длительности аренды
    THREE_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='трое суток')]"  # Срок аренды трое суток
    FIVE_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='пятеро суток')]"  # Срок аренды пятеро суток
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Комментарий для курьера
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']" # Кнопка "Заказать"
    CONFIRM = By.XPATH, "//div[text()='Хотите оформить заказ?']" # Всплывающее окно подтверждения заказа
    YES_BUTTON = By.XPATH, "//button[text()='Да']"  # Кнопка "Да" на всплывающем окне подтверждения
    ORDER_SUCCESS_WINDOW = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]" # Всплывающее окно с заказом
    FOR_WHOM_IS_SCOOTER = [By.XPATH, ".//div[text()='Для кого самокат']"]  # Заголовок "Для кого самокат"