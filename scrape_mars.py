from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # Set up a list to collect the data
    marslatest = {}

    # Activity 1: Retrieve Lastest Mars News Update
    # setup splinter
    ##executable_path = {'executable_path': ChromeDriverManager().install()}
    ##browser = Browser('chrome', **executable_path, headless=False)

    # URL for NASA Mars News
    ##url = 'https://redplanetscience.com/'
    ##browser.visit(url)
     
    # HTML object
    ##html = browser.html

    # Parse HTML with Beautiful Soup
    ##soup = BeautifulSoup(html, 'html.parser')
    #latestnews = soup.find_all('div', class_='list_text')

    # Retrieve all elements that contain book information
    ##marslatest['title']       = soup.find('div', class_='content_title')
    ##marslatest['paragraph']   = soup.find('div', class_='article_teaser_body')

    #marslatest['title']     = title
    #marslatest["paragraph"] = paragraph

    ##browser.quit()

    # Activity 2: latest featured Mars Image
    # setup splinter 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL for NASA Mars featured image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
      
    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the header image from Space Image website
    marsimage       = soup.find('img', class_='headerimage fade-in') 
    image           = marsimage['src']

    # Saving the the web link in featured_image)url
    marslatest["featured_image_url"] = ('https://spaceimages-mars.com/' + image)

    browser.quit()

    # Activity 3: Scraping with Pandas to created HTML tables 
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)

    # Activity 3.1: Scraping with Pandas to create the Mars information table
    # Creating HTML Table for Mars Profile

    profile_df = tables[1]
    transpose_profile_df = profile_df.transpose()
    transpose_profile_df.columns = transpose_profile_df.iloc[0]
    transpose_profile_df = transpose_profile_df[1:]
    transpose_profile_df

    marslatest["html_profile_table"] = transpose_profile_df.to_html()
    
    # Activity 3.2: Scraping with Pandas to create Mars - Earth Comparision table
    # Creating HTML Table for Mars Profile
    comparision_df = tables[0]
    transpose_comp_df = comparision_df.transpose()
    transpose_comp_df.columns = transpose_comp_df.iloc[0]
    transpose_comp_df = transpose_comp_df[1:]
    transpose_comp_df

    marslatest["html_comp_table"] = transpose_comp_df.to_html()

    # Activity 4: Scrap for Mars Hemisphere information
    # setup splinter 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL for NASA Mars News
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_images_urls = []

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain book information
    images = soup.find_all('div', class_='description')

    for image in images:
        hemisphere_info = {}
        hemisphere_info["title"] = image.find('h3').get_text()
        a = image.find('a')
        href = a['href']

        url2 = "https://marshemispheres.com/" + href
        browser.visit(url2)

        html = browser.html

        soup = BeautifulSoup(html, 'html.parser')

        wideimage = soup.find(class_='wide-image')
    
        imageurl = wideimage['src']

        hemisphere_info["img_url"] = "https://marshemispheres.com/" + imageurl

        hemisphere_images_urls.append(hemisphere_info)

        marslatest["image_url"] = hemisphere_images_urls

    browser.quit()

    #return result
    return marslatest