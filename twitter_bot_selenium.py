import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import io
import csv
import os
import re
import config # config is a python file that has your login details to twitter

# disabling notification on firefox
# options = webdriver.FirefoxOptions()
# options.set_preference("dom.push.enabled", False)
# driver = webdriver.Firefox(firefox_options=options)


options = webdriver.ChromeOptions()
poi = {"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs",poi)
driver = webdriver.Chrome(executable_path='chromedriver',options=options)



# This function likes tweets from someone's twitter timeline

def profile_like_tweets(twitter_profile_account,scroll_number):
    # opening twitter login page
    driver.get('https://twitter.com/login/')
    # driver.maximize_window()
    time.sleep(10)

    # Login to twitter
    username_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'
    password_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'
    login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div'

    driver.find_element_by_xpath(username_xpath).send_keys(config.username)
    time.sleep(10)
    driver.find_element_by_xpath(password_xpath).send_keys(config.password)
    # time.sleep(10)
    driver.find_element_by_xpath(login_button_xpath).click()

    driver.get(twitter_profile_account)

    # to scroll through the twitter profile timeline
    for i in range(scroll_number):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)


    # Get the links of each tweets on the twitter profile account
    tweet_xpath = '//div[@data-testid="tweet"]'
    tweet_links_xpath = '//a[@href]' 
    tweet_link = driver.find_elements_by_xpath(tweet_links_xpath)
    elements = driver.find_elements_by_xpath(tweet_xpath)
    print(len(elements))

    tweets = [tweet.get_attribute("href") for tweet in tweet_link]
    main_tweets = set(())
    for i in tweets:
        if '/status/' in i and '/photo/' not in i:
            main_tweets.add(i)
        else:
            pass

    print(main_tweets)

    # Like tweets

    for tweets in main_tweets:
        driver.get(tweets)
        driver.switch_to_active_element()
        time.sleep(3)
        like = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="like"]')))
        like.click()
        time.sleep(2)

  
twitter_profile = 'https://twitter.com/coolpythoncodes'
while True:
    profile_like_tweets(twitter_profile,10)