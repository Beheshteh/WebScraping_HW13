#Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that
#will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# Dependencies
#from os import getcwd
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def get_title_news(browser):
    
    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    
    # Retrieve page with the requests module
    response = requests.get(url)
    
    time.sleep(2)
    soup = bs(response.text, 'html.parser')

    # Retrieve the parent divs for latest articles title and paragraph

    result = soup.find('div', class_='content_title')
    news_title = result.text

    result = soup.find('div', class_='rollover_description_inner')    
    news_p = result.text

    print("news title = ", news_title)
    print("news content = ", news_p)
    return(news_title, news_p)

# JPL Mars Space Images - Featured Image
def get_featured_image_url(browser):
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
  
    browser.visit(url)
    time.sleep(3)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(3)
    browser.click_link_by_partial_text('more info')
   # while not browser.html:
    time.sleep(3)
        
    #get html code once at page
    image_html = browser.html
    print("Beheshteh ")
    while not browser.html:
        time.sleep(1)

    #parse
    soup = bs(image_html, "html.parser")
    
    results = soup.find('article')
    image_path = results.find('figure', 'lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov" + image_path

    print("featured_image_url = ", featured_image_url)
    return(featured_image_url)


# Mars Weather
def get_weather(browser):
    
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    
    time.sleep(2)
    soup = bs(response.text, 'html.parser')
    
    # Retrieve the parent divs for all articles title
    results = soup.find_all('div', class_='js-tweet-text-container')
    mars_weather = results[0].text
    print(mars_weather)
    return(mars_weather)


# Mars Hemisperes
def get_hemisperes_info(browser):
    
    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Retrieve page with the requests module
    response = requests.get(url)
    soup = bs(response.text, 'html.parser') 
    hemisphere_image_urls = []

    results = soup.find_all('div', class_='item')

    for result in results:
        a = result.find('a')
        title = a.h3.text
        link = "https://astrogeology.usgs.gov" + a['href']
    
        #follow link from each page
        browser.visit(link)
        while not browser.html:
            time.sleep(1)
    
        #get image links
        image_page = browser.html
        soup = bs(image_page, 'html.parser')
        img_url = soup.find('div', class_='downloads').find('li').a['href']
    
        
        hemisphere_image_urls.append({"Title": title, "Image_Url": img_url})
        print(hemisphere_image_urls)
        
    return(hemisphere_image_urls)
    
def scrape():
    
    browser = init_browser()
    
    space_mission = {}
    hemisphere_image = []
    
    # NASA Mars News
    news_title , news_p = get_title_news(browser)
    space_mission["title"] = news_title
    space_mission["news_p"] = news_p
    

    #JPL Mars Space Images - Featured Image
    image_url = get_featured_image_url(browser)
    space_mission["featured_image"] = image_url
    
    # Mars Weather
    weather_info = get_weather(browser)
    space_mission["weather_mars"] = weather_info

    # Mars Facts
    
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)
    

    Mars_df = tables[0]
    Mars_df.columns = ['Mars_Fact', 'Value']
    Mars_df.set_index('Mars_Fact', inplace=True)
    Mars_html = "".join(Mars_df.to_html().split("\n"))
    space_mission["facts"] = Mars_html
    
    
    # Mars Hemisperes
    browser = init_browser()
    hemisphere_image = get_hemisperes_info(browser)
    space_mission["hemisphere_image"] = hemisphere_image
    
    return(space_mission)
    
