from .basepage import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn_add_to_basket.click()

    def get_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return product_title.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'Button Add to basket NOT present'

    def should_be_product_tile_present(self):
        title_alertinner = self.browser.find_element_by_class_name('alertinner').text.strip()
        assert title_alertinner == f'{self.get_product_title()}, Good has been added to basket'

    def should_be_product_price_present(self):
        price_alertinner = self.browser.find_element_by_css_selector('.alertinner > p').text.strip()
        assert price_alertinner == f'Your basket total is now {self.get_product_price()}'
