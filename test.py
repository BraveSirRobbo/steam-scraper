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
		      }

class ScraperTests(unittest.TestCase):
    def test_example_page(self):

	with open("examples/Age of Wonders III on Steam.html", "r") as f:
		page_text = "".join(f.readlines())

        self.assertEqual(scrapePage(page_text),
		{ "title" : "Age of Wonders III"
		, "overall_rating" : "Very Positive"
		, "num_reviews" : "3504"
		})

if __name__ =="__main__":
	unittest.main()
