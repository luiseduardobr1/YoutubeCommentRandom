import os, re, requests, time, random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Initialize the lists 
user=[]
link=[]

# Open Youtube Video Channel
thing_url=input('Video URL: ')
vencedores=input('How many users to select: ')


# Initialize browser
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(thing_url)
driver.execute_script("window.scrollTo(0, 400)") 

# Scroll to the end of the page
time.sleep(3)
SCROLL_PAUSE_TIME = 2
# Get scroll height
height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == height:
        break
    height = new_height
    
# Extract source code
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")
titulo = soup.title.text

link_repetido="teste"
user_repetido="teste"
for lista in soup.findAll("a", {"class" : "yt-simple-endpoint style-scope ytd-comment-renderer"}):
    if lista.text.strip()!='':
        user.append(lista.text.strip())
    if link_repetido!=lista['href'] or user_repetido==lista.text.strip():
        link.append('https://www.youtube.com'+lista['href'])
        link_repetido=lista['href']
        user_repetido=lista.text.strip()

#print(user)
#print(link)

contador=1
print('\n')
print('THE USERS ARE: ')
while contador<=int(vencedores):
    numero_selecionado=random.randint(0,len(user))
    print(user[numero_selecionado] + ' - '+link[numero_selecionado])
    contador=contador+1
    
print('\n')
print('Total of comments: ' + str(len(user)))

driver.quit()