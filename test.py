import unittest
from bs4 import BeautifulSoup

def scrapePage(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')

	titles = soup.find_all("div",class_="apphub_AppName")
	assert(len(titles) == 1)
	title = titles[0].get_text()


	return {"title": title, 
		"overall_rating" : "",
		"num_reviews" : ""
		}

class ScraperTests(unittest.TestCase):
    def test_example_page(self):

	with open("examples/Age of Wonders III on Steam.html", "r") as f:
		page_text = "".join(f.readlines())

        self.assertEqual(scrapePage(page_text),
		{ "title" : "Age of Wonders III"
		, "overall_rating" : "Very Positive"
		, "num_reviews" : "3505"
		, "release_year" : "2014" #from class "release_date"
		, "user_tags" : "Strategy, Turn-Based Strategy, Fantasy, RPG" #from class "glance_tags popular_tags"
		, "Multiplayer" : "True" #"Multi-Player" from class "game_area_details_specs"
		, "Co-op" : "True" #"Co-op" from class "game_area_details_specs"
		, "local_multiplayer" : "True" #"Shared/Split Screen" from class "game_area_details_specs"
		, "online_multiplayer" : "True" #from class "game_area_details_specs"
		, "steam_cloud" : "True" #Cross-Platform Multiplayer from class "game_area_details_specs"
		, "controller_supported" : "False" #Full OR Partial Controller Support from class "game_area_details_specs"
		})

if __name__ =="__main__":
	unittest.main()
