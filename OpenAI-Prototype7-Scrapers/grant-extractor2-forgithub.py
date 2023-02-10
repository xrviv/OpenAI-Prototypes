import requests
import csv
from bs4 import BeautifulSoup

url = "https://bitcoinwords.github.io/grants/"

def analyze_page(url):
    # Make a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Look for a table
    table = soup.find("table")

    # If a table is found
    if table:
        # Get the header row
        header_row = [header.text.strip() for header in table.find("thead").find_all("th")]

        # Get the data rows
        data_rows = []
        for row in table.find("tbody").find_all("tr"):
            data_rows.append([cell.text.strip() for cell in row.find_all("td")])

        # Write the data to a CSV file
        with open("grants_data.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(header_row)
            writer.writerows(data_rows)

        # Print the data to the terminal
        print("Header row:", header_row)
        print("Data rows:")
        for row in data_rows:
            print(row)
    else:
        print("There is no table on this page.")

analyze_page(url)
