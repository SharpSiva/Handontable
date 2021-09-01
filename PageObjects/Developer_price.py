from selenium.webdriver.support.ui import Select

class Dynamic_price:
    link_Pricing_link_text="Pricing"
    drp_amt_id="amount-select"
    def __init__(self,driver):
        self.driver=driver

    def drp_action(self):
        self.driver.find_element_by_link_text(self.link_Pricing_link_text).click()
