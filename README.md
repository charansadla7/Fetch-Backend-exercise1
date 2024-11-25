# Fetch-Backend-exercise1
# Receipt Processor

This project implements a web service that processes receipts, calculates points based on specific rules, and provides an API to retrieve the points for a receipt. The service is built using Python and Flask and stores all data in memory.

## Features

1. **Process Receipts**: Accepts receipt data in JSON format and returns a unique ID for the receipt.
2. **Retrieve Points**: Provides the points calculated for a specific receipt using its unique ID.
## Prerequisites
- Python 3.8 or above
- `pip` (Python package installer)

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
 ## Install dependencies:
pip install -r requirements.txt
Run the Application

## Run the following command:

python app.py
Access the API locally at http://127.0.0.1:5000.


## Points Calculation Rules

- **Retailer Name**: 1 point for each alphanumeric character.
- **Round Dollar Amount**: 50 points if the total is a whole number.
- **Multiple of $0.25**: 25 points if the total is a multiple of $0.25.
- **Item Pairs**: 5 points for every 2 items on the receipt.
- **Item Description Length**: If the trimmed length of an item description is a multiple of 3, multiply the item price by 0.2, round up, and add the result to the points.
- **Odd Purchase Day**: 6 points if the purchase date is an odd day.
- **Afternoon Purchase Time**: 10 points if the time of purchase is between 2:00 PM and 4:00 PM.

## Example 1

## Input:

{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },
    {
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    }
  ],
  "total": "18.74"
}
## Output:

{
  "id": "12345678-1234-5678-1234-567812345678"
}
## Points Calculation:
Retailer Name: 6 points
Item Pairs: 5 points
Total: 11 points
