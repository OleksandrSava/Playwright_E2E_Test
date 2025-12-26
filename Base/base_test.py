
import pytest
from Config.data import Data
from Pages.dashboard_page import DashboardPage
from Pages.login_page import LoginPage
from Pages.buzz_page import BuzzPage


class BaseTest:

    data : Data

    login_page: LoginPage
    buzz_page: BuzzPage
    dashboard_page: DashboardPage


    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page
        request.cls.data = Data()

        request.cls.login_page = LoginPage(page)
        request.cls.buzz_page = BuzzPage(page)
        request.cls.dashboard_page = DashboardPage(page)

