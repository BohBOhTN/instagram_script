from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with open('links.txt', 'r') as file:
    links = file.read().split(',')

links = [link.strip() for link in links]
print(len(links))

def pasting_link(img_link):
    driver = webdriver.Chrome()
    driver.get('https://inflact.com/downloader/instagram/photo/')
    input_link = driver.find_element(By.XPATH,"//input[@id='downloaderform-url']")
    time.sleep(2)
    input_link.send_keys(img_link)
    search_button = driver.find_element(By.XPATH,"//button[@id='search']")
    search_button.click()
    time.sleep(7)
    download_image_link = driver.find_element(By.XPATH,"//a[@class='download-button btn btn-primary downloader-modal-w']")
    download_image_link.click()
    time.sleep(2)
    driver.quit()
    


for link in links:
    pasting_link(link)

