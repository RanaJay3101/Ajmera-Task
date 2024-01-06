# Flipkart Scraper

This Python script is a web scraper designed to extract product information from Flipkart based on a search query. It uses the `requests` library for making HTTP requests and `BeautifulSoup` for web scraping. The extracted data is then saved to a CSV file for further analysis or usage.

## Functions

### `flipkart_scraper(search_query, page_number)`

This function takes two parameters:
- `search_query`: The product you want to search for on Flipkart.
- `page_number`: The page number of the search results to scrape.

The function constructs a Flipkart search URL using the provided parameters, sends an HTTP request, and then parses the HTML to extract product information. It returns a list of dictionaries containing the extracted data (Name, Price, Ratings) for each product.

### `save_to_csv(data, filename="flipkart_mobiles.csv")`

This function takes two parameters:
- `data`: The extracted product information in the form of a list of dictionaries.
- `filename` (optional): The name of the CSV file to which the data will be saved. The default filename is `flipkart_mobiles.csv`, but you can customize it by modifying the `filename` parameter.

The function creates a CSV file and writes the header followed by the data rows.

## Usage

1. **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4
    ```

2. **Modify Search Query:**

    Open the `flipkart_scraper.py` script and modify the `search_query` variable to specify the product you want to search for on Flipkart.

3. **Run the Script:**

    ```bash
    python flipkart_scraper.py
    ```

    The script iterates through the specified number of pages and extracts product information using the `flipkart_scraper` function.

4. **Output:**

    The extracted data is saved to a CSV file named `flipkart_mobiles.csv` by default. You can change the filename by modifying the `filename` parameter in the `save_to_csv` function.

## Note

- Make sure to update the user-agent in the `headers` dictionary if necessary. The current user-agent mimics a Chrome browser on Windows.

- This script is a basic example and may require adjustments based on changes to Flipkart's website structure.

