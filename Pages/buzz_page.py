import allure
from Config.links import links
from Base.base_page import BasePage


class BuzzPage(BasePage):

    FILL_FOR_POST = 'Test-pw'
    PAGE_URL = links.BUZZ_PAGE

    @allure.step('Fill info in post')
    async def write_post(self):
        POST_INPUT =  self.page.locator('.oxd-buzz-post-input')
        await self.expect(POST_INPUT).to_be_visible()
        await POST_INPUT.fill(self.FILL_FOR_POST)

    @allure.step('Click post button')
    async def post(self):
        POST_BUTTON = self.page.locator('.oxd-button--main')
        await self.expect(POST_BUTTON).to_be_visible()
        await POST_BUTTON.click()

    @allure.step('Sort by Most Likes')
    async def filter_likes(self):
        MOST_LIKED_POST =  self.page.get_by_role('button', name='Most liked Posts')
        await self.expect(MOST_LIKED_POST).to_be_visible()
        await MOST_LIKED_POST.click()

    @allure.step('Check if first post already liked')
    async def check_first_post(self) -> bool:
        HEART_WRAPPER =  self.page.locator("(//path[@id='heart'])[1]/ancestor::div[contains(@class, 'orangehrm-like-animation')]")
        count = await HEART_WRAPPER.count()
        if count > 0:
            return True
        else: return False

    @allure.step('Find post without like and like it ')
    async def like_the_post(self):
        LIKE_BUTTON = self.page.locator("(//*[@class='orangehrm-heart-icon-path'])[1]")
        is_liked = await self.check_first_post()
        if is_liked:
            for i in range(1, 5):
                NEXT_LIKE_WRAPPER = self.page.locator(f"(//path[@id='heart'])[{i}]/ancestor::div[contains(@class, 'orangehrm-like-animation')]")
                count = await NEXT_LIKE_WRAPPER.count()
                if count > 0:
                    NEXT_LIKE = self.page.locator(f"(//*[@class='orangehrm-heart-icon-path'])[{i}]")
                    await self.expect(NEXT_LIKE).to_be_visible()
                    await NEXT_LIKE.scroll_into_view_if_needed()
                    await NEXT_LIKE.click()
                    break
        else:
            await LIKE_BUTTON.click()