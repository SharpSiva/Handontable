from selenium.webdriver.support.ui import Select
from PageObjects.Developer_price import Dynamic_price
from utilities.logger import Log_generate

class Test_id002_Pricing:
    url = "https://handsontable.com/"
    log=Log_generate.log_gen()

    def test_dev_price(self, setup):
        self.log.info("*******Test_id002_Pricing**********")

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dp=Dynamic_price(self.driver)
        self.dp.drp_action()
        amt = self.driver.find_element_by_id(self.dp.drp_amt_id)
        selcet = Select(amt)
        self.log.info("*******Verify dynamic price for different drop down**********")

        for i in range(1, 10):
            selcet.select_by_value(str(i))
            price = self.driver.find_element_by_id("dynamic-price").text
            basic = 790
            if i == 1:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 2:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 3:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 4:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 5:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 6:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 7:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 8:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            elif i == 9:
                if price == "$" + str(i * basic):
                    assert True
                else:
                    assert False
            self.driver.implicitly_wait(3)