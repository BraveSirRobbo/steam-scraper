import unittest
from bs4 import BeautifulSoup
import re

def justOne(ls):
  assert(len(ls) == 1)
  return ls[0]

def scrapePage(html_doc):
  soup = BeautifulSoup(html_doc, 'html.parser')

  ratings = [s.get_text() for s in soup.find_all("span",attrs={ "class": re.compile(r"game_review_summary .*")})]
  assert(len(ratings) != 1)
  reviewCounts = [x.attrs["content"] for x in soup.find_all("meta",attrs={"itemprop":"reviewCount"})]

  aList = [t.get_text() for t in soup.find_all("div",class_="game_area_details_specs")]

  def tagChecker(*things):
    for thing in things:
      if thing in aList:
        return True
    return False

  return  { "title":
              justOne(soup.find_all("div",class_="apphub_AppName")).get_text()
          , "overall_rating" :
              ratings[1] if len(ratings) > 0 else None
          , "num_reviews" :
              reviewCounts[0] if len(reviewCounts) > 0 else None
          , "release_year" :
              justOne(soup.find_all("span",class_="date")).get_text()[-4:]
          , "user_tags" :
              [x.get_text().strip() for x in justOne(soup.find_all("div",class_="glance_tags popular_tags")).find_all("a")]
          , "multiplayer" :
              tagChecker("Multi-player")
          , "co-op" :
              tagChecker("Co-op")
          , "local_multiplayer" :
              tagChecker("Shared/Split Screen")
          , "steam_cloud" :
              tagChecker("Steam Cloud")
          , "controller_supported" :
              tagChecker("Full controller support", "Partial Controller Support")
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
      self.assertKeyValue(res, "user_tags", ['Strategy', 'Turn-Based Strategy', 'Fantasy', 'RPG', '4X', 'Turn-Based', 'Multiplayer', 'Singleplayer', 'Tactical', 'Co-op', 'Adventure', 'Hex Grid', 'Great Soundtrack', 'Grand Strategy', 'Classic', 'Atmospheric', 'Moddable', 'Action', 'Female Protagonist', 'Indie']) #from class "glance_tags popular_tags"
      self.assertKeyValue(res, "multiplayer", True) #"Multi-Player" from class "game_area_details_specs"
      self.assertKeyValue(res, "co-op", True) #"Co-op" from class "game_area_details_specs"
      self.assertKeyValue(res, "local_multiplayer", True) #"Shared/Split Screen" from class "game_area_details_specs"
      self.assertKeyValue(res, "steam_cloud", True) #Cross-Platform Multiplayer from class "game_area_details_specs"
      self.assertKeyValue(res, "controller_supported", False) #Full OR Partial Controller Support from class "game_area_details_specs"


    def test_no_recent_reviews(self):

      with open("examples/No Recent Reviews.html") as f:
        page_text = "".join(f.readlines())

      res = scrapePage(page_text)

      self.assertKeyValue(res,"overall_rating", "Very Positive")


    def test_no_reviews(self):

      with open("examples/No Reviews.html") as f:
        page_text = "".join(f.readlines())

      res = scrapePage(page_text)

      self.assertKeyValue(res,"overall_rating", None)
      self.assertKeyValue(res,"num_reviews", None)




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
