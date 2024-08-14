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
    
    # Extract data - this part will depend on the specific structure of the page
    # For demonstration, let's assume we're extracting property titles and prices
    properties = soup.find_all('div', class_='tile__listing-details md:border-slateGrey-200 md:border-b md:pb-4')

    property_list = []
    
    for property in properties:
        title = property.find('h3', class_ = 'mb-1 pr-3 text-base font-semibold capitalize text-black')
        price_div = property.find('div', class_ = 'font-semibold leading-tight text-black text-xl.25 justify-start')
        price = price_div.contents[0].strip()
        # Extract the time period (e.g., "per week")
        time_period = price_div.find('span', class_='text-slateGrey-500 text-sm font-normal self-center').get_text(strip=True)

        rooms = property.find('div', class_='data-test="bedroom"')

        
        property_list.append({
            'Title': title,
            'Price': price,
            'Rent_frequency': time_period,
            'Rooms': rooms,
        #   'Price': price
        })
    
    # Convert the list of properties to a DataFrame
    df = pd.DataFrame(property_list)
    
    # Display the DataFrame
    print(df)
    
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

