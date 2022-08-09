#Import needed libraries
from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options

#Set Chrome for webdriver

optionss = Options()
optionss.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path='C:\est\chromedriver.exe', options=optionss) #Make sure to change the path of chromedriver.exe !!

#Lists of needed data
laptops=[]
prices=[]
rate=[]

#Website requested..
driver.get("https://www.amazon.com/s?k=laptop&sprefix=lap%2Caps%2C410&ref=nb_sb_ss_retrain-deeppltr_1_3")

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

#Storing Products into lists
for info in soup.findAll('div', attrs={'class':'a-section a-spacing-small a-spacing-top-small'}):

    pName = info.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
    if pName is not None:
        laptops.append(pName.text)
    else:
        pName = None

    pPrice = info.find('span', attrs={'class':'a-offscreen'})
    if pPrice is not None:
        prices.append(pPrice.text)
    else:
        pPrice = None

    pRating = info.find('span', attrs={'class': 'a-icon-alt'})
    if pRating is not None:
        rate.append(pRating.text)
    else:
        pRating = None
    
    #prices.append(pPrice.text)
    #rate.append(pRating.text)
#Push the products to the lists


print("Now creating the cvs file ...")
df = pd.DataFrame({'Product Name':laptops,'Price':prices,'Rating':rate}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
print("Created")

