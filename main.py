import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
driver = webdriver.Chrome()

URL = "https://www.lookfantastic.com/health-beauty/hair/view-all-haircare.list"
driver.get(URL)

page_count = 3
current_page = 1

wait = WebDriverWait(driver, 10)

def scroll_to_bottom():
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_duration = 20
    scroll_steps = 100  # You can adjust this value based on your preference
    scroll_distance = scroll_height / scroll_steps

    for _ in range(scroll_steps):
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(scroll_duration / scroll_steps)

def close_popup():
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    accept_button.click()

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "epopup-close-button"))
    )
    close_button.click()

def get_product_info():
    wait = WebDriverWait(driver, 10)

    try:
        products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))

        if len(products) == 45:
            name = []
            price = []
            link = []

            for product in products:
                name_element = WebDriverWait(product, 10).until(
                    EC.visibility_of_element_located((By.XPATH, './/h3[contains(@class,"productBlock_productName")]')))
                price_element = WebDriverWait(product, 10).until(
                    EC.visibility_of_element_located((By.XPATH, './/span[contains(@class,"productBlock_priceValue")]')))
                link_element = WebDriverWait(product, 10).until(
                    EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))

                name.append(name_element.text)
                price.append(price_element.text)
                link.append(link_element.get_attribute("href"))

            new_data = pd.DataFrame({"name": name, "price": price, "link": link})

            if os.path.isfile("lookfantastic.csv"):
                existing_data = pd.read_csv("lookfantastic.csv")
                df = pd.concat([existing_data, new_data])
            else:
                df = new_data

            df.to_csv("lookfantastic.csv", index=False)
        else:
            print(f"Expected 45 products, but found {len(products)} products.")
    except Exception as e:
        import traceback

        traceback.print_exc()

close_popup()

while current_page < page_count:
    scroll_to_bottom()
    get_product_info()
    time.sleep(10)
    container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"responsiveProductListPage_bottomPagination")]')))
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"paginationNavigationButtonNext")]')))
    driver.execute_script("arguments[0].click();", next_button)
    current_page += 1
    time.sleep(10)

driver.quit()