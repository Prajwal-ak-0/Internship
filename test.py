import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

URL = "https://www.lookfantastic.com/health-beauty/face/skincare-products.list"
driver.get(URL)

wait = WebDriverWait(driver, 10)

def expand_accordion():
    accordion_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "product-description-heading-lg-7"))
    )

    ActionChains(driver).move_to_element(accordion_button).perform()

    accordion_button.click()

def get_ingredients(URL):
    driver.get(URL)
    time.sleep(2)

    expand_accordion()
    time.sleep(2)

    try:
        ingredients_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="product-description-content-lg-7"]/div/div/p'))
        )
        ingredients_text = ingredients_element.text
    except TimeoutException:
        # If ingredients are not found, set an empty string
        ingredients_text = ''

    driver.back()

    print(ingredients_text)
    return ingredients_text

try:
    products = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))

    ingredients = []

    for i in range(len(products)):
        try:
            products = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, '//li[contains(@class,"productListProducts_product")]')))
            product = products[i]

            link_element = WebDriverWait(product, 10).until(
                EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))

            ingredients_text = get_ingredients(link_element.get_attribute("href"))
            ingredients.append(ingredients_text)

            if not ingredients_text:
                print(f'Ingredients not found for product {i + 1}. Continuing with the next product.')

        except TimeoutException:
            print(f'Timeout waiting for the link for product {i + 1}. Continuing with the next product.')

except Exception as e:
    import traceback

    traceback.print_exc()
