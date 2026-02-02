# Python script to demonstrate scraping a website and storing the data to a file
# NB: Make sure you've installed requests & beautifulsoup4 modules (pip install requests beautifulsoup4)

# Import the required modules
import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path

# 1. Set up a polite user agent string
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; X64) Salim-Learning-Scraper/1.0'
}

# 2. Specify the target URL (Website you wish to scrape)
url = "https://books.toscrape.com/"

# 3. Make the request
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"  # 👈 IMPORTANT : to get rid of weird character (Â)
except requests.exceptions.RequestException as errh:
    print(f"Request failed due to:\n{errh}")
    exit(1)

# 4. Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# ---------------------------------------------------------------
# 😁 Fun part now: Extract the data
# ===============================================================

books = soup.find_all("h3")
prices = soup.find_all("p",class_="price_color")

# Display the book titles
print("==============================================================================")
print("First 8 book titles")
print("------------------------------------------------------------------------------")
for book in books[:8]:
    title = book.a["title"]
    print(f"* {title}")

# Combine the titles and prices safely
print("\n==============================================================================")
print("The book titles & prices")
print("------------------------------------------------------------------------------")
book_data = []
for book, price in zip(books,prices):
    title = book.a["title"].strip()
    price_text = price.get_text(strip=True)
    book_data.append([title, price_text])
    print(f"* {title} — {price_text}")

# ---------------------------------------------------------------
# 💾 7. Save the data to a CSV file
# ===============================================================
# a. Build the path to the files folder where we'll save our scraped data
files_dir = Path.cwd().parent / "files"
files_dir.mkdir(exist_ok=True)

csv_path = files_dir /'scraped_books.csv'

# encoding='utf-8-sig' 👈 Here IMPORTANT : to get rid of weird characters and for CSV to Excel format
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Book Title", "Book Price"])
    writer.writerows(book_data)

# Inform the user the data's been saved
print(f"Saved {len(book_data)} books record in {csv_path}")

# Polite delay
time.sleep(1.5)