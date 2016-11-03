import unittest

def scrapePage(html):
	return {}

class ScraperTests(unittest.TestCase):
    def test_example_page(self):
        self.assertEqual(scrapePage(""),
		{ "title" : "Age of Wonders III"
		, "overall_rating" : "Very Positive"
		, "num_reviews" : "3505"
		})

if __name__ =="__main__":
	unittest.main()
