import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Services:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=20):
        """
        This method is to wait for presence of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
        logging.info("## Checking for console error on loaded page")
        logging.info("# Wait for element to appear... %s" % locator)
        if locator.startswith("id"):
            locator = locator.replace("id=", "")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, locator)))
        elif locator.startswith('xpath='):
            locator = locator.replace("xpath=", "")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        elif locator.startswith("css"):
            locator = locator.replace("css=", "")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, locator)))

        logging.info("# Element '%s' is present." % locator)

    def assert_and_click_by_xpath(self, locator):
        """
        This method is to assert and click on the web element.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("## Checking for console error on loaded page")
        self.wait_for_element(locator)
        logging.info("# Click on element %s" % locator)
        ele = self.driver.find_element_by_xpath(locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        """
        This method is get the text present within given web element.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("## getting text for %s ##" % locator)
        return self.driver.find_element_by_xpath(locator).text

    def is_element_present(self, locator, timeout=20):
        """
        This method is to verify element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("## Checking for console error on loaded page")
        try:
            logging.info("# Wait for element to appear... %s" % locator)
            if locator.startswith("id"):
                locator = locator.replace("id=", "")
                self.driver.find_element_by_id(locator)
            elif locator.startswith('xpath='):
                locator = locator.replace("xpath=", "")
                self.driver.find_element_by_xpath(locator)
            elif locator.startswith("css"):
                locator = locator.replace("css=", "")
                self.driver.find_element_by_css_selector(locator)
            else:
                self.driver.find_element_by_id(locator)

            logging.info("# Element '%s' is present." % locator)
            return True
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % locator)
            return False

    def assert_element_present(self, locator):
        """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("# Verifying Element is present.")
        assert self.is_element_present(locator), "Element '%s' should be present." % locator

    def assert_element_is_not_present(self, locator, timeout=20):
        """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("# Verifying Element is not present.")
        assert not self.is_element_present(locator), "Element '%s' should not be present." % locator

    def wait_for_element_visible(self, locator, timeout=30):
        """
        This method is to wait for visibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
        logging.info("## Checking for console error on loaded page")
        logging.info("# Wait for element to appear... %s" % locator)
        if locator.startswith("id"):
            locator = locator.replace("id=", "")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
        elif locator.startswith('xpath='):
            locator = locator.replace("xpath=", "")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        elif locator.startswith("css"):
            locator = locator.replace("css=", "")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_invisible(self, locator, timeout=20):
        """
        This method is to wait for visibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """

        logging.info("# Wait for element to appear... %s" % locator)
        if locator.startswith("id"):
            locator = locator.replace("id=", "")
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.ID, locator)))
        elif locator.startswith('xpath='):
            locator = locator.replace("xpath=", "")
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))
        elif locator.startswith("css"):
            locator = locator.replace("css=", "")
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def is_element_visible(self, locator):
        logging.info("## Checking for console error on loaded page")
        logging.info("## finding element for %s ##" % locator)
        try:
            if locator.startswith("id"):
                return self.driver.find_element_by_id(locator.replace("id=", "")).is_displayed()
            elif locator.startswith('xpath='):
                return self.driver.find_element_by_xpath(locator.replace("xpath=", "")).is_displayed()
            elif locator.startswith("css"):
                return self.driver.find_element_by_css_selector(locator.replace("css=", "")).is_displayed()
            else:
                return self.driver.find_element_by_id(locator).is_displayed()
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % locator)
            return False

    def is_element_not_visible(self, locator):
        logging.info("## Checking for console error on loaded page")
        logging.info("## finding element for %s ##" % locator)
        try:
            if locator.startswith("id"):
                return not self.driver.find_element_by_id(locator.replace("id=", "")).is_displayed()
            elif locator.startswith('xpath='):
                return not self.driver.find_element_by_xpath(locator.replace("xpath=", "")).is_displayed()
            elif locator.startswith("css"):
                return not self.driver.find_element_by_css_selector(locator.replace("css=", "")).is_displayed()
            else:
                return not self.driver.find_element_by_id(locator).is_displayed()
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % locator)
            return False

    def assert_element_visibility(self, locator, is_visible=True):
        """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("## Checking for console error on loaded page")
        logging.info("# Verifying Element visibility.")
        assert is_visible == self.is_element_visible(locator), "Element '%s' visibility should be %s." % (
            locator, is_visible)

    def assert_element_invisibility(self, locator, is_not_visible=True):
        """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        logging.info("## Checking for console error on loaded page")
        logging.info("# Verifying Element visibility.")
        assert is_not_visible == (not self.is_element_visible(locator)), "Element '%s' visibility should be %s." % (
            locator, is_not_visible)

    def find_element(self, locator):
        logging.info("## finding element for %s ##" % locator)
        if locator.startswith("id"):
            return self.driver.find_element_by_id(locator.replace("id=", ""))
        elif locator.startswith('xpath='):
            return self.driver.find_element_by_xpath(locator.replace("xpath=", ""))
        elif locator.startswith("css"):
            return self.driver.find_element_by_css_selector(locator.replace("css=", ""))
        else:
            return self.driver.find_element_by_id(locator)

    def find_elements(self, locator):
        logging.info("## finding elements for %s ##" % locator)
        if locator.startswith("id"):
            return self.driver.find_element_by_id(locator.replace("id=", ""))
        elif locator.startswith('xpath='):
            return self.driver.find_elements_by_xpath(locator.replace("xpath=", ""))
        elif locator.startswith("css"):
            return self.driver.find_elements_by_css_selector(locator.replace("css=", ""))
        else:
            return self.driver.find_elements_by_xpath(locator.replace("xpath=", ""))

    def click_element(self, locator):
        """

        :rtype: object
        """
        logging.info("## finding element for %s ##" % locator)
        ele = self.find_element(locator)
        logging.info("## clicking on %s ##" % ele)
        ele.click()

    def get_text(self, locator):
        logging.info("## finding element for %s ##" % locator)
        if locator.startswith("id"):
            return self.driver.find_element_by_id(locator.replace("id=", "")).text
        elif locator.startswith('xpath='):
            return self.driver.find_element_by_xpath(locator.replace("xpath=", ""))
        elif locator.startswith("css"):
            return self.driver.find_element_by_css(locator.replace("css=", ""))
        else:
            return self.driver.find_element_by_id(locator)

    def check_for_console_error(self):
        error_log = self.driver.get_log('browser')
        error_log_size = len(error_log)
        if error_log_size > 1:
            logging.info("## WEB APPLICATION CONTENET IS NOT LOADED PROPERLY. HENCE TERMINATING EXECUTION ##")
            self.assertFalse(True)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_new_tab_name(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        title = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return title

    def assert_new_tab_opened(self, tab_name):
        logging.info("## verifying if %s is opened" % tab_name)
        assert tab_name == self.get_new_tab_name(), "%s should be opened" % tab_name

    def reset_page_and_nav_to_homepage(self):
        self.driver.delete_all_cookies()
        self.driver.get("https://www.atg.party/")

    def get_url(self):
        return self.driver.current_url

    def find_all_elements(self, locator):
        logging.info("## finding element for %s ##" % locator)
        if locator.startswith("id"):
            return self.driver.find_elements_by_id(locator.replace("id=", ""))
        elif locator.startswith('xpath='):
            return self.driver.find_elements_by_xpath(locator.replace("xpath=", ""))
        elif locator.startswith("css"):
            return self.driver.find_elements_by_css_selector(locator.replace("css=", ""))
        else:
            return self.driver.find_elements_by_id(locator)

    def switch_tab(self, number):
        logging.info("switching to tab " + str(number))
        self.driver.switch_to.window(self.driver.window_handles[number])

    def assert_text_present(self, text, locator, timeout=10):
        # # checks if text is not present in a specific location
        logging.info("searching for " + str(text))

        try:
            if locator.startswith("id"):
                locator = locator.replace("id=", "")
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, locator), text))
            elif locator.startswith('xpath='):
                locator = locator.replace("xpath=", "")
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, locator), text))
            elif locator.startswith("css"):
                locator = locator.replace("css=", "")
                WebDriverWait(self.driver, timeout).until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
            else:
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, locator), text))

        except TimeoutException:
            logging.info(str(text) + " is not present")
            raise AssertionError
        logging.info(str(text) + " is present")

    def assert_text_not_present(self, text, locator, timeout=10):
        # checks if text is not present in a specific location
        logging.info("searching for " + str(text))

        try:
            if locator.startswith("id"):
                locator = locator.replace("id=", "")
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, locator), text))
            elif locator.startswith('xpath='):
                locator = locator.replace("xpath=", "")
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, locator), text))
            elif locator.startswith("css"):
                locator = locator.replace("css=", "")
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
            else:
                WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, locator), text))

        except TimeoutException:
            logging.info(str(text) + " is not present")
            return
        # raise error if element was found in the specific location
        logging.info(str(text) + " is present")
        raise AssertionError

    # certain objects are only clickable in specific locations
    def click_at_a_position(self, element, down, right):
        # specify pixels down and right from the upper left corner of the element
        ele = element
        logging.info("## clicking on %s ##" % ele)
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(ele, down, right)
        action.click()
        action.perform()

    def url(self):
        return self.driver.current_url

    def execute_javascript(self, script):
        self.driver.execute_script(script)

    def refresh_page(self):
        self.driver.refresh()

    def go_back(self):
        logging.info("## going to the previous page ##")
        self.driver.back()

    def check_tab(self, tab):
        logging.info("checking if " + tab + " opened")
        self.driver.switch_to.window(self.driver.window_handles[1])
        check = True if tab == self.driver.title else False
        self.driver.switch_to.window(self.driver.window_handles[0])
        return check

    def change_frame(self):
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)

    def wait(self, t):
        logging.info("## waiting... ##")
        self.driver.implicitly_wait(t)

    def get_tab_name(self):
        return self.driver.title

    def get_website(self, url):
        self.driver.get(url)
