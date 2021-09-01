class Presence:
    link_download_linktext="Download"
    tab_react_id="tab-react"
    tab_angular_id="tab-angular"
    tab_vue_id="tab-vue"

    def __init__(self,driver):
        self.driver=driver

    def click_download(self):
        self.driver.find_element_by_link_text(self.link_download_linktext).click()



