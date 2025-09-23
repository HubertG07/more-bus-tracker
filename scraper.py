import requests
from bs4 import BeautifulSoup

def getBusInfo(url):
    timetable = {}
    stopNames = []
    webInfo = requests.get(url)
    soup = BeautifulSoup(webInfo.text, 'html.parser')
    stopRow = soup.find_all('th',attrs={'scope': 'row'})
    for row in stopRow:
        stopNames.append(row.find("a").text.strip())

    rows = soup.find_all('tr')
    for row in rows:
        stop_tag = row.find("a")
        if stop_tag:
            stop = stop_tag.text.strip()
            times = []
            for td in row.find_all("td"):
                times.append(td.text.strip())
            timetable[stop] = times

    return timetable
    ##return requests.get(url)