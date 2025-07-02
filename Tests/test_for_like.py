import pytest
import allure

from Config.links import links
from Base.base_test import BaseTest
from Base.base_page import BasePage
from playwright.async_api import async_playwright, expect

@allure.feature('Buzz page functionality')
class TestMain(BaseTest):

    @allure.title("Post and like")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_like_post(self):
        await self.login_page.open()
        await self.login_page.login(self.data.LOGIN)
        await self.login_page.password(self.data.PASSWORD)
        await self.login_page.submit_button()
        await self.dashboard_page.is_open()
        await self.dashboard_page.go_to_buzz_page()
        await self.buzz_page.is_open()
        await self.buzz_page.write_post()
        await self.buzz_page.post()
        await self.buzz_page.filter_likes()
        await self.buzz_page.check_first_post()
        await self.buzz_page.like_the_post()


