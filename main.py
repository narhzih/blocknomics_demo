import requests

# Details to make API request
BLOCKONOMICS_API_URL = "https://www.blockonomics.co/api"
API_KEY = "<INSERT_API_KEY>"


# Function to get transaction output value
def get_transaction_output_value(txid, address):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(f"{BLOCKONOMICS_API_URL}/tx_detail?txid={txid}", headers=headers)

    if response.status_code != 200:
        return None

    transaction = response.json()

    for output in transaction.get('vout', []):
        if output['address'] == address:
            # Convert the amount from Satoshis to Bitcoins
            return output['value'] / 1e8

    return None


# Main function
def main():
    txid = input("Enter the Bitcoin transaction ID: ")
    address = input("Enter the Bitcoin address: ")

    output_value = get_transaction_output_value(txid, address)
    if output_value is not None:
        print(output_value)
    else:
        print("Transaction or Address not found in given transaction")


if __name__ == "__main__":
    main()
