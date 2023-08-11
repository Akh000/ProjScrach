from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM_Login:
    username_name_xpath = (By.XPATH, "//input[@placeholder='Username']")
    password_xpath = (By.XPATH, "//input[@placeholder='Password']")
    login_button_xpath = (By.XPATH, "//button[@type='submit']")
    logout_menu_xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    logout_button_CSS = (By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)")
    dashboard_xpath = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.username_name_xpath))
        self.driver.find_element(*OrangeHRM_Login.username_name_xpath).send_keys(username)

    def enter_password(self, pswd):
        self.wait.until(expected_conditions.visibility_of_element_located(self.password_xpath))
        self.driver.find_element(*OrangeHRM_Login.password_xpath).send_keys(pswd)

    def Login_Button(self):
        self.driver.find_element(*OrangeHRM_Login.login_button_xpath).click()

    def logout_menu(self):
        self.driver.find_element(*OrangeHRM_Login.logout_menu_xpath)

    def logout(self):
        self.driver.find_element(*OrangeHRM_Login.logout_button_CSS)

    def Dashboard_logo(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.dashboard_xpath))
            self.driver.find_element(*OrangeHRM_Login.dashboard_xpath)
            return True
        except:
            return False
