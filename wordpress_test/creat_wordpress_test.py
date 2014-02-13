import unittest,login,time
from selenium import webdriver

class WordPressTestCase(unittest.TestCase):
    dr  = None
    login_url = 'http://localhost/wordpress/wp-login.php'
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'
    
    def setUp(self):
      self.dr = webdriver.Chorme()
     
      
    def test_login(self):
        self.login()
        print self.dr.current_url
        self.assertTrue('wp-admin' in self.dr.current_url)

    def test_create_post(self):
        self.login()
        title = self.creat_post()

        self.dr.get(self.post_list_url)
        post_list_table = self.dr.find_element_by_class_name('wp-list-table')
        self.assertTrue(title in post_list_table.text)

    def login(self):
        self.dr.get(self.login_url)
        self.dr.find_element_by_name('log').send_keys('admin')
        self.dr.find_element_by_name('pwd').send_keys('admin')
        self.dr.find_element_by_name('wp-submit').click()


    def creat_post(self):
        create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
        self.dr.get(create.post_url)
        title_or_content = 'new post' + str(time.time())
        self.dr.find_element_by_name('post_title').send_keys(title_or_content)
        js = "document.getElementById"('content_ifr').contentWindow.document.body.innerHtml='" + title_or_content + "'"
        print js
        self.dr.execute_script(js)
        self.dr.find_element_by_name('publish').click()

        return  title_or_content


  
    def tearDown(self):
            sleep(3)
            self.dr.quit()

    if __mane__=='__main__':
            unittest.main()
      
    
   
