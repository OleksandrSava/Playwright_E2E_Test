import allure
from Config.links import links
from Base.base_page import BasePage

class LoginPage(BasePage):

     PAGE_URL = links.LOGIN_PAGE

     @allure.step('Write login')
     async def login(self, login):
          LOGIN_FIELD =  self.page.get_by_placeholder("Username")
          await self.expect(LOGIN_FIELD).to_be_visible()
          await LOGIN_FIELD.fill(login)

     @allure.step('Write password')
     async def password(self, password):
          PASSWORD_FIELD =  self.page.get_by_placeholder("Password")
          await self.expect(PASSWORD_FIELD).to_be_visible()
          await PASSWORD_FIELD.fill(password)

     @allure.step('Click submit')
     async def submit_button(self):
          SUBMIT_BUTTON = self.page.get_by_role('button', name='Login')
          await self.expect(SUBMIT_BUTTON).to_be_visible()
          await SUBMIT_BUTTON.click()
