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

# Initializing the Chrome driver
driver = webdriver.Chrome()

# URL of the target page
URL = "https://www.lookfantastic.com/health-beauty/dermatological-skincare/dull-skin.list"
driver.get(URL)

# WebDriverWait object for explicit waits
wait = WebDriverWait(driver, 10)

def expand_accordion():
    # Function to expand the accordion on the product page
    accordion_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "product-description-heading-lg-7"))
    )

    ActionChains(driver).move_to_element(accordion_button).perform()

    accordion_button.click()

def save_to_csv(data):
    # Function to save data to CSV
    csv_file_path = 'products_data.csv'

    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
    else:
        existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients'])

    updated_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)

    updated_df.to_csv(csv_file_path, index=False)
    print(f'Data successfully written to {csv_file_path}')

def get_ingredients(URL):
    # Function to get product details from a product page
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

try:
    # Wait for the products to be visible
    products = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))

    for i in range(len(products)):
        try:
            # Re-fetch products inside the loop to avoid StaleElementReferenceException
            products = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, '//li[contains(@class,"productListProducts_product")]')))
            product = products[i]

            link_element = WebDriverWait(product, 10).until(
                EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))

            # Get ingredients for the current product
            get_ingredients(link_element.get_attribute("href"))

        except TimeoutException:
            print(f'Timeout waiting for the link for product {i + 1}. Continuing with the next product.')
            driver.back()

except Exception as e:
    print(f'An error occurred: {e}')

finally:
    # Close the browser window
    driver.quit()
