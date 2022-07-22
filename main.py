from bs4 import BeautifulSoup
import requests
import replit

URL = 'https://flex.myreservations.nl/reserveren.php?id=62673c58d02aa&token=5595b875e2f3634abb611df83b566d8c&iframe&orginfo=yes'

page = requests.get(URL).text
  
soup = BeautifulSoup(page, 'html.parser')
res = soup.find_all("div", class_='myDiv')


replit.clear()

for e in res:
  txtSpans = e.find_all("span")
  for t in txtSpans:
   if t.text.strip() != "":
    print(t.text.strip())
