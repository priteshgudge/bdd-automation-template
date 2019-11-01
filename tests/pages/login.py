from framework.webapp import webapp
import re


class Login():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_login_form(self):
        form = self.driver.find_element_by_id('signin_form').text
        assert form is not None

    def action_enter_credentials(self, email, password):
        email = self.driver.find_element_by_id('loginEmail')
        password = self.driver.find_element_by_name('password')
        email.send_keys("Email@email.com")
        password.send_keys("Password")
        sigin = self.driver.find_element_by_class_name('btn_sign_in')
        sigin.click()

    def verify_incorrect_credentials_message(self, message):
        msg = re.sub(r'\W+', '', message)
        self.driver.switch_to_active_element()
        error_message = self.driver.find_element_by_class_name('errMsg').text
        err_msg = re.sub(r'\W+', '', error_message)
        #3print(error_message, msg)
        assert err_msg == msg

login = Login.get_instance()
