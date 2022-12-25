# Download html
# Find book elements
# Display book_name, book_rating (Sorted by rating)

import requests
from bs4 import BeautifulSoup as bs

pages = []

# Download html pages
print("Downloading HTML page...")

url = "https://www.goodreads.com/shelf/show/time-management"
r = requests.get(url)
html_page = r.text

elements = []

# Find book elements in all pages
print("Extracting elements...")

soup = bs(html_page, 'html.parser')
elements += soup.select('div[class~=elementList]>div[class~=left]')

books = []

print("Parsing elements...")
# Extract book name and rating from elements
for e in elements:
    book_name = e.select("[class~=bookTitle]")[0].text
    book_rating = e.select('[class~=greyText]')[-1].text.split('avg rating')[1].split(' ')[1]
    books.append({'name': book_name, 'rating': book_rating})

def display_book(book):
    print(f'{book["rating"]} {book["name"]} ')
# Display books sorted

def sort_by_rating(book):
    return book['rating']

books.sort(key=sort_by_rating)

for b in books:
    display_book(b)

