import requests
import time
from bs4 import BeautifulSoup

url = "https://bitcoinwords.github.io/grants/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the required information
            amount = soup.find("div", {"class": "amount"}).text
            date_given = soup.find("div", {"class": "date-given"}).text
            amount_giver = soup.find("div", {"class": "amount-giver"}).text
            amount_receiver = soup.find("div", {"class": "amount-receiver"}).text
            purpose = soup.find("div", {"class": "purpose"}).text if soup.find("div", {"class": "purpose"}) else ""

            # Print the extracted information
            print("Amount:", amount)
            print("Date Given:", date_given)
            print("Amount Giver:", amount_giver)
            print("Amount Receiver:", amount_receiver)
            print("Purpose:", purpose)
            break
        elif response.status_code == 403:
            time.sleep(30)
        else:
            print("Request failed with status code", response.status_code)
            break
    except Exception as e:
        print("Request failed with error:", e)
        time.sleep(30)
