import requests
from bs4 import BeautifulSoup
import csv

def flipkart_scraper(search_query, page_number):
    base_url = "https://www.flipkart.com/search?q="
    url = f"{base_url}{search_query}&page={page_number}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("div", class_="_1AtVbE")

        extracted_data = []

        for product in products:
            name_element = product.find("div", class_="_4rR01T")
            price_element = product.find("div", class_="_30jeq3")
            ratings_element = product.find("span", class_="_1lRcqv")

            name = name_element.text if name_element else "N/A"
            price = price_element.text if price_element else "N/A"
            ratings = ratings_element.text if ratings_element else "N/A"

            extracted_data.append({
                "Name": name,
                "Price": price,
                "Ratings": ratings
            })

        return extracted_data
    else:
        print(f"Error {response.status_code}: Unable to fetch the page.")

def save_to_csv(data, filename="flipkart_mobiles.csv"):
    keys = data[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    search_query = "iPhone"
    for page_number in range(1, 5):
        data = flipkart_scraper(search_query, page_number)
        if data:
            save_to_csv(data)
            print(f"Data extraction successful. Check {search_query.lower()}_mobiles.csv.")
        else:
            print("Data extraction failed.")
