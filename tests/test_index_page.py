import time

import allure
import pytest
import pages


@pytest.mark.test_login
@allure.title('Набор тестов для авторизации в системе')
@allure.epic('Набор тестов для авторизации в ')

class TestFooter:

    # def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
    #     pages.index_page.open_index_page(page)
    #     actual_result = pages.index_page.get_text_from_google_search_button(page)
    #     assert actual_result == 'Поиск в Google', 'Google Search button text is not correct'
    # @pytest.mark.test_login
    # @allure.description('Авторизация с валидными данными')
    # def test_user_should_be_able_to_open_popup_select_subscription_plan3(self, page):
    #     pages.index_page.open_index_page(page)
    #     time.sleep(5)
    #
    #     pages.index_page.get_login_button(page)
    #     time.sleep(5)
    #     pages.index_page.get_login(page)
    #
    #     # assert actual_result == 'Поиск в Google', 'Google Search button text is not correct'
    #     time.sleep(5)
    #
    # @pytest.mark.test_login
    # @allure.description('Авторизация с невалидным паролем')
    # def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
    #     pages.index_page.open_index_page(page)
    #     time.sleep(5)
    #
    #     pages.index_page.get_login_button(page)
    #     time.sleep(5)
    #     pages.index_page.get_login(page)
    #
    #     # assert actual_result == 'Поиск в Google', 'Google Search button text is not correct'
    #     time.sleep(5)
    #
    # @pytest.mark.test_login
    # @allure.description('Авторизация с невалидной почтой')
    # def test_user_should_be_able_to_open_popup_select_subscription_plan2(self, page):
    #     pages.index_page.open_index_page(page)
    #     time.sleep(5)
    #
    #     pages.index_page.get_login_button(page)
    #     time.sleep(5)
    #     pages.index_page.get_login(page)
    #
    #     # assert actual_result == 'Поиск в Google', 'Google Search button text is not correct'
    #     time.sleep(5)

    @pytest.mark.test_login
    @allure.description('Востановление пароля')
    def test_user_should_be_able_to_open_popup_select_subscription_plan1(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.get_login_button(page)
        pages.index_page.get_login(page)
        #pages.index_page.make_screenshot("тест")
        pages.index_page.make_screenshot("example_screenshot.png")

        # assert actual_result == 'Поиск в Google', 'Google Search button text is not correct'
        time.sleep(5)