import allure
from playwright.sync_api import Page
import config
from allure_commons.types import AttachmentType

import allure
from playwright.sync_api import Page
import config
from allure_commons.types import AttachmentType

class IndexPage:
    def __init__(self, page: Page):
        self.page = page  # Сохраняем ссылку на экземпляр Page

    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    fld_login = '//*[@id="email"]'
    fld_pass = '//*[@id="password"]'
    btn_login = 'section > a > button'
    btn_sign_in = '//*[@type="submit"]'

    @allure.step("Открыть главную страницу")
    def open_index_page(self) -> None:
        self.page.goto(config.url.HOST)

    @allure.step("Получить текст с кнопки поиска Google")
    def get_text_from_google_search_button(self):
        return self.page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')

    @allure.step("Нажать кнопку входа")
    def get_login_button(self):
        return self.page.locator(self.btn_login).click()

    @allure.step("Войти с помощью электронной почты и пароля")
    def get_login(self):
        self.page.locator(self.fld_login).click()
        self.page.locator(self.fld_login).fill('Guest@mail.com')
        self.page.locator(self.fld_pass).click()
        self.page.locator(self.fld_pass).fill('Test1234.')
        self.page.locator(self.btn_sign_in).click()

    def screenshot(self) -> bytes:
        """Сделать скриншот текущей страницы."""
        return self.page.screenshot()

    def make_screenshot(self, screenshot_name):
        """Прикрепить скриншот к отчету Allure."""
        allure.attach(
            body=self.screenshot(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

















# import allure
# from playwright.sync_api import Page
# import config
# from allure_commons.types import AttachmentType
#
#
# class IndexPage():
#     _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
#     fld_login = '//*[@id="email"]'
#     fld_pass = '//*[@id="password"]'
#     btn_login = 'section > a > button'
#     btn_sign_in = '//*[@type="submit"]'
#
#     @allure.step
#     def open_index_page(self, page: Page) -> None:
#         page.goto(config.url.HOST)
#
#     @allure.step
#     def get_text_from_google_search_button(self, page: Page):
#         return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')
#
#     @allure.step
#     def get_login_button(self, page: Page):
#         return page.locator(self.btn_login).click()
#
#     @allure.step
#     def get_login(self, page: Page):
#         page.locator(self.fld_login).click()
#         page.locator(self.fld_login).fill('Guest@mail.com')
#         page.locator(self.fld_pass).click()
#         page.locator(self.fld_pass).fill('Test1234.')
#         page.locator(self.btn_sign_in).click()
#
#     def make_screenshot(self, screenshot_name):
#         allure.attach(
#             body=self.screenshot(),
#             name=screenshot_name,
#             attachment_type=AttachmentType.PNG
#         )
