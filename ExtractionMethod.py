import bs4
import urllib.request as url
import re
#!pip3 install nltk
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import heapq
from nltk.stem import *
from nltk.stem.porter import *

# ---- Step 1: download the article
url_name = "https://www.linkedin.com/pulse/digital-new-word-describe-analog-world-lauro-valente/"
web = url.urlopen(url_name)

# ---- Step 2: structure and pre-process
page = bs4.BeautifulSoup(web,'html.parser')
elements = page.find_all(['p','blockquote','h2'])
article = ''
for i in elements:
 article+= (i.text)

# article

processed = article.replace(r'^\s+|\s+?$','')
processed = processed.replace('\n',' ')
processed = processed.replace("\\",'')
processed = processed.replace(",",'')
processed = processed.replace('"','')
processed = processed.replace('”','')
processed = processed.replace('“','')
processed = processed.replace('’','')
processed = re.sub(r'\[[0-9]*\]','',processed)

# processed

# ---- Step 3: tokenize, and count occurences based on the words' stem

sentences = sent_tokenize(processed)

nltk.download('punkt')
nltk.download('stopwords')
stop_word = stopwords.words('english')
stemmer = PorterStemmer()

frequency = {}
processed1 = processed.lower()
for word in word_tokenize(processed1):
 if word not in stop_word and word not in string.punctuation:
  singular_word = stemmer.stem(word)
  if singular_word not in frequency.keys():
   frequency[singular_word]=1
  else:
   frequency[singular_word]+=1

# frequency

# top 10 words
# heapq.nlargest(10,frequency,key = frequency.get)

# count word occurences
max_fre = max(frequency.values())
for word in frequency.keys():
 frequency[word]=(frequency[word]/max_fre)

#frequency

# ---- Step 4: Count score of sentences
sentence_score = {}
for sent in sentences:
 for word in word_tokenize(sent):
  singular_word = stemmer.stem(word)
  if singular_word in frequency.keys():
   if len(sent.split(' '))<30:
    if sent not in sentence_score.keys():
     sentence_score[sent] = frequency[singular_word]
    else:
     sentence_score[sent]+=frequency[singular_word]
	 
# sentence_score

# Final: print result 

summary = heapq.nlargest(3,sentence_score,key = sentence_score.get)
summary = ' '.join(summary)

summary
