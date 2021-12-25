import requests
import bs4
import lxml
url = 'https://directory.msutexas.edu/users'

r = requests.get(url)
s = bs4.BeautifulSoup(r.text,'lxml')
dd = s.findAll('a',href=True, class_='text-blue-700') # filter the links
users_links=[]
# phones = [] # no need to use it! just print it on the console
# emails = [] # no need to use it! just print it on the console
# get users link
for i in dd:
    users_links.append(i['href']) # save the links into a list to use them later on
# get the user infos
for x in users_links:
    ur = requests.get(x) 
    us = bs4.BeautifulSoup(ur.text,'lxml')
    dd2=us.findAll('a',href=True, class_='text-blue-700') # filter the a links
    # scrap their web page
    for l in dd2:
        if "tel" in l['href']:
            print(l['href'].split(':')[1]) # print the phone number
        if "mailto" in l['href']:
            print(l['href'].split(':')[1]) # print the email
