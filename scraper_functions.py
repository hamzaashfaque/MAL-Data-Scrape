from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from tqdm import tqdm


def get_card_links(link):
    driver = webdriver.Chrome()
    card_links = []
    end_page = False
    limit = 0
    while(end_page is False):
        driver.get(f"{link}{limit}")
        driver.implicitly_wait(5)
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
    print("Links Gathered Successfully!")
    return card_links



def get_entry_info(card_links):
    # Returns a list of dictionaries containing text data about anime
    anime_list = []
    driver = webdriver.Chrome()

    for cardlink in tqdm(card_links):
        driver.get(cardlink)
        driver.implicitly_wait(3)

        # Finds tags and store their contents into a dictionary
        title = driver.find_element(
            By.CSS_SELECTOR,
            ".title-name > strong"
            ).get_attribute("innerHTML")
        try:
            english_title = driver.find_element(
                By.CLASS_NAME,
                "title-english"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            english_title = title

        try:
            show_type = driver.find_element(
                By.XPATH, 
                "//*[@class='borderClass']//span[contains(text(), 'Type')]/parent::*/a"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            show_type = "None"

        try:
            episodes = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Episodes')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            episodes = "None"
        
        try:
            status = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Status')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            status = "None"
        
        try:
            aired = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Aired')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip().split(' to ')
            started_airing = aired[0]
            try:
                ended_airing = aired[1]
            except IndexError:
                ended_airing = aired[0]
        except exceptions.NoSuchElementException:
            aired = "None"

        try:
            first_premiered = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Premiered')]/parent::*/a"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            first_premiered = "None"
        
        try:
            broadcast = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Broadcast')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            broadcast = "None"

        try:
            producers = []
            links = driver.find_elements(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Producers')]/parent::*/a"
                )
            for link in links:
                link_string = link.get_attribute("innerHTML")
                if link_string != "add some":
                    producers.append(link_string)
                else:
                    producers = "None Found"
        except exceptions.NoSuchElementException:
            producers = "None"

        try:
            licensors = []
            links = driver.find_elements(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Licensors')]/parent::*/a"
                )
            for link in links:
                link_string = link.get_attribute("innerHTML")
                if link_string != "add some":
                    licensors.append(link_string)
                else:
                    licensors = "None Found"
        except exceptions.NoSuchElementException:
            licensors = "None"

        try:
            studios = []
            links = driver.find_elements(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Studios')]/parent::*/a"
                )
            for link in links:
                link_string = link.get_attribute("innerHTML")
                if link_string != "add some":
                    studios.append(link_string)
                else:
                    studios = "None Found"
        except exceptions.NoSuchElementException:
            studios = "None"

        try:
            source = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Source')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            source = "None"
        
        try:
            genre = []
            links = driver.find_elements(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Genre')]/parent::*/a"
                )
            for link in links:
                link_string = link.get_attribute("innerHTML")
                if link_string != "add some":
                    genre.append(link_string)
                else:
                    genre = "Unknown"
        except exceptions.NoSuchElementException:
            genre = "None"
        
        try:
            theme = []
            links = driver.find_elements(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Theme')]/parent::*/a"
                )
            for link in links:
                link_string = link.get_attribute("innerHTML")
                if link_string != "add some":
                    theme.append(link_string)
                else:
                    theme = "Unknown"
            if len(theme) == 0:
                theme = "None"
        except exceptions.NoSuchElementException:
            theme = "None"
        
        try:
            demographic = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Demographic')]/parent::*/a"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            demographic = "None"
        
        try:
            duration = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Duration')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            duration = "Unknown"

        try:
            age_rating = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Duration')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            age_rating = "Unknown"

        try:
            score = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Score')]/parent::*/span[@itemprop='ratingValue']"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            score = "N/A"
        
        try:
            ratings_count = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Score')]/parent::*/span[@itemprop='ratingCount']"
                ).get_attribute("innerHTML")
        except exceptions.NoSuchElementException:
            ratings_count = "N/A"
        
        try:
            rank = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Ranked')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
            rank = rank[:rank.index('<sup>')]
        except exceptions.NoSuchElementException:
            rank = "N/A"
        
        try:
            popularity = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Popularity')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            popularity = "N/A"
        
        try:
            members = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Members')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            members = "N/A"
        
        try:
            users_favorited = driver.find_element(
                By.XPATH,
                "//*[@class='borderClass']//span[contains(text(), 'Favorites')]/parent::*"
                ).get_attribute("innerHTML").splitlines()[2].lstrip()
        except exceptions.NoSuchElementException:
            users_favorited = "N/A"

        entry_list = [
            cardlink,
            title,
            english_title,
            show_type,
            episodes,
            status,
            started_airing,
            ended_airing,
            first_premiered,
            broadcast,
            producers,
            licensors,
            studios,
            source,
            genre,
            theme,
            demographic,
            duration,
            age_rating,
            score,
            ratings_count,
            rank,
            popularity,
            members,
            users_favorited
        ]
        anime_list.append(entry_list)

    return anime_list