import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    #Login with prepared registered email
    def test_login(self):
        driver = self.driver
        url = 'https://trello.com/'
        driver.get(url)

        #"Zaloguj" click
        main_page_login_button = driver.find_element_by_xpath('//*[@class="btn btn-sm btn-link text-white"]')
        main_page_login_button.click()

        #Username insert
        email_input_element = driver.find_element_by_id("user")
        email_input_element.send_keys('test.email08102019@gmail.com')

        #Login button click
        login_button = driver.find_element_by_id("login")
        login_button.click()

        #Wait webpage to load
        driver.implicitly_wait(5)

        #Check value of an email
        inputed_email_element = driver.find_element_by_id("username")
        inputed_email_element_value = inputed_email_element.get_attribute('value')
        print(f"Current email adress used to log in: {inputed_email_element_value}")

        self.assertEqual('test.email08102019@gmail.com', inputed_email_element_value,
                         f'Expected email differs from current email: {inputed_email_element_value}')

        #Submit login and confirm with a password
        login_submit_button = driver.find_element_by_id("login-submit")
        login_submit_button.click()

        driver.implicitly_wait(5)

        password_input_element = driver.find_element_by_id("password")
        password_input_element.send_keys('123456789IOP')

        login_submit_button = driver.find_element_by_id("login-submit")
        login_submit_button.click()

        #Logout
        member_menu_button = driver.find_element_by_xpath('//*[@data-test-id="header-member-menu-button"]')
        member_menu_button.click()

        logout_element = driver.find_element_by_xpath('//span[text() = "Wyloguj"]')
        logout_element.click()

    def test_register_with_existing_email(self):
        driver = self.driver
        url = 'https://trello.com/signup'
        driver.get(url)

        #Try to signup with an existing email
        email_input_element = driver.find_element_by_id("email")
        email_input_element.send_keys('test.email08102019@gmail.com')

        signup_button = driver.find_element_by_id("signup")
        signup_button.click()

        driver.implicitly_wait(5)

        #Input name and password
        name_input_element = driver.find_element_by_id("name")
        name_input_element.send_keys('Jan Testowy')

        password_input_element_registration = driver.find_element_by_id("password")
        password_input_element_registration.send_keys('12345678')

        signup_submit_button = driver.find_element_by_id("signup")
        signup_submit_button.click()

        login_prompt_element = driver.find_element_by_id("login-prompt")

        # Expecting warning to be shown with an information about email was already used
        if login_prompt_element.is_enabled():
            print(f'Expected message visible: {login_prompt_element.get_attribute("innerText")}')
        else:
            self.fail("Expected message is not visible")




    @classmethod
    def tearDownClass(self):
        self.driver.quit()
