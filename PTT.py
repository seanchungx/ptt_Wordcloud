# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:16:17 2019

@author: kidneyweakx
"""
import tkinter as tk # GUI

from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup 

import jieba


def show():
    # 用cookies 略過已滿18歲
    response = requests.get(en.get(), cookies={'over18':'1'})
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    t = soup.find_all('div','push')
    # 抓取所有推文    
    msg = ''
    for t in t: 
        msg += t.find('span', 'f3 push-content').getText().replace(':','').strip()
    # 結巴斷詞
    wordlist = jieba.cut(msg,cut_all=True)
    split = " ".join(wordlist)
    stopwords = [line.strip() for line in open('rmword.txt',encoding='UTF-8').readlines()]
    # 文字雲
    wordcloud = WordCloud(background_color='white', font_path='msjh.ttc',stopwords=stopwords).generate(split)
    # 壓成圖片
    wordcloud.to_file('tmp.png')
    # 在介面加入圖片
    photo = tk.PhotoImage(file= 'tmp.png')
    cv = tk.Canvas()
    cv.pack()
    cv.create_image(10, 10, image=photo, anchor='nw')
    # 運行介面
    win.mainloop()
    
# 創建主視窗、大小和標題
win = tk.Tk() 
win.geometry("500x700")
win.title("PTT 推文wordcloud")
# 加入文字、輸入框和按鈕
label = tk.Label(win,text = "Enter PTT URL").pack()
# https://www.ptt.cc/bbs/Gossiping/M.1575971635.A.410.html
en = tk.StringVar()
enter = tk.Entry(win,text=en).pack()
btn = tk.Button(win,text="Enter",padx =2, pady= 2,command =show).pack()
# 運行介面
win.mainloop()
