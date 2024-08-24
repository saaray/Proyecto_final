from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura Selenium
driver = webdriver.Chrome()
driver.get("https://mydramalist.com/")

try:
    # Encuentra el contenedor de artículos
    articles_list = driver.find_element(By.ID, "articles-list")

    # Extrae los títulos de los artículos dentro del contenedor
    titles = articles_list.find_elements(By.XPATH, ".//h2/a")
    
    for title in titles:
        print(title.text)

except Exception as e:
    print(f"Error extracting data: {e}")

finally:
    driver.quit()

