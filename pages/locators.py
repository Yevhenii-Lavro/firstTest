from selenium.webdriver.common.by import By


class SignInPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-name")
    BANKSEND_LOGO = (By.CSS_SELECTOR, "img.logo")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-danger")

class LoggedPageLocators():
    USER_LOGGED = (By.CSS_SELECTOR, ".chartjs-render-monitor[width]")

class DashboardPageLocators():
    DASHBOARD = (By.CSS_SELECTOR, ".chartjs-render-monitor[width]")
    TRANSACTIONS_BOARD_BUTTON = (By.CSS_SELECTOR, "tabset > ul > li:nth-child(1) > a")
    DAILY_SUMMARY_BUTTON = (By.CSS_SELECTOR, "#main-container ul > li:nth-child(2) > a")
    SUPERADMIN_DASHBOARD = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > a")
    SUPERADMIN_REPORTS = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(3) > a")
    SUPERADMIN_SETTINGS = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a")
    SUPERADMIN_COMPLIANCE = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(5) > a")
    DASHBOARD_TRANSACTION_LIST_TITLE = (By.CSS_SELECTOR, "div > div.block > div > h3")
    DASHBOARD_DAILY_SUMMARY_TITLE = (By.CSS_SELECTOR, "app-daily-summary-datatable > div > div > h3")
    FILTER_FROM = (By.CSS_SELECTOR, "#filterFrom")
    FILTER_TO = (By.CSS_SELECTOR, "#filterTo")
    RESET_BUTTON = (By.CSS_SELECTOR, ".ml-10")

