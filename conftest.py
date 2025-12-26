
import pytest_asyncio
from playwright.async_api import async_playwright

@pytest_asyncio.fixture(scope="function", autouse=True)
async def page(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled"
            ]
        )
        page = await browser.new_page()
        request.cls.page = page
        yield page
        await browser.close()