import requests
from bs4 import BeautifulSoup
import pandas as pd  
import os
import time

url = 'https://news.ycombinator.com/'

print("Connecting to Hacker News...")
try:
    response = requests.get(url)
    response.raise_for_status() 
except Exception as e:
    print(f"Error connecting to site: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
stories = soup.find_all('span', class_='titleline')

data_rows = []

for story in stories:
    title = story.getText()
    link = story.find('a')['href']

    if 'python' in title.lower() or 'ai' in title.lower():
        data_rows.append({'Title': title, 'URL': link})

df = pd.DataFrame(data_rows)

df.to_csv('scraped_news.csv', index=False, encoding='utf-8')

html_content = f"""
<html>
<head>
    <title>Hacker News AI Monitor</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h1 class="mb-4">🚀 Latest AI & Python News</h1>
    <p class="text-muted">Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <div class="table-responsive">
        {df.to_html(classes='table table-hover table-striped', index=False, render_links=True)}
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("-" * 30)
print(f"SCRAPING COMPLETE!")
print(f"Found {len(data_rows)} stories. Website and CSV updated.")
print("-" * 30)
