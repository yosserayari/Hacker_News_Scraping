import requests
from bs4 import BeautifulSoup
import csv
import os

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
        data_rows.append([title, link])

filename = 'scraped_news.csv'

file_path = os.path.join(os.getcwd(), filename)

with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'URL'])
    writer.writerows(data_rows)

print("-" * 30)
print(f"SCRAPING COMPLETE!")
print(f"Found {len(data_rows)} stories related to Python or AI.")
print(f"Your file is saved here: {file_path}")
print("-" * 30)

html_content = f"""
<html>
<head>
    <title>Hacker News AI Monitor</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h1>🚀 Latest AI & Python News</h1>
    <p>Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    {df.to_html(classes='table table-hover', index=False)}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
