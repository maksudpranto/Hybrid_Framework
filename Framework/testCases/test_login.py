from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepage_title(self, setup):
        self.logger.info("******* Test_001_Login********")
        self.logger.info("****** Verifying Homepage Title**********")

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** Homepage Title Test Passed ******")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "testHomepageTitle.png")
            self.driver.close()
            self.logger.info("****** Homepage Title Test Failed ******")
            assert False

    def test_login(self, setup):
        self.logger.info("******* Verifying Login Test ********")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actual_title = self.driver.title
        self.driver.close()

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***** Login Test Passed *****")
        else:
            assert False










