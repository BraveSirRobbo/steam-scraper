import unittest

def scrapePage(html):
	return {}

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
