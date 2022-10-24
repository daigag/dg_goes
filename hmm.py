import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.calameo.com/read/002502199936ac19ec130?authid=GrQmO2SzZn2T") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('.jpg'):
    print(item['src'])