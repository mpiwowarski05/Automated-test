from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())


# driver = webdriver.Firefox(executable_path=r"D:\Testy Automatyczne\tutorial_selenium\drivers\geckodriver.exe")
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Dubai']").click()
# driver.find_element_by_name('checkin').send_keys("01/04/2020")
# driver.find_element_by_name('checkout').send_keys("30/04/2020")
driver.find_element_by_name('checkin').click()
driver.find_element_by_xpath("//td[@class='day ' and text()='2']").click()
# driver.find_element_by_name('checkout').click()
elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='15']")
for element in elementy: #iteracja po liście i wybór odpowiedniej daty
    if element.is_displayed():
        element.click()
        break

# driver.find_element_by_xpath("//td[@class='day ' and text()='15']").click()
driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys('4')
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys('4')
driver.find_element_by_xpath("//button[text()=' Search']").click()
# //h4[contains(@class, 'list_title')]//b
hotels = driver.find_elements_by_xpath("//h4[contains(@class, 'list_title')]//b") #wszystkie elementy listy
hotel_names =[hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
prices = driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
price_values =[price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Cena to: " + price)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

assert price_values[0] =='$22'
assert price_values[1] =='$50'
assert price_values[2] =='$80'
assert price_values[3] =='$150'

driver.quit()




