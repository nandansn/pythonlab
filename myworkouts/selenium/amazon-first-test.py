import unittest
from selenium import webdriver

class AmazonTitleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testTitle(self):
        self.driver.get("https://www.amazon.in/")
        print(self.driver.title)
        self.assertIn("Amazon.in",self.driver.title,"Not Found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()