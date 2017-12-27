import time
from typing import *

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    query = sys.argv[1]
    tweets = get_tweets(query)
    for tweet in tweets:
        print(tweet.text)
    #     TODO: Put chromium driver in path
    pass


def get_tweets(query: str) -> List[str]:
    browser = webdriver.Chrome()
    url = u'https://twitter.com/search?q=' + query

    browser.get(url)
    time.sleep(1)
    browser_body = browser.find_element_by_tag_name('body')
    for _ in range(5):
        browser_body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    tweets = browser.find_element_by_class_name('tweet-text')
    return tweets


if __name__ == '__main__':
    main()
