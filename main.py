from scraper_functions import get_card_links
import pandas as pd

LINK = "https://myanimelist.net/topanime.php?limit="
card_links = get_card_links(LINK)

df = pd.DataFrame(card_links, columns=['card_links'])
df.to_csv("data/card_links.csv")