
class LoginPage:
    button_xpath_signin="/html/body/header/div[2]/div[2]/nav/ul/li[9]/a"
    textbox_email_name="email"
    textbox_password_name="password"
    button_signin_xpath="//input[@value='SIGN IN']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver
    def setemail_id(self,email_id):
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email_id)

    def setpassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicksig_HP(self):
        self.driver.find_element_by_xpath(self.button_xpath_signin).click()

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
