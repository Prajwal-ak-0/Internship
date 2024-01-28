import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

URL = "https://www.lookfantastic.com/health-beauty/hair/view-all-haircare.list"
driver.get(URL)
driver.maximize_window()

expected_product_count = 45

scroll_height = driver.execute_script("return document.body.scrollHeight")
scroll_duration = 20
scroll_steps = 100  # You can adjust this value based on your preference
scroll_distance = scroll_height / scroll_steps

accept_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
)
accept_button.click()

close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"epopup-close-button"))
)
close_button.click()

for _ in range(scroll_steps):
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    time.sleep(scroll_duration / scroll_steps)
try:
    products = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))

    if len(products) == expected_product_count:
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

        df = pd.DataFrame({"name": name, "price": price, "link": link})

        df.to_csv("lookfantastic.csv", index=False)
    else:
        print(f"Expected {expected_product_count} products, but found {len(products)} products.")
except Exception as e:
    import traceback
    traceback.print_exc()

driver.quit()