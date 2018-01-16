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

#%%

from googletrans import Translator
translator = Translator()

text_translation = translator.translate(text[10000:10250], src='en', dest='es')

print(text_translation.text)