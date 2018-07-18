import sys

from selenium import webdriver
import unittest 

import utils



class full_capturing(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):

        url = "https://www.thomascook.com/search?resortCode=any&goingTo=Any%20destination&depAirport=0&sbDepAirport=0&origin=Any%20Airport&departureDate=20180701,20180731&flexible=true&when=20180701&duration=7&occupation=2&brand=1&brand=8&brand=12&start=0&end=9&sort=recommendation_asc&abTest=1#intcmp=froghp_Lazy_block_1_text_july"
        self.driver.get(url)
        utils.fullpage_screenshot(self.driver, "test.png")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
