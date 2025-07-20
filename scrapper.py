import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup(['script', 'style']):
            tag.decompose()

        
        raw_text = soup.get_text(separator='\n')

        lines = []
        for line in raw_text.splitlines():
            stripped = line.strip()
            if stripped != '':
                lines.append(stripped)

        
        return '\n'.join(lines)

    except requests.RequestException:
        return ''
