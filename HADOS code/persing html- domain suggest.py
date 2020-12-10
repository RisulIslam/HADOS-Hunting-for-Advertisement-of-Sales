import requests
from bs4 import BeautifulSoup

import nltk   
from urllib.request import urlopen

f=open("domain sale urls.txt","r")
fnew=open("dataset.txt","w",encoding="utf-8")
documents=[]
i=1
for line in f:
    line=line.split('\n')
    url=line[0]
    print("\nURL: ",i," : ",url,"\n\n")
    i=i+1
    
    html = urlopen(url).read()    
    #raw = nltk.clean_html(html)  
    #print(raw)

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


    text=text.replace("\n"," ")

    import sys
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    #print(text.translate(non_bmp_map))
    text=text.translate(non_bmp_map)


    text=text+"\n"
    fnew.write(text)
    print(text)
    

    #documents.insert(len(documents),str(text))

    

fnew.close()
print("test\n\n\n")
#print(documents)






"""

# similarity measure


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print (tfidf_matrix.shape[0])
print (tfidf_matrix)


from sklearn.metrics.pairwise import cosine_similarity
#sim=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)



#documents.remove(s)
print(documents)


sim=cosine_similarity(tfidf_matrix[tfidf_matrix.shape[0]-1:], tfidf_matrix)
print(sim[0])


resp = requests.get('http://www.google.com')
print(resp)
txt = resp.text
print("Text response: \n")
print(txt)


print("Start souping: \n")

soup = BeautifulSoup(txt,"html5lib")
#print(soup.text)
x=soup.find_all('p')[0].text
print(x)

"""
