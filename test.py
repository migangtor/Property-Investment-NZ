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
    properties = soup.find_all('a', class_='ember-view block h-full py-6 px-3 md:px-6 text-slateGrey-500')

    property_list = []
    
    for property in properties:
        address_element = property.find('h3', class_='mb-1 pr-3 text-base font-semibold capitalize text-black')
        address = address_element.get_text(strip=True)

        price_div = property.find('div', class_ = 'font-semibold leading-tight text-black text-xl.25 justify-start')
        price = price_div.contents[0].strip()
        # Extract the time period (e.g., "per week")
        time_period = price_div.find('span', class_='text-slateGrey-500 text-sm font-normal self-center').get_text(strip=True)

        rooms = property.find('div', class_='data-test="bedroom"')
        # Extract the href attribute (link)
        link = property.get('href')
        base_url = "https://www.realestate.co.nz"
        full_link = base_url + link        

        
        property_list.append({
            'Address': address,
            'Price': price,
            'Rent_frequency': time_period,
            'Rooms': rooms,
            'Link': link,
            'Full_link': full_link
        #   'Price': price
        })
    
    # Convert the list of properties to a DataFrame
    df = pd.DataFrame(property_list)
    
    # Display the DataFrame
    print(df)
    
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    


