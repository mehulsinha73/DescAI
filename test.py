import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=how+to+scrape+all+links+in+a+route"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# Find all <a> in your HTML that have a not null 'href'. Keep only 'href'.
links = [a["href"] for a in soup.find_all("a", href=True)]
print(
    [
        link
        if link.startswith("https://stackoverflow.com")
        else f"https://stackoverflow.com{link}"
        for link in links
        
    ]
)