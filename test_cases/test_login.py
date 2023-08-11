import time

from Utilities.Logger import LogGenerator
from pageObjects.LoginObject import OrangeHRM_Login


class Test_Login_001:
    log = LogGenerator.loggen()

    def test_title_page(self, browser):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = browser
        self.log.info("Page Title is " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("E:\\Software Testing Class Notes\\Python\Scrach To "
                                        "Best\\Screenshot\\test_title001(Pass).png")
            self.log.info("Testcase test_page_title_001 is passed\n")
            assert True
        else:
            self.driver.save_screenshot("E:\\Software Testing Class Notes\\Python\Scrach To "
                                        "Best\\Screenshot\\test_title001(Fail).png")
            self.log.info("Testcase test_page_title_001 is failed\n")
            assert False

    def test_login_002(self, browser):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = browser
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.enter_username("Admin")
        self.log.info("Entering password")
        self.lp.enter_password("admin123")
        self.log.info("Clicking in login button")
        self.lp.Login_Button()
        self.log.info("Checking Dashboard Logo")
        if self.lp.Dashboard_logo() == True:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("E:\\Software Testing Class Notes\\Python\\Scrach To "
                                        "Best\\Screenshot\\test_login_002(Pass).png")
            self.log.info("Clicking on Menu button")
            self.lp.logout_menu()
            self.log.info("Clicking on logout button")
            self.lp.logout()
            self.log.info("Testcase test_login_002 is passed\n\n")
            assert True
        else:
            self.driver.save_screenshot("E:\\Software Testing Class Notes\\Python\\Scrach To "
                                        "Best\\Screenshot\\test_login_002(Fail).png")
            self.log.info("Testcase test_login_002 is Failed\n\n")
            assert False
