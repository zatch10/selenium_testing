import unittest     
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, JavascriptException
import requests

class Tests(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.maximize_window()
    
    def test_1(self):
        #set load time detection
        self.driver.set_page_load_timeout(10)

        try:
            #get website
            self.driver.get("https://www.atg.party")

            #to check if response is 200
            r = requests.get(self.driver.current_url)
            hcode = requests.options(r.url)
            hcode = str(hcode.status_code)
            self.assertTrue(hcode.startswith('200')) 

            #to check if 404 resources are present in page_source
            self.assertFalse("404" in self.driver.page_source)

            #sign in process
            self.driver.find_element_by_link_text("Login").click() 
            email = self.driver.find_element_by_id("email")
            email.clear()
            email.send_keys("hello@atg.world")

            password = self.driver.find_element_by_id("password")
            password.clear()
            password.send_keys("Pass@123")

            self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div[2]/div[1]/div/div/div/div/div/div/div[1]/form/div[4]/button").click()

            #to check if response is 200
            r = requests.get(self.driver.current_url)
            hcode = requests.options(r.url)
            hcode = str(hcode.status_code)
            self.assertTrue(hcode.startswith('200'))

            #to check if 404 resources are present in page_source
            self.assertFalse("404" in self.driver.page_source)
            return self.driver

        except TimeoutException:         
            print("timeout")
            raise AssertionError
            
        except JavascriptException:
            print("javascript error")
            raise AssertionError

        except AssertionError:
            return False


    def test_2(self):
        try:
            #sign in with test_1()
            self.driver = self.test_1()

            #initiate load time detection and get website
            self.driver.set_page_load_timeout(10)
            self.driver.get("https://www.atg.party/article")
        
            #enter test in title and desription, then submit
            title = self.driver.find_element_by_id("title")
            title.clear()
            title.send_keys("test with python")
            article = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/section/div[1]/div/form/div[2]/div[2]/div[1]/div[1]/div[2]/div")
            article.clear()
            article.send_keys("test with selenium")
            self.driver.find_element_by_css_selector("button.btn:nth-child(7)").click()

            #to check if response is 200
            r = requests.get(self.driver.current_url)
            hcode = requests.options(r.url)
            hcode = str(hcode.status_code)
            self.assertTrue(hcode.startswith('200')) 
            
            #to check if 404 resources are present in page_source
            self.assertFalse("404" in self.driver.page_source)
            
        except JavascriptException:
            print("javascript error")
            raise AssertionError
        
        except TimeoutException:
            print("timeout")
            raise AssertionError

        except AssertionError:
            return False



    @classmethod
    def tearDownClass(inst):
    ##will work with chromedrive. Geckodriver does not support get log at this moment
    #     # browser_logs = inst.driver.get_log("browser")
    #     # errors = [logentry['message'] for logentry in browser_logs if logentry['level'] == 'SEVERE']
    #     # if errors:
    #     #     inst.fail('The following JavaScript errors occurred: {"; ".join(errors)}')
        inst.driver.close()


if __name__ == '__main__':
    unittest.main()
