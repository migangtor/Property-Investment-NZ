import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for OneRoof NZ
url = 'https://www.oneroof.co.nz/search/houses-for-sale/suburb_mount-wellington-auckland-city-2583_page_1'

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
    
    # Extract data - this part will depend on the specific structure of the page
    # For demonstration, let's assume we're extracting property titles and prices
    properties = soup.find_all('div', class_='space-y-8 flex flex-col justify-center flex-1 lg:space-y-10')
    
    property_list = []
    
    for property in properties:
        title = property.find('address').get_text(strip=True)
        #price = property.find('div', class_='PropertyCard__Price').get_text(strip=True)
        
        property_list.append({
            'Title': title
        #,
        #   'Price': price
        })
    
    # Convert the list of properties to a DataFrame
    df = pd.DataFrame(property_list)
    
    # Display the DataFrame
    print(df)
    
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

