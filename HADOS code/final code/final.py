import string
import urllib.request
import time
import ssl

import requests
from bs4 import BeautifulSoup

import nltk   
from urllib.request import urlopen

thresehold=0.2
sleeptime=1

print("Hell World")
fw=open("Testing urls.txt","w")


#generate all Typosquatts

url="ntv"
index=0
for letter in url:
    for i in list(string.ascii_lowercase):
        replace_with=i
        new_url="http://www."+url[:index]+i+url[index+1:]+".com\n"
        print(new_url)
        fw.write(new_url)
        #new_url="http://www."+url[:index]+i+url[index+1:]+".net\n"
        #print(new_url)
        #fw.write(new_url)
        #new_url="http://www."+url[:index]+i+url[index+1:]+".org\n"
        #print(new_url)
        #fw.write(new_url)
         #print(new_url)
    index=index+1
fw.close()

#be prepared for cosine similarities by taking the texts in documents
documents=[]
fd=open("dataset.txt","r")
for l in fd:
    l=l.split("\n")
    data=l[0]
    documents.insert(len(documents),data)
print("Documents: ")
print(documents[17])


#test their existance and collect the html text if exxist


valid=0
output=""

f=open("Testing urls.txt","r")
for line in f:
    line=line.split('\n')
    url=line[0]
    result=url

    print("\n",url,"\n")

    try: html = urlopen(url,timeout=5).read()    
    #raw = nltk.clean_html(html)  
    #print(raw)
    except urllib.error.URLError as e:
        print(e.reason)
        continue
    except urllib.error.HTTPError as e:
        print(e.code)
        continue
    except ssl.SSLError as err:
        print(err.reason)
        continue

    soup=BeautifulSoup(html, "html5lib")


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

    import sys
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    #print(text.translate(non_bmp_map))
    

    #print(text)

    
    

    # cosine similarities

    documents.insert(0,text)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    #print (tfidf_matrix.shape[0])
    #print (tfidf_matrix)


    from sklearn.metrics.pairwise import cosine_similarity
    #sim=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)



    documents.remove(text)
    #print(documents[0])

    sim=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    
    #print("\n\n\nThe similarity matrix is: ",sim[0])
    #print("\n\n")
    a=sim[0]
    x=a[1]
    for k in range(1,len(a)-1):
        if a[k]>x:
            x=a[k]
    print("\n\nMax: ",x)
    
    if x>thresehold:
        output=output+result+" "+str(x)+"\n"
        print("yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",result)
    
    time.sleep(sleeptime)
print("The output is: ")
print(output)
    
    

