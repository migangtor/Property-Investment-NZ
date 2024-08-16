import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for OneRoof NZ
url = 'https://www.realestate.co.nz/residential/rental/canterbury/christchurch-city'

# Set headers to mimic a real browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    

a_tag = soup.find('a', class_='paginated-items__page-number text-primaryBlue-500 cursor-pointer')

# Extract the text content
if a_tag:
    value = a_tag.get_text(strip=True)
    print(f"Extracted Value: {value}")
else:
    print("Element not found")