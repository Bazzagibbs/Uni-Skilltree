import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Home page scraping
startUrl = 'https://unitguides.mq.edu.au/units/show_year/2020/Department%20of%20Computing'
url = startUrl
hasMorePages = True

while hasMorePages:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    unitListTable = soup.find(class_='table-search-results')
    # remove "help" div
    unitListTable.find(class_='unit-guide-list-header').decompose()

    unitElements = unitListTable.find_all('a')

    for unitElement in unitElements:
        # print(unitElement['href'])
        unitName = unitElement.find(class_='underline')
        unitLink = unitElement['href']
        print(unitLink + ' --> ' + unitName.text)

    nextPage = soup.find(class_='next_page')
    if 'disabled' in nextPage['class']:
        print('No more pages')
        hasMorePages = False
    else:
        relUrl = nextPage.find('a')['href']
        url = urljoin(startUrl, relUrl)
