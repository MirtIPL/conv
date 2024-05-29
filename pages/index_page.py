import time

import allure
from playwright.sync_api import Page
import config
from allure_commons.types import AttachmentType
import logging

class IndexPage():
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    fld_login = '//*[@id="email"]'
    fld_pass = '//*[@id="password"]'
    btn_login = 'section > a > button'
    btn_sign_in = '//*[@type="submit"]'
    error_text = '//*[@id="email-helper-text"]'
    error_text_AUTH = '//*[@class="MuiFormHelperText-root css-4fig25"]'

    @allure.step
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.HOST)

    @allure.step
    def get_text_from_google_search_button(self, page: Page):
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')

    @allure.step
    def get_login_button(self, page: Page):
        return page.locator(self.btn_login).click()

    @allure.step
    def get_login_pass(self, page: Page):
        page.locator(self.fld_login).click()
        page.locator(self.fld_login).fill('Guest@mail.com')
        page.locator(self.fld_pass).click()
        page.locator(self.fld_pass).fill('Test1234.')
        page.locator(self.btn_sign_in).click()


    @allure.step
    def get_login_fail(self, page: Page):
        page.locator(self.fld_login).click()
        page.locator(self.fld_login).fill('Guest@mail')
        page.locator(self.fld_pass).click()
        page.locator(self.fld_pass).fill('Test1234.')
        page.locator(self.btn_sign_in).click()
        error_text = page.locator(self.error_text).get_attribute('textContent')
        print(error_text)
        assert error_text == error_text


    @allure.step
    def get_login_fail_auth(self, page: Page):
        page.locator(self.fld_login).click()
        page.locator(self.fld_login).fill('Guest@mail.com')
        page.locator(self.fld_pass).click()
        page.locator(self.fld_pass).fill('Test1234')
        page.locator(self.btn_sign_in).click()
        time.sleep(5)
        assert page.locator(self.error_text_AUTH).is_visible()



    @allure.step('Снимок экрана')
    def make_screenshot(self, page, comment):
        allure.attach(page.screenshot(), comment, allure.attachment_type.PNG)

