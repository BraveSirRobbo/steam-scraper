import unittest
from bs4 import BeautifulSoup
import re

def justOne(ls):
  assert(len(ls) == 1)
  return ls[0]

def scrapePage(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')

	return  { "title":
              justOne(soup.find_all("div",class_="apphub_AppName")).get_text()
		      , "overall_rating" :
                (soup.find_all("span",attrs=
                { "class": re.compile(r"game_review_summary .*")})[1]).get_text()
		      , "num_reviews" :
            justOne(soup.find_all("meta",attrs={"itemprop":"reviewCount"})).attrs["content"]
          , "release_year" : ""
          , "user_tags" : ""
          , "Multiplayer" : ""
          , "Co-op" : ""
          , "local_multiplayer" : ""
          , "online_multiplayer" : ""
          , "steam_cloud" : ""
          , "controller_supported" : ""
		      }


class ScraperTests(unittest.TestCase):
    def assertKeyValue(self, d, key, value):
      self.assertIn(key, d)
      self.assertEqual(d[key], value)

    def test_example_page(self):

      with open("examples/Age of Wonders III on Steam.html", "r") as f:
        page_text = "".join(f.readlines())

      res = scrapePage(page_text)

      self.assertKeyValue(res, "title", "Age of Wonders III")

      self.assertKeyValue(res, "overall_rating", "Very Positive")
      self.assertKeyValue(res, "num_reviews", "3504")
      self.assertKeyValue(res, "release_year","2014") #from class "release_date"
      self.assertKeyValue(res, "user_tags", "Strategy, Turn-Based Strategy, Fantasy, RPG") #from class "glance_tags popular_tags"
      self.assertKeyValue(res, "Multiplayer", "True") #"Multi-Player" from class "game_area_details_specs"
      self.assertKeyValue(res, "Co-op", "True") #"Co-op" from class "game_area_details_specs"
      self.assertKeyValue(res, "local_multiplayer", "True") #"Shared/Split Screen" from class "game_area_details_specs"
      self.assertKeyValue(res, "online_multiplayer", "True") #from class "game_area_details_specs"
      self.assertKeyValue(res, "steam_cloud", "True") #Cross-Platform Multiplayer from class "game_area_details_specs"
      self.assertKeyValue(res, "controller_supported", "False") #Full OR Partial Controller Support from class "game_area_details_specs"

# TODO: Real implementation
def filterGames(ls,q):
  return [ls[0]]

# TODO: This is just a silly example
class FilterTests(unittest.TestCase):
  def test_basic_filter(self):

    examples = [ {"title" : "blah", "overall_rating" : "Very Positive"}
               , {"title" : "bad", "overall_rating" : "Very Negative"} ]

    # TODO: Will - Do you have ideas about the form of the query input to the filter
    q = "overall_rating > Ok"

    self.assertEqual(filterGames(examples, q),
                      [ {"title" : "blah", "overall_rating" : "Very Positive"} ])


if __name__ =="__main__":
	unittest.main()
