import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
driver = webdriver.Chrome()

URL = "https://www.clinique.com/makeup-clinique?&utm_id=go_cmp-20493563026_adg-158450696131_ad-671210073586_kwd-10615601_dev-c_ext-_prd-_mca-_sig-Cj0KCQiAwvKtBhDrARIsAJj-kTgPvHe-JrfC9_jw_O76QoCShPC9QD_a0lHt_CJVu-2dEVoE9efnmQsaAmffEALw_wcB&utm_source=google&gad_source=1&gclid=Cj0KCQiAwvKtBhDrARIsAJj-kTgPvHe-JrfC9_jw_O76QoCShPC9QD_a0lHt_CJVu-2dEVoE9efnmQsaAmffEALw_wcB&gclsrc=aw.ds"
driver.get(URL)

# product_link = driver.find_element(By.XPATH,'(//div[contains(@id,"phx-F7AbJCdbZDyFd5IC-5-0")])/div/div/a').get_attribute('href')
# time.sleep(3)
# driver.get(product_link)
#
# time.sleep(3)

time.sleep(3)
product_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[contains(@id,"phx-F7AbJCdbZDyFd5IC-5-0")])/div/div/a'))
)
product_link = product_link.get_attribute('href')
time.sleep(3)

driver.get(product_link)

driver.quit()