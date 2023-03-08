import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.getLogger().setLevel(logging.INFO)



class WebpageNavigationBot:
    def __init__(self, url):
        logging.info('Class initialization')
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.get(url)

    def close_driver(self):
        logging.info('Closing browser window')
        self.driver.close()

def decline_cookies(bot):
    '''Declines cookies in orioninc.com homepage'''
    logging.info('Decline_cookies function started')
    try:
        bot.driver.implicitly_wait(5)
        decline_cookies_button = bot.driver.find_element(By.ID, "hs-eu-decline-button")
        decline_cookies_button.click()
    except NoSuchElementException:
        pass
    logging.info('Decline_cookies function ended')


def navigate_to_careers_in_europe_page(bot):
    '''This function hovers over "comapny" in orioninc.com home page and goes to carrer page.
    In the carrer page it finds job opportunities in Europe Link text and clicks it'''
    logging.info('navigate_to_careers_in_europe_page function started')

    chain = ActionChains(bot.driver)

    random = bot.driver.find_element(By.ID, 'menu-28')
    company = bot.driver.find_element(By.ID, 'menu-27')

    chain.move_to_element(random).perform()
    chain.move_to_element(company).perform()

    wait = WebDriverWait(bot.driver, 10)
        
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="primaryMenu"]/ul/li[5]/div/div/div/div[1]/a[6]')))
    element.click()

    careers_in_europe = bot.driver.find_element(By.LINK_TEXT, "Europe")
    careers_in_europe.click()
    logging.info('navigate_to_careers_in_europe_page function ended')


def location_filters(bot):
    '''This function resets all filters in carrer page.
      After resettings all filters it filters all job offers in Lithuania and then Vilnius'''
    logging.info('location_filters function started')

    wait = WebDriverWait(bot.driver, 10)        

    reset_filters = bot.driver.find_element(By.XPATH, '//*[@id="search-filter"]/div[2]/a')
    reset_filters.click()

    locations_in_europe = bot.driver.find_element(By.XPATH, '//*[@id="search-filter"]/div[5]/div/div[5]/span')
    try:
        locations_in_europe.click()
    except:
        wait.until(EC.element_to_be_clickable(locations_in_europe)).click()

    locatios_in_lithuania = bot.driver.find_element(By.XPATH, '//*[@id="search-filter"]/div[5]/div/div[9]')
    locatios_in_lithuania.click()

    jobs_in_Vilnius = bot.driver.find_element(By.XPATH, '//*[@id="search-filter"]/div[5]/div/div[9]/div')
    jobs_in_Vilnius.click()
    logging.info('location_filters function ended')


def apply_for_pythonTA(bot):
    '''This function finds the exact job we want to apply for, clicks it and fills up the form'''

    logging.info('apply_for_pythonTA function started')
    job = bot.driver.find_element(By.LINK_TEXT, "Python Test Automation Engineer")
    job.click()

    apply_btn = bot.driver.find_element(By.XPATH, '//*[@id="post-16579"]/div/div[3]/div[2]/div/div[1]/a')
    apply_btn.click()

    bot.driver.implicitly_wait(5)

    first_name = bot.driver.find_element(By.ID, "input_7_2")
    first_name.send_keys("Modestas")

    last_name = bot.driver.find_element(By.ID, "input_7_3")
    last_name.send_keys("Ramelis")

    email = bot.driver.find_element(By.ID, "input_7_4")
    email.send_keys("modestas.ramelis@orioninc.com")

    phone_number = bot.driver.find_element(By.ID, "input_7_5")
    phone_number.send_keys("+37067029179")

    search = bot.driver.find_element(By.XPATH, '//*[@id="field_7_6"]/div/div/div[2]/b')
    search.click()

    country_of_application = bot.driver.find_element(By.CSS_SELECTOR, '#field_7_6 > div > div > div.selectric-items > div > ul > li:nth-child(128)')
    country_of_application.click()

    state = bot.driver.find_element(By.ID, "input_7_7")
    state.send_keys("Vilnius")
    
    time.sleep(15)
    logging.info('apply_for_pythonTA function ended')


logging.info('Start of program')

orion_bot = WebpageNavigationBot(url="https://www.orioninc.com/")
decline_cookies(bot=orion_bot)
navigate_to_careers_in_europe_page(bot=orion_bot)
location_filters(bot=orion_bot)
apply_for_pythonTA(bot=orion_bot)

orion_bot.close_driver()
logging.info('End of program')