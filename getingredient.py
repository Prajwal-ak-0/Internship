import time
import csv
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

def scroll_to_bottom():
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_duration = 20
    scroll_steps = 100  # You can adjust this value based on your preference
    scroll_distance = scroll_height / scroll_steps

    for _ in range(scroll_steps):
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(scroll_duration / scroll_steps)

def expand_accordion():
    accordion_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "product-description-heading-lg-7"))
    )

    ActionChains(driver).move_to_element(accordion_button).perform()

    accordion_button.click()

def save_to_csv(data):
    csv_file_path = 'products_dt.csv'

    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
    else:
        existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients'])

    updated_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)

    updated_df.to_csv(csv_file_path, index=False)
    print(f'Data successfully written to {csv_file_path}')

def get_ingredients(URL):
    driver.get(URL)
    time.sleep(2)

    expand_accordion()
    time.sleep(2)

    try:
        name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(@class,"productName_title")]'))
        )
        name_text = name.text
        price = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"productPrice_price")]'))
        )
        price_text = price.text
        ingredients_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="product-description-content-lg-7"]/div/div/p'))
        )
        ingredients_text = ingredients_element.text

        print(f'Name: {name_text}')
        print(f'Price: {price_text}')
        print(f'Ingredients: {ingredients_text}')

        data = {'Name': [name_text], 'Price': [price_text], 'Ingredients': [ingredients_text]}
        save_to_csv(data)

        driver.back()

    except TimeoutException:
        print(f'Timeout waiting for product details on {URL}. Skipping this product.')

def get_product_info():
    try:
        products = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))

        for i in range(len(products)):
            try:
                products = wait.until(
                    EC.visibility_of_all_elements_located(
                        (By.XPATH, '//li[contains(@class,"productListProducts_product")]')))
                product = products[i]

                link_element = WebDriverWait(product, 10).until(
                    EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))

                get_ingredients(link_element.get_attribute("href"))

            except TimeoutException:
                print(f'Timeout waiting for the link for product {i + 1}. Continuing with the next product.')
                driver.back()

    except Exception as e:
        print(f'An error occurred: {e}')


pages = 2

current_page = 1

while current_page <= pages:
    print(f"Scraping data from page {current_page}")
    get_product_info()
    time.sleep(10)

    container = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[contains(@class,"responsiveProductListPage_bottomPagination")]')))
    next_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"paginationNavigationButtonNext")]')))
    driver.execute_script("arguments[0].click();", next_button)

    current_page += 1
    time.sleep(10)

driver.quit()