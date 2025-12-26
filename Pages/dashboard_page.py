import allure
from Config.links import links
from Base.base_page import BasePage


class DashboardPage(BasePage):

    PAGE_URL = links.DASHBOARD_PAGE

    @allure.step('Go to Buzz page')
    async def go_to_buzz_page(self):
        BUZZ_LINK =  self.page.get_by_role('link', name='Buzz')
        await self.expect(BUZZ_LINK).to_be_visible()
        await BUZZ_LINK.click()

