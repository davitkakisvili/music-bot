from youtubesearchpython import VideosSearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path="C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


def get_input(question):
    user_input=input(question)
    return user_input

def search(link,limit_count):
    videosSearch = VideosSearch(link, limit = int(limit_count))
    return videosSearch.result()['result']


def init():
    song=get_input("enter song: ")
    limit=get_input("enter limit: ")
    results=search(song, limit)
    for result in results:
        print(result['title'])
    correct=get_input("enter the number of correct song :")
    correct=int(correct)-1
    link=results[correct]['link']
    print(link)
    link=link.split('youtube')[0]+"youtubepp"+link.split('youtube')[1]
    print(link)


    driver = webdriver.Chrome(path,chrome_options=options)
    driver.get(link)
    
    print('clicked')
    time.sleep(3)
    mp3_btn=driver.find_element_by_xpath('//*[@id="result"]/div/div[2]/ul/li[2]/a')
    mp3_btn.click()
    print('clicked')
    time.sleep(3)
    btn=driver.find_element_by_id("process_mp3_a")
    btn.click()
    print('clicked')
    try:
            open_in_browser_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="process-result"]/div/a'))
            )
            open_in_browser_btn.click()
    except:
            print('download btn failed fuck this site')
   
    while(True):
       pass
      

init()


    





    