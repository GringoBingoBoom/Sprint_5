from selenium.webdriver.common.by import By


class Locators:
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка 'Войти в аккаунт'
    LINK_TO_REGISTER = (By.XPATH, "//*[text()='Зарегистрироваться']")  # ссылка 'Зарегистрироваться'

    INPUT_REGISTER_NAME = (By.XPATH, ".//*[text()='Имя']/../input")  # поле ввода имени при регистрации
    INPUT_REGISTER_EMAIL = (By.XPATH, ".//*[text()='Email']/../input")  # поле ввода email при регистрации
    INPUT_REGISTER_PASSWORD = (By.XPATH, ".//*[text()='Пароль']/../input")  # поле ввода пароля при регистрации

    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка 'Войти в аккаунт'

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка 'Личный Кабинет'

    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")  # заголовок страницы РЕГИСТРАЦИЯ
    SIGN_IN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # заголовок страницы ВХОД

    ALARM_WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # предупреждение Некорректный пароль

    BUTTON_SIGNIN = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти

    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок главной Соберите бургер

    BUTTON_SIGNIN_ON_REGISTER_PAGE = (By.XPATH, "//a[text()='Войти']")  # кнопка Войти

    PROFILE = (By.XPATH, "//a[text()='Профиль']")  # Профиль

    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Конструктор
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход из личного кабинета

    BUNS = (By.XPATH, "//span[text()='Булки']")  # Конструктор Булки
    SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Конструктор Соусы
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Конструктор Начинки
