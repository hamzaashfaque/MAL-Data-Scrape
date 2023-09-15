from scraper_functions import get_card_links, get_entry_info
import pandas as pd

LINK = "https://myanimelist.net/topanime.php?limit="
card_links = get_card_links(LINK)
df = pd.DataFrame(card_links, columns=['card_links'])
df.to_csv("data/card_links.csv", index_label="id")

anime_list = get_entry_info(card_links=card_links)
df = pd.DataFrame(anime_list, columns=[
    "cardlink",
    "title",
    "english_title",
    "show_type",
    "episodes",
    "status",
    "started_airing",
    "ended_airing",
    "first_premiered",
    "broadcast",
    "producers",
    "licensors",
    "studios",
    "source",
    "genre",
    "theme",
    "demographic",
    "duration",
    "age_rating",
    "score",
    "ratings_count",
    "rank",
    "popularity",
    "members",
    "users_favorited"
])
df.to_csv("data/anime_list.csv", index_label="id")