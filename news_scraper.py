import requests
from bs4 import BeautifulSoup

def get_political_headlines():
    """Scrapes political news headlines for satire content."""
    url = "https://www.politico.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = []
    for article in soup.find_all("h3"): 
        headlines.append(article.text.strip())

    return headlines[:5]

if __name__ == "__main__":
    print(get_political_headlines())
