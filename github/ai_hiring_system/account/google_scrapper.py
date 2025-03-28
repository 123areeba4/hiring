import requests
from bs4 import BeautifulSoup
import random

def scrape_experts(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ])
    }
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        
        for g in soup.find_all('div', class_='tF2Cxc'):
            title = g.find('h3').text if g.find('h3') else 'No Title'
            link = g.find('a')['href'] if g.find('a') else 'No Link'
            results.append({"title": title, "link": link})
        
        return results
    else:
        return None

# Example usage
experts = scrape_experts("Data Scientist Germany site:linkedin.com")
print(experts)