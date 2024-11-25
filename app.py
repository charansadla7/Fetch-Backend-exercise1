from flask import Flask, request, jsonify
import uuid
from datetime import datetime
import math

app = Flask(__name__)
receipts = {}

def calculate_points(receipt):
    points = 0

    # One point for every alphanumeric character in retailer name
    for char in receipt['retailer']:
        if char.isalnum():
            points+=1

    # 50 points if the total is a round dollar amount with no cents
    if float(receipt['total']).is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25 
    if float(receipt['total']) % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt
    total_pairs = len(receipt['items']) // 2
    points += total_pairs * 5

    # Points for items with trimmed descriptions as a multiple of 3
    for item in receipt['items']:
        description_length = len(item['shortDescription'].strip())
        if description_length % 3 == 0:
            item_price = float(item["price"])
            item_points = math.ceil(item_price * 0.2)  # Rounds up
            points += item_points

    # 6 points if the day in the purchase date is odd
    date_format = "%Y-%m-%d"
    purchase_date = datetime.strptime(receipt['purchaseDate'], date_format)
    if purchase_date.day % 2 == 1:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm
    time_format = "%H:%M"
    purchase_time = datetime.strptime(receipt['purchaseTime'], time_format)
    if purchase_time.hour>=14 and purchase_time.hour<16:
        points += 10

    return points


# API route to process a receipt and return an id
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt_data = request.get_json()

        # generate a unique id  for the receipts
        receipt_id = str(uuid.uuid4())

        # calculate points for the receipts
        points = calculate_points(receipt_data)

        # store the receipt data
        receipts[receipt_id] = receipt_data
        receipts[receipt_id]['points'] = points

        return jsonify({"id": receipt_id}), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

# API route to get points for a receipt by ID
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    receipt = receipts.get(receipt_id)

    if receipt:
        return jsonify({"points": receipt['points']}), 200
    else:
        return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
