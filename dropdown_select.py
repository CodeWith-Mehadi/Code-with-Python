from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "dropdown")

dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Drop Down Item 4")

print("'Drop Down Item 4' successfully select.")

time.sleep(3)
driver.quit()
