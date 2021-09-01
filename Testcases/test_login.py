
from PageObjects.Login import LoginPage
from utilities.logger import Log_generate

class Test_id001_login:
    url="https://handsontable.com/"
    email_id="sivasankarqae@gmail.com"
    password="Testtest@123"
    log=Log_generate.log_gen()

    def test_homepagetest(self,setup):
        self.log.info("*******Test_id12_login**********")
        self.driver =setup
        self.driver.get(self.url)
        act_title=self.driver.title
        if act_title=="Handsontable is a JavaScript data grid that looks and feels like a spreadsheet | Available for React, Angular and Vue":
            assert True
            self.driver.close()
            self.log.info("********test_homepagetest is passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetest.png")
            self.driver.close()
            self.log.error("***************test_homepagetest is failed********************")
            assert False


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.clicksig_HP()
        self.driver.implicitly_wait(10)
        self.lp.setemail_id(self.email_id)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title

        if act_title=="Sign In":
            assert True
            self.driver.close()
            self.log.info("********test_login is passed*********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetest.png")
            self.driver.close()
            self.log.error("***************test_login is failed********************")
            assert False


