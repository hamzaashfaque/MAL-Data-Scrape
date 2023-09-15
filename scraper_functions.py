from selenium import webdriver
from selenium.webdriver.common.by import By


def get_card_links(link):
    driver = webdriver.Chrome
    card_links = []
    end_page = False
    limit = 0
    while(end_page is False):
        driver.get(f"{link}{limit}")
        print(f"Gathering anime titles {limit} to {limit+50}")
        header = driver.find_element(By.CLASS_NAME, "h1").get_attribute("innerHTML")
        if header == "404 Not Found":
            end_page = True
            continue
        a_tags = driver.find_elements(By.CSS_SELECTOR, ".ranking-list > .title > a")
        for tag in a_tags:
            href = tag.get_attribute("href")
            card_links.append(href)
        limit += 50
    return card_links



#def get_anime_info(card_links):