#pip install bs4
import bs4
#pip install requests
import requests
#pip install csv (if needed)
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = bs4.BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)
    writer.writerow([quote.text, author.text])


file.close()
 
