from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:3000/user/1/edit")

driver.find_element_by_name("name").clear()
driver.find_element_by_name("name").send_keys("test2")

driver.find_element_by_name("update").click()

assert "test2" in driver.page_source

driver.quit()
