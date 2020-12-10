import string

f=open("legitimatesite.txt","r")
fw=open("all domains from legitimate.txt","w")


for line in f:
    line=line.split('\n')
    l=line[0]
    

    # find the domain from full website address
    
    l=l[l.find('.')+1:]
    l=l[:l.find('.')]

    fstr=l+"\n"
    fw.write(fstr)
    
    print(l)

f.close()
fw.close()



f=open("all domains from legitimate.txt","r")
fw=open("all sites from domain.txt","w")


for line in f:
    """
   if line.find("www")>= 0:
      u=line.split(".")
      url=u[1]
      print("url: ",url)
   else:
      t=line.split("//")
      #print(t)
      te=t[1].split(".")
      url=te[0]
      print("url: ",url)
   #url= 'google'

    """
    line=line.split('\n')
    url=line[0]
    print("URL: ",url)



   #Generate all possible websites
      
   #replacement code     
    #print('replace every character in the url for : ',url)
    index=0
    for letter in url:
       for i in list(string.ascii_lowercase):
          replace_with=i
          new_url="http://www."+url[:index]+i+url[index+1:]+".com\n"
          fw.write(new_url)
          new_url="http://www."+url[:index]+i+url[index+1:]+".net\n"
          fw.write(new_url)
          new_url="http://www."+url[:index]+i+url[index+1:]+".org\n"
          fw.write(new_url)
         #print(new_url)
       index=index+1

   #insertion code
    #print('Insert character befor and after every character of url for : ',url)
    index=0
    for j in range(len(url)+1):
       for i in list(string.ascii_lowercase):
          new_url="http://www."+url[:index]+i+url[index:]+".com\n"
          fw.write(new_url)
          new_url="http://www."+url[:index]+i+url[index:]+".net\n"
          fw.write(new_url)
          new_url="http://www."+url[:index]+i+url[index:]+".org\n"
          fw.write(new_url)
         #print(new_url)
       index=index+1
   #deletion code
    #print('Delete a character from the url for : ',url)
    index=1
    for i in range(len(url)):
        new_url="http://www."+url[:index-1]+url[index:]+".com\n"
        fw.write(new_url)
        new_url="http://www."+url[:index-1]+url[index:]+".net\n"
        fw.write(new_url)
        new_url="http://www."+url[:index-1]+url[index:]+".org\n"
        fw.write(new_url)
        index=index+1
      #print(new_url)


f.close()
fw.close()
