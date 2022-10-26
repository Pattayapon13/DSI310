from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import requests

page = 1
Topic_list = []
Description_list = []
Date_list = []
Tag1_list = []
Tag2_list = []
Link_list = []
while page <= 29 :
    url = requests.get("https://www.bbc.co.uk/search?q=Heart+Disease&page=" + str(page))
    soup = BeautifulSoup(url.text, 'html.parser') 
    url.encoding = "uft-8"
    for c in soup.find_all('div',{'class':'ssrcss-11rb3jo-Promo ett16tt0'},limit=300) :                                              
        Topic = Topic_list.append(str(c.find('span',{'aria-hidden' : 'false'}).text))                                   
        Description = Description_list.append(str(c.find('p',{'class' : 'ssrcss-1q0x1qg-Paragraph eq5iqo00'}).text))
        Date = Date_list.append(str(c.find('span',{'class' : 'ssrcss-1if1g9v-MetadataText ecn1o5v1'}).text)) 
        Tag1 = Tag1_list.append([item.text for item in c.find_all('span',{'class' : 'ssrcss-1if1g9v-MetadataText ecn1o5v1'},limit=100)][1])
        Tag2 = Tag2_list.append([item.text for item in c.find_all('span',{'class' : 'ssrcss-1if1g9v-MetadataText ecn1o5v1'},limit=100)][2])
        Link = Link_list.append(c.find("a",{'class':'ssrcss-1ynlzyd-PromoLink e1f5wbog0'}).get("href"))
        Datasort = pd.DataFrame([Topic_list,Description_list,Date_list,Tag1_list,Tag2_list,Link_list]).transpose()
        Datasort.columns = ['Topic','Description','Date','Tag1','Tag2','Link']
        Normalform = Datasort.set_index('Topic')
    print("complete page number",page-1)
    print(Normalform)
    page +=1

Normalform = Datasort.set_index('Topic')
Normalform.to_excel('BBC News-Heart Disease.xlsx',engine='openpyxl')






    