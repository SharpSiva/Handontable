from PageObjects.element_in_downloads import Presence
from utilities.logger import Log_generate

class Test_id003_is_present:
    url = "https://handsontable.com/"
    log=Log_generate.log_gen()

    def test_presence(self, setup):
        self.log.info("*******Test_id003_is_present**********")

        self.driver = setup
        self.driver.get(self.url)
        self.ele = Presence(self.driver)
        self.ele.click_download()
        React=self.driver.find_element_by_id(self.ele.tab_react_id)
        Angular=self.driver.find_element_by_id(self.ele.tab_angular_id)
        Vue=self.driver.find_element_by_id(self.ele.tab_vue_id)
        if React.is_displayed() and Angular.is_displayed() and Vue.is_displayed():
            self.log.info("*******Expected elements are shown**********")
            assert True
        else:
            self.log.error("*******Expected elements are not shown**********")
            assert False

