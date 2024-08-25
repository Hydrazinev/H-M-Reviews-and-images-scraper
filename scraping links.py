from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver with the specified path to ChromeDriver
driver = webdriver.Chrome(executable_path=r"C:\Users\vaidi\Downloads\chromedriver.exe")

# Open the webpage
url = 'https://www2.hm.com/en_in/men/shop-by-product/tshirts-tank-tops.html'
driver.get(url)

# Scroll and click "Load more products" until all products are loaded
while True:
    try:
        load_more_button = driver.find_element(By.ID, 'button js-load-more')  # Change to the actual ID of the button
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        load_more_button.click()
        time.sleep(2)  # Wait for new products to load
    except:
        break  # Exit the loop if there are no more "Load more products" buttons

# Get page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract product links and store them in a list
product_links = []
for a in soup.find_all('a', class_='link'):
    link = a['href']
    if 'productpage' in link:
        full_link = f'https://www2.hm.com{link}'
        product_links.append(full_link)

# Print all product links
print(product_links)
