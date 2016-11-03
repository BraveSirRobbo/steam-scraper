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
		})

if __name__ =="__main__":
	unittest.main()
