# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:16:22 2018

@author: chrothenbach
"""
#%% clean html
import urllib.request
from bs4 import BeautifulSoup

url = "file:///E:/Dropbox/rothenbach%20historia/History%20of%20Zerne.html"

with urllib.request.urlopen(url) as read_url:
    html = read_url.read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

#%%  break into chunks

"""
break into
pages
sentences

"""

lines = []
for line in text:
    lines.append(line)

text_sample = text[2500:5000]
print(text_sample)


text_pages = []
for i in range(5,60):
    print('\n---------Finding page' , i, '--------')
    page = '\n'+ str(i)
    start = text.find(page) + len(page) 
    end = text.find('\n'+str(i+1), start)
    text_pages.append(text[start:end])




#%% translate with googletrans

from googletrans import Translator
translator = Translator()

text_translation = []
for page in range(5,60):
    print('Translating page' , page)
    page_translated = translator.translate(text_pages[page], src='en', dest='es')
    text_translation.append(page_translated.text)


#%% translate with goslate

import goslate
gs = goslate.Goslate()
text_translation = gs.translate(text,'es')