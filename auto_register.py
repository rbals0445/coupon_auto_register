# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 00:03:44 2021
coupon auto register program
@author: HKM
"""
import time

from selenium import webdriver  #셀레니움 프레임워크에서 webdriver객체 가져옴
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

file_path = ['./chromedriver/chromedriver91.exe','./chromedriver/chromedriver90.exe','./chromedriver/chromedriver89.exe','./chromedriver/chromedriver88.exe','./chromedriver/chromedriver87.exe','./chromedriver/chromedriver86.exe','./chromedriver/chromedriver85.exe',
             './chromedriver/chromedriver84.exe']


global code
try:
    cred = credentials.Certificate('json파일위치')
except:
    print("인증서 가져오기 실패.")


try :
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'url'
    })
except :
    print("already accessed")

dir = db.reference('code')
code = dir.get()

def connect() :
    url = 'https://game.devplay.com/coupon/ck/ko'
    for i in file_path :
        try :
            driver = webdriver.Chrome(i)
        except : 
            print("Error : There is no matched ChromeDriver. Check your Chrome version.")
    
                            
    driver.get(url)
    id_box = driver.find_element_by_id('email-box')
    code_box = driver.find_element_by_id('code-box')
    id_box.send_keys(x1)
    for i in code:
        code_box.clear()
        code_box.send_keys(i)
        #print(i)
        click = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/form/div[4]/div')
        click.click()
        time.sleep(1)
        alarm = driver.switch_to_alert()
        alarm.accept()

def getSquareRoot ():  
    global x1
    x1 = entry1.get()
    x1 = x1.upper()
    connect()
    return;
    
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)    
button1 = tk.Button(text='ID 입력 후 클릭', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)
root.mainloop()
    
    