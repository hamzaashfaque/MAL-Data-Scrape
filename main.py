from scraper_functions import get_card_links, get_anime_info
import pandas as pd

# LINK = "https://myanimelist.net/topanime.php?limit="
# card_links = get_card_links(LINK)
# df = pd.DataFrame(card_links, columns=['card_links'])
# df.to_csv("data/card_links.csv")

test_links = ["https://myanimelist.net/anime/2921/Ashita_no_Joe_2",
              "https://myanimelist.net/anime/457/Mushishi",
              "https://myanimelist.net/anime/33352/Violet_Evergarden",
              "https://myanimelist.net/anime/33050/Fate_stay_night_Movie__Heavens_Feel_-_III_Spring_Song"]

get_anime_info(test_links)