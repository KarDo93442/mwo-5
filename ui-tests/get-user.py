from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:3000/user/1")

assert "test" in driver.page_source
assert "test@email.com" in driver.page_source

driver.quit()
