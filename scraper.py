import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Vakance:
    nosaukums: str
    apraksts: str
    vieta: str
    alga: Optional[str]
    datums: str
    saite: str

def iegut_vakances(url: str) -> List[Vakance]:
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    vakances = []
    sludinajumi = soup.find_all('tr', class_='list-row')

    for sludinajums in sludinajumi:
        nosaukums_elem = sludinajums.find('a', class_='list-ad-title')
        if not nosaukums_elem:
            continue

        nosaukums = nosaukums_elem.text.strip()
        saite = 'https://www.ss.com' + nosaukums_elem['href']

        apraksts_elem = sludinajums.find('div', class_='list-ad-description')
        apraksts = apraksts_elem.text.strip() if apraksts_elem else ''

        vieta_elem = sludinajums.find('td', class_='list-ad-region')
        vieta = vieta_elem.text.strip() if vieta_elem else ''

        alga_elem = sludinajums.find('td', class_='list-ad-price')
        alga = alga_elem.text.strip() if alga_elem else None

        datums_elem = sludinajums.find('td', class_='list-ad-date')
        datums = datums_elem.text.strip() if datums_elem else ''

        vakance = Vakance(nosaukums, apraksts, vieta, alga, datums, saite)
        vakances.append(vakance)

    return vakances


if __name__ == "__main__":
    url = 'https://www.ss.com/lv/work/are-required/programmer/'
    vakances = iegut_vakances(url)
    for vakance in vakances:
        print(vakance)
