import os
import time
import random
from http.cookies import SimpleCookie

from selenium import webdriver
from selenium.webdriver.chrome.options import Options







def crawl_page(url,scroll_count=10):
    """
    request and crawl the page from the `url` parameter, and scroll down the page in order to load more data.
    the parameter `scroll_count` specifies how many times the page should be scrolled.
    """

    # get facebook cookie from the env variable FB_COOKIE
    FB_COOKIE = os.getenv("FB_COOKIE")


    # Set chrome webdriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    # initialize chrome webdriver
    driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver_linux64/chromedriver")

    
    driver.get(url)
    # Parse cookies from string format to Python Dict
    cookie = SimpleCookie()
    cookie.load(FB_COOKIE)
    for key, morsel in cookie.items():
        driver.add_cookie({"name":key,"value":morsel.value})

    # In order to apply the new cookies settings, we need to request the page again and reload the browser for the cookies settings to take effect.
    driver.get(url)
    driver.refresh()
    for i in range(1,scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down the page
        time.sleep(random.randint(3,5)) # using random to avoid being blocked
    # Saving the html source code
    html_source = driver.page_source
    with open("./results.html","w") as file:
        file.write(html_source)
    
    return html_source