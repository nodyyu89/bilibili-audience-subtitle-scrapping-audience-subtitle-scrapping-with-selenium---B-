# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:45:19 2019

@author: yunod
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import csv
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import win32clipboard
import pyautogui
import os

excel_path = os.getcwd() + 'bilibili_dm.csv'  # 放彈幕的 csv  # store audience subtitle in a csv file 
url = r'https://www.bilibili.com/video/av4050443?from=search&seid=6283533534040097040'   
#這裡放 bilili url  # Here is the path of one bilibili video url

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument('--proxy-server=1.2.3.4:8080')
base_path = os.getcwd()
browser = webdriver.Chrome(base_path + 'chromedriver.exe',chrome_options=chrome_options)

excel = open(excel_path, mode='a', newline='', errors='ignored',encoding='utf-8')
bilibili_excel_writer = csv.writer(excel, delimiter=',')
bilibili_excel_writer.writerow(['url','video_time_point','jump_subtitle','date','number'])

browser.get(url)
time.sleep(3)
jump_subtitle_btn = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[1]/div[1]/span').click()
time.sleep(3)

scroll_bar = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/div/div')
scroll_bar.click()
data = []
for i in range(0,3000):    # 隨彈幕數而定  # it depends on the number of audience subtitle
    for j in range(1,40):  
        try:
            video_time_point = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/ul/li['+str(j)+']/span[1]').text
            jump_subtitle = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/ul/li['+str(j)+']/span[2]').text
            date = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/di v[1]/div/div[2]/div/div[2]/div[3]/div[1]/ul/li['+str(j)+']/span[3]').text
            print(video_time_point,jump_subtitle,date,i)
            data.append((url,video_time_point,jump_subtitle,date,str(i)))
            bilibili_excel_writer.writerow([url,video_time_point,jump_subtitle,date,str(i)])
        except NoSuchElementException:
            scroll_bar = browser.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/div/div')
            pyautogui.moveTo(scroll_bar.location['x'],scroll_bar.location['y'])
            pyautogui.scroll(-500)
            print(i)
            break
excel.close()        
        


