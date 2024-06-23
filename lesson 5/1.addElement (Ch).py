from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
#Открыть страницу
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    
# Локатор для кнопки "Add Element"
add_button_locator = "button[onclick='addElement()']"
    
# Локатор для кнопок "Delete"
delete_button_locator = "div#elements > button[onclick='deleteElement()']"
    
# Найти кнопку "Add Element" и кликнуть на нее 5 раз
add_button = driver.find_element(By.CSS_SELECTOR, add_button_locator)
for _ in range(5):
    add_button.click()
    
    # Собрать все кнопки "Delete"
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_button_locator)
    
# Вывести на экран размер списка кнопок "Delete"
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

driver.quit()