import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\PythonProject\Python_Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency="USD"):
        # Open currency selector
        currency_button = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_button.click()

        # Wait and find the right currency option by visible text or a more precise selector
        currency_options = self.find_elements(By.CSS_SELECTOR, 'button[data-testid="selection-item"]')
        for option in currency_options:
            if currency in option.text:
                option.click()
                break

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element('name', 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        # Wait for the first autocomplete suggestion to appear and contain the desired place
        wait = WebDriverWait(self, 10)
        first_result = wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, 'autocomplete-result-0'),
                place_to_go)
        )

        first_result= self.find_element('id', 'autocomplete-result-0')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self):
        selection_element = self.find_element(By.CSS_SELECTOR, '*[data-testid="occupancy-config"]')
        selection_element.click()

        decrease_adults_element = self.find_element(By.CSS_SELECTOR, '*[class="de576f5064 b46cd7aad7 e26a59bb37 c295306d66 c7a901b0e7 aaf9b6e287 dc8366caa6"]')
        decrease_adults_element.click()

    def select_final_results(self):
        final_result = self.find_element(By.CSS_SELECTOR, '*[type="submit"]')
        final_result.click()


