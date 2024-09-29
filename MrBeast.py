#This program is the equivalent of telling someone
#to go to Twitter's website and copy(into a notebook) MrBeast's tweets.

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize Chrome driver
service = Service(executable_path=CM().install())
driver = webdriver.Chrome(service=service)

# Go to the profile
driver.get("https://x.com/MrBeast")

# Wait for the page to load
time.sleep(5)

# Scroll to load more tweets
for i in range(10):
    driver.execute_script("window.scrollBy(0, 2000)")
    time.sleep(1)


# Locate tweet elements
tweets = driver.find_elements(By.XPATH, '//div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div')

#Create a new file(tweets.txt) to store the tweets
file = open("tweets.txt", "w")

# Extract and print tweet text
#Also store tweet in the new file(tweets.txt)
for tweet in tweets:
    print(tweet.text)
    file.write("------------------------------------------------\n" + tweet.text + "\n")
