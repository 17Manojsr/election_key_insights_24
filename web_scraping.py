import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_eci_results(url):
    
    response = requests.get(url)

    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')

        
        table = soup.find('table', {'id': 'div1'})

        
        headers = ['Constituency', 'Const. No.', 'Leading Candidate', 'Leading Party', 'Trailing Candidate', 'Trailing Party', 'Margin', 'Status']

        
        rows = []
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1:
                row_data = {
                    'Constituency': cells[1].text.strip(),
                    'Const. No.': cells[2].text.strip(),
                    'Leading Candidate': cells[3].text.strip(),
                    'Leading Party': cells[4].text.strip(),
                    'Trailing Candidate': cells[5].text.strip(),
                    'Trailing Party': cells[6].text.strip(),
                    'Margin': cells[7].text.strip(),
                    'Status': cells[8].text.strip()
                }
                rows.append(row_data)

        
        df = pd.DataFrame(rows, columns=headers)

        
        print(df.head())

        
        df.to_csv('Election_results_2024.csv', index=False)

    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')


if __name__ == "__main__":
    
    url = 'https://results.eci.gov.in/'

    
    scrape_eci_results(url)
