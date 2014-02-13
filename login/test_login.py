import unittest,time,login
from selenium import webdriver


class WordPressTestCase(unittest.TestCase):
    dr = None

    def setUp(self):
        self.dr = webdriver.Chrome()
        
    def test_login(self):
        con = login.commen(self.dr)
        con.login()
        print self.dr.current_url
        self.assertTrue('wp-admin' in self.dr.current_url)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()
