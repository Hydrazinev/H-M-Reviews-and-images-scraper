from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')


chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")



chrome_driver_path = r"C:\Users\vaidi\Downloads\chromedriver.exe"  


driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.implicitly_wait(10)  

# List of URLs to scrape
urls = [
    'https://www2.hm.com/en_in/productpage.1034065080.html'
    # Add more URLs here
]


def scrape_reviews(url, output_file):
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    print("Page title: ", driver.title)
    
    try:
        review_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'd1a171')))
        print("Review button HTML: ", review_button.get_attribute('outerHTML'))
        driver.execute_script("arguments[0].scrollIntoView(true);", review_button)
        review_button.click()
        print("Review button clicked successfully.")
    except Exception as e:
        print("Error finding or clicking review button:", e)

    time.sleep(5)  

    def click_show_more_in_reviews():
        while True:
            for i in range(40):
            
                show_more_buttons = driver.find_elements(By.CSS_SELECTOR, "button")
                for c in show_more_buttons:
                    if c.get_attribute('class') in ['CTA-module--action__1qN9s CTA-module--large__uJ3Wz CTA-module--primary__2eqCh CTA-module--fullWidth__1WXt6 CTA-module--inverted__3rN3y']:
                        c.click()
                        for m in show_more_buttons:
                            if m.get_attribute('class') in ['CTA-module--action__1qN9s CTA-module--medium__1uoRl CTA-module--reset__1G6AO CTA-module--inline__1rDLl']:
                                m.click()
                        time.sleep(3)  
                        print("--> Button clicked <--")
                
            if not show_more_buttons:
                break
            break

    click_show_more_in_reviews()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    review_containers = soup.find_all("p", class_="BodyText-module--general__jkobl Review-module--reviewContent__2xeBs")
    reviews = [paragraph.get_text().strip() for paragraph in review_containers]

    if reviews:
        print("Reviews found:")
        for review in reviews:
            print(review)
    else:
        print("No reviews found.")

    total_reviews = len(reviews)
    print(f"Total reviews scraped: {total_reviews}")

    os.makedirs('scraped_reviews', exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for review in reviews:
            f.write(review + '\n\n')

    print(f"Reviews have been saved to {output_file}")


def calculate_time_taken(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time.total_seconds() / 60
    print(f"Total time taken: {elapsed_minutes:.2f} minutes")


start_time = datetime.datetime.now()


for i, url in enumerate(urls):
    output_file = f'scraped_reviews/reviews_184.txt'
    scrape_reviews(url, output_file)

end_time = datetime.datetime.now()
calculate_time_taken(start_time, end_time)

driver.quit()
