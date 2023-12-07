from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:3000/addnewuser")

driver.find_element_by_name("name").send_keys("test")
driver.find_element_by_name("email").send_keys("test@email.com")

driver.find_element_by_name("add").click()

assert "test" in driver.page_source

driver.quit()
