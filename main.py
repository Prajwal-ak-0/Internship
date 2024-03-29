# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import os
# driver = webdriver.Chrome()
#
# URL = "https://www.lookfantastic.com/health-beauty/hair/view-all-haircare.list"
# driver.get(URL)
#
# page_count = 3
# current_page = 1
#
# wait = WebDriverWait(driver, 10)
#
# def scroll_to_bottom():
#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#     scroll_duration = 20
#     scroll_steps = 100  # You can adjust this value based on your preference
#     scroll_distance = scroll_height / scroll_steps
#
#     for _ in range(scroll_steps):
#         driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
#         time.sleep(scroll_duration / scroll_steps)
#
# def close_popup():
#     accept_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
#     )
#     accept_button.click()
#
#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "epopup-close-button"))
#     )
#     close_button.click()
#
# def get_product_info():
#     wait = WebDriverWait(driver, 10)
#
#     try:
#         products = wait.until(
#             EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))
#
#         if len(products) == 45:
#             name = []
#             price = []
#             link = []
#
#             for product in products:
#                 name_element = WebDriverWait(product, 10).until(
#                     EC.visibility_of_element_located((By.XPATH, './/h3[contains(@class,"productBlock_productName")]')))
#                 price_element = WebDriverWait(product, 10).until(
#                     EC.visibility_of_element_located((By.XPATH, './/span[contains(@class,"productBlock_priceValue")]')))
#                 link_element = WebDriverWait(product, 10).until(
#                     EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))
#
#                 name.append(name_element.text)
#                 price.append(price_element.text)
#                 link.append(link_element.get_attribute("href"))
#
#             new_data = pd.DataFrame({"name": name, "price": price, "link": link})
#
#             if os.path.isfile("lookfantastic.csv"):
#                 existing_data = pd.read_csv("lookfantastic.csv")
#                 df = pd.concat([existing_data, new_data])
#             else:
#                 df = new_data
#
#             df.to_csv("lookfantastic.csv", index=False)
#         else:
#             print(f"Expected 45 products, but found {len(products)} products.")
#     except Exception as e:
#         import traceback
#
#         traceback.print_exc()
#
# close_popup()
#
# while current_page < page_count:
#     scroll_to_bottom()
#     get_product_info()
#     time.sleep(10)
#     container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"responsiveProductListPage_bottomPagination")]')))
#     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"paginationNavigationButtonNext")]')))
#     driver.execute_script("arguments[0].click();", next_button)
#     current_page += 1
#     time.sleep(10)
#
# driver.quit()
#
#
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains
# #
# # # Set up Chrome WebDriver
# # driver = webdriver.Chrome()
# #
# # # Navigate to the URL
# # URL = "https://www.lookfantastic.com/kerastase-elixir-ultime-l-original-elixir-ultime-bundle/13745479.html"
# # driver.get(URL)
# #
# # # Function to close popups
# # def close_popup():
# #     accept_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
# #     )
# #     accept_button.click()
# #
# #     close_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.ID, "epopup-close-button"))
# #     )
# #     close_button.click()
# #
# #     login_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"emailReengagement_close_button")]'))
# #     )
# #     login_button.click()
# #
# # # Function to expand accordion
# # def expand_accordion():
# #     accordion_button = WebDriverWait(driver, 20).until(
# #         EC.presence_of_element_located((By.ID, "product-description-heading-lg-7"))
# #     )
# #
# #     # Use ActionChains to move to the element and make it visible
# #     ActionChains(driver).move_to_element(accordion_button).perform()
# #
# #     # Click on the accordion button
# #     accordion_button.click()
# #
# # # Close popups
# # close_popup()
# # time.sleep(2)
# #
# # # Expand accordion to reveal ingredient content
# # expand_accordion()
# # time.sleep(2)  # Adjust this delay if needed
# #
# # # Extract ingredients
# # ingredients_element = WebDriverWait(driver, 20).until(
# #     EC.presence_of_element_located((By.XPATH, '//div[@id="product-description-content-lg-7"]/div/div/p'))
# # )
# # ingredients_text = ingredients_element.text
# #
# # # Print the ingredients
# # print("Ingredients:", ingredients_text)
# #
# # # Close the Chrome WebDriver
# # driver.quit()
#
#
#
#
#
#
#
#
#
# # import time
# # import pandas as pd
# # import os
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains
# #
# # def scroll_to_bottom():
# #     scroll_height = driver.execute_script("return document.body.scrollHeight")
# #     scroll_duration = 20
# #     scroll_steps = 100  # You can adjust this value based on your preference
# #     scroll_distance = scroll_height / scroll_steps
# #
# #     for _ in range(scroll_steps):
# #         driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
# #         time.sleep(scroll_duration / scroll_steps)
# #
# # def close_popup():
# #     accept_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
# #     )
# #     accept_button.click()
# #
# #     try:
# #         close_button = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.ID, "epopup-close-button"))
# #         )
# #         close_button.click()
# #     except:
# #         pass
# #
# # def get_product_info(product):
# #     name_element = WebDriverWait(product, 10).until(
# #         EC.visibility_of_element_located((By.XPATH, './/h3[contains(@class,"productBlock_productName")]')))
# #     price_element = WebDriverWait(product, 10).until(
# #         EC.visibility_of_element_located((By.XPATH, './/span[contains(@class,"productBlock_priceValue")]')))
# #     link_element = WebDriverWait(product, 10).until(
# #         EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,"productBlock_link")]')))
# #
# #     product_info = {
# #         "name": name_element.text,
# #         "price": price_element.text,
# #         "link": link_element.get_attribute("href")
# #     }
# #
# #     return product_info
# #
# # def expand_accordion():
# #     try:
# #         accordion_button = WebDriverWait(driver, 20).until(
# #             EC.presence_of_element_located((By.ID, "product-description-heading-lg-7"))
# #         )
# #
# #         # Use ActionChains to move to the element and make it visible
# #         ActionChains(driver).move_to_element(accordion_button).perform()
# #
# #         # Click on the accordion button
# #         accordion_button.click()
# #     except:
# #         pass
# #
# # def get_ingredients():
# #     try:
# #         ingredients_element = WebDriverWait(driver, 20).until(
# #             EC.presence_of_element_located((By.XPATH, '//div[@id="product-description-content-lg-7"]/div/div/p'))
# #         )
# #         ingredients_text = ingredients_element.text
# #
# #         return ingredients_text
# #     except:
# #         return "Ingredients not found"
# #
# # # Set up Chrome WebDriver
# # driver = webdriver.Chrome()
# #
# # # Navigate to the URL
# # URL_list = "https://www.lookfantastic.com/health-beauty/hair/view-all-haircare.list"
# # driver.get(URL_list)
# #
# # page_count = 3
# # current_page = 1
# #
# # wait = WebDriverWait(driver, 10)
# #
# # # Close popups
# # close_popup()
# #
# # while current_page < page_count:
# #     scroll_to_bottom()
# #
# #     # Get product information
# #     products = wait.until(
# #         EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListProducts_product")]')))
# #
# #     for product in products:
# #         product_info = get_product_info(product)
# #
# #         # Navigate to the product page
# #         driver.get(product_info["link"])
# #
# #         # Close popups
# #         close_popup()
# #         time.sleep(2)
# #
# #         # Expand accordion to reveal ingredient content
# #         expand_accordion()
# #         time.sleep(2)  # Adjust this delay if needed
# #
# #         # Get ingredients
# #         ingredients = get_ingredients()
# #
# #         # Print the information
# #         print("Name:", product_info["name"])
# #         print("Price:", product_info["price"])
# #         print("Ingredients:", ingredients)
# #         print("=" * 50)
# #
# #         # Store data in a DataFrame
# #         df = pd.DataFrame({
# #             "Name": [product_info["name"]],
# #             "Price": [product_info["price"]],
# #             "Ingredients": [ingredients],
# #             "Link": [product_info["link"]]
# #         })
# #
# #         # Write to CSV
# #         if os.path.isfile("lookfantastic.csv"):
# #             existing_data = pd.read_csv("lookfantastic.csv")
# #             df = pd.concat([existing_data, df], ignore_index=True)
# #         df.to_csv("lookfantastic.csv", index=False)
# #
# #         # Go back to the previous page
# #         driver.back()
# #         time.sleep(2)
# #
# #     container = wait.until(
# #         EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"responsiveProductListPage_bottomPagination")]')))
# #     next_button = wait.until(
# #         EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"paginationNavigationButtonNext")]')))
# #     driver.execute_script("arguments[0].click();", next_button)
# #     current_page += 1
# #     time.sleep(10)
# #
# # # Close the Chrome WebDriver
# # driver.quit()



#         'pro1.csv': 'Foundation Makeup',
#         'pro2.csv': 'Concealer',
#         'pro3.csv': 'Colour Correctors',
#         'pro4.csv': 'Blushers',
#         'pro5.csv': 'Bronzers',
#         'pro6.csv': 'highlighters-shimmers',
#         'pro7.csv': 'Makeup Palette',
#         'pro8.csv': 'Face Powders',
#         'pro9.csv': 'Tinted Moisturisers',
#         'pro10.csv': 'Primers',
#         'pro11.csv': 'Contouring',
#         'pro12.csv': 'Setting Sprays',
#         'pro13.csv': 'BB Creams',
#         'pro14.csv': 'Eye Shadows',
#         'pro15.csv': 'Mascara',
#         'pro16.csv': 'Eyeliner',
#         'pro17.csv': 'Primer Enhancer',
#         'pro18.csv': 'False Eyelashes',
#         'pro19.csv': 'Lash & Brow Enhancers',
#         'pro20.csv': 'Brows',
#         'pro21.csv': 'False Eyelashes Glue'