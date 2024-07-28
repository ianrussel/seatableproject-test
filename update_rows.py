import requests
import urllib.parse

# Replace these with your Seatable API details
ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0MTIwNDYsImR0YWJsZV91dWlkIjoiZTA3NTQ0MWMtYTQwMi00MDdkLTgxMjMtMTJlZTdiYzM4MWE4IiwicGVybWlzc2lvbiI6InJ3Iiwib3JnX2lkIjozNDA1MSwib3duZXJfaWQiOiI1NzRiNDM5MGY2OTk0MjU0ODU2YjQ1ZDQxOWJlYmY3OEBhdXRoLmxvY2FsIiwiYXBwX25hbWUiOiJ0ZXN0LWFwcCIsInVzZXJuYW1lIjoiIiwiaWRfaW5fb3JnIjoiIiwidXNlcl9kZXBhcnRtZW50X2lkc19tYXAiOnsiY3VycmVudF91c2VyX2RlcGFydG1lbnRfaWRzIjpbXSwiY3VycmVudF91c2VyX2RlcGFydG1lbnRfYW5kX3N1Yl9pZHMiOltdfX0.4C48zBARoDUx0cjdfKkFfPloqHcxQ8UaY_QzrJuzNLI'
BASE_URL = 'https://cloud.seatable.io/api-gateway/api/v2/dtables'
BASE_ID = 'e075441c-a402-407d-8123-12ee7bc381a8'
TABLE_NAME = 'Test Analyzer'
COLUMN_NAME = 'Brand'
NEW_VALUE = 'Apple'


data = [{'ASIN': 'B00000DM99', 'Product ID': 'B00000DM99', 'Brand': 'Energizer', 'Package Quantity': 1, 'Category': 'Health & Household', 'Est Sales': 332, 'Buy Box Landed': 4.58, 'Lowest FBA': 4.58, 'Lowest FBM': 4.52, 'Sell Price': 4.58, 'Referral Fee': 0.69, 'Fulfillment Subtotal': 2.46, 'Package Dimensions': '4.17 x 3.66 x 0.55', 'Package Weight': 0.11, 'New FBA Offers': 2, 'BuyBox Contention': 2, 'Avg Sales Rank 30d': 53100, 'Avg Sales Rank 90d': 40720, 'Avg Sales Rank 180d': 22529, 'Avg Buybox 30d': 4.52, 'Avg Buybox 90d': 4.06, 'Avg Buybox 180d': 3.87, 'Amazon Seller InStock Rate 30d': '100%', 'Amazon Seller InStock Rate 90d': '100%', 'Amazon Seller InStock Rate 180d': '100%', 'Variation Count': 4, 'Is Top Level Category': True, 'Is Hazmat': False}, {'ASIN': 'B00000IS6G', 'Product ID': 'B00000IS6G', 'Brand': 'Radio Flyer', 'Package Quantity': 1, 'Category': 'Toys & Games', 'Est Sales': 1039, 'Buy Box Landed': 119.99, 'Lowest FBA': 119.99, 'Lowest FBM': 139.99, 'Sell Price': 119.99, 'Referral Fee': 18.0, 'Fulfillment Subtotal': 25.64, 'Package Dimensions': '37.50 x 18.00 x 5.00', 'Package Weight': 29.2, 'New FBA Offers': 1, 'BuyBox Contention': 1, 'Avg Sales Rank 30d': 13597, 'Avg Sales Rank 90d': 12807, 'Avg Sales Rank 180d': 11436, 'Avg Buybox 30d': 119.98, 'Avg Buybox 90d': 119.98, 'Avg Buybox 180d': 119.98, 'Amazon Seller InStock Rate 30d': '100%', 'Amazon Seller InStock Rate 90d': '100%', 'Amazon Seller InStock Rate 180d': '100%', 'Variation Count': 3, 'Is Top Level Category': True, 'Is Hazmat': False}, {'ASIN': 'B00000IS6S', 'Product ID': 'B00000IS6S', 'Brand': 'Radio Flyer', 'Package Quantity': 1, 'Category': 'Toys & Games', 'Est Sales': 132, 'Buy Box Landed': 159.99, 'Lowest FBA': 159.99, 'Lowest FBM': 211.48, 'Sell Price': 159.99, 'Referral Fee': 24.0, 'Fulfillment Subtotal': 26.99, 'Package Dimensions': '38.00 x 15.25 x 6.00', 'Package Weight': 32.15, 'New FBA Offers': 1, 'BuyBox Contention': 1, 'Avg Sales Rank 30d': 108925, 'Avg Sales Rank 90d': 176431, 'Avg Sales Rank 180d': 191820, 'Avg Buybox 30d': 178.59, 'Avg Buybox 90d': 183.84, 'Avg Buybox 180d': 196.24, 'Amazon Seller InStock Rate 30d': '100%', 'Amazon Seller InStock Rate 90d': '57%', 'Amazon Seller InStock Rate 180d': '42%', 'Variation Count': 0, 'Is Top Level Category': True, 'Is Hazmat': False}, {'ASIN': 'B00000J47F', 'Product ID': 'B00000J47F', 'Brand': 'Energizer', 'Package Quantity': 1, 'Category': 'Health & Household', 'Est Sales': 5, 'Buy Box Landed': 12.04, 'Lowest FBA': None, 'Lowest FBM': 12.04, 'Sell Price': 12.04, 'Referral Fee': 1.81, 'Fulfillment Subtotal': 3.44, 'Package Dimensions': '4.21 x 3.70 x 0.70', 'Package Weight': 0.13,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'New FBA Offers': 0, 'BuyBox Contention': 1, 'Avg Sales Rank 30d': 518112, 'Avg Sales Rank 90d': 492947, 'Avg Sales Rank 180d': 420752, 'Avg Buybox 30d': 11.94, 'Avg Buybox 90d': 11.68, 'Avg Buybox 180d': 11.84, 'Amazon Seller InStock Rate 30d': '0%', 'Amazon Seller InStock Rate 90d': '0%', 'Amazon Seller InStock Rate 180d': '0%', 'Variation Count': 0, 'Is Top Level Category': True, 'Is Hazmat': False}, {'ASIN': 'B00000J47J', 'Product ID': 'B00000J47J', 'Brand': 'Energizer', 'Package Quantity': 2, 'Category': 'Health & Household', 'Est Sales': 5, 'Buy Box Landed': 14.99, 'Lowest FBA': None, 'Lowest FBM': 14.99, 'Sell Price': 14.99, 'Referral Fee': 2.25, 'Fulfillment Subtotal': 4.18, 'Package Dimensions': '4.20 x 3.80 x 1.00', 'Package Weight': 0.05, 'New FBA Offers': 0, 'BuyBox Contention': 1, 'Avg Sales Rank 30d': 454284, 'Avg Sales Rank 90d': 326456, 'Avg Sales Rank 180d': 270706, 'Avg Buybox 30d': 16.52, 'Avg Buybox 90d': 14.49, 'Avg Buybox 180d': 14.56, 'Amazon Seller InStock Rate 30d': '0%', 'Amazon Seller InStock Rate 90d': '0%', 'Amazon Seller InStock Rate 180d': '0%', 'Variation Count': 2, 'Is Top Level Category': True, 'Is Hazmat': False}, {'ASIN': 'B00000J47O', 'Product ID': 'B00000J47O', 'Brand': 'Energizer', 'Package Quantity': 2, 'Category': 'Health and Beauty', 'Est Sales': 5, 'Buy Box Landed': 18.99, 'Lowest FBA': None, 'Lowest FBM': 18.99, 'Sell Price': 18.99, 'Referral Fee': 2.85, 'Fulfillment Subtotal': 4.17, 'Package Dimensions': '2.70 x 2.30 x 1.00', 'Package Weight': 0.2, 'New FBA Offers': 0, 'BuyBox Contention': 1, 'Avg Sales Rank 30d': 851532, 'Avg Sales Rank 90d': 834011, 'Avg Sales Rank 180d': 813046, 'Avg Buybox 30d': 21.98, 'Avg Buybox 90d': 21.98, 'Avg Buybox 180d': 21.98, 'Amazon Seller InStock Rate 30d': '0%', 'Amazon Seller InStock Rate 90d': '0%', 'Amazon Seller InStock Rate 180d': '0%', 'Variation Count': 0, 'Is Top Level Category': False, 'Is Hazmat': False}, {'ASIN': 'B00000JGN9', 'Product ID': 'B00000JGN9', 'Brand': 'Energizer', 'Package Quantity': 1, 'Category': 'Health & Household', 'Est Sales': 5, 'Buy Box Landed': None, 'Lowest FBA': 13.45, 'Lowest FBM': 18.99, 'Sell Price': 13.45, 'Referral Fee': 2.02, 'Fulfillment Subtotal': 3.44, 'Package Dimensions': '4.40 x 4.00 x 0.70', 'Package Weight': 0.1, 'New FBA Offers': 1, 'BuyBox Contention': 0, 'Avg Sales Rank 30d': 398461, 'Avg Sales Rank 90d': 289880, 'Avg Sales Rank 180d': 307738, 'Avg Buybox 30d': 0.0, 'Avg Buybox 90d': 14.37, 'Avg Buybox 180d': 13.94, 'Amazon Seller InStock Rate 30d': '0%', 'Amazon Seller InStock Rate 90d': '0%', 'Amazon Seller InStock Rate 180d': '2%', 'Variation Count': 0, 'Is Top Level Category': True, 'Is Hazmat': False}]


# URL =  f'{BASE_URL}/api-gateway/api/v2/dtable/{BASE_ID}/rows/'
URL = "https://cloud.seatable.io/api-gateway/api/v2/dtables/e075441c-a402-407d-8123-12ee7bc381a8/rows/?table_name=Test%20Analyzer"

print(URL)
# print(pfu)
def get_headers():
    return {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

def get_table_metadata():
    url = f'{BASE_URL}/{BASE_ID}/metadata/'
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()['metadata']

def get_rows():
   
    params = {
        'table_name': TABLE_NAME
    }
    encoded_params = urllib.parse.urlencode(params).replace('+', '%20')
    print(f" encode {encoded_params}")
   
    response = requests.get(URL, headers=get_headers())
    response.raise_for_status()
    return response.json()['rows']

def map_columns(rows, column_mappings):
    mapped_rows = []
    for row in rows:
        mapped_row = {}
        for col_id, value in row.items():
            col_name = column_mappings.get(col_id, col_id)
            mapped_row[col_name] = value
        mapped_rows.append(mapped_row)
    return mapped_rows

def update_row(row_id, column_key, value):
    print(f" column {column_key} value {value}")
    data = {
        'row_id': row_id,
        'table_name': TABLE_NAME,
        'row': {
            'N745': value
        }
    }
    url = "https://cloud.seatable.io/api-gateway/api/v2/dtables/e075441c-a402-407d-8123-12ee7bc381a8/rows/"
    response = requests.put(url, headers=get_headers(), json=data)
    response.raise_for_status()
    print(f" response {response.text}")
    return response.json()

def main():
    import json
    metadata = get_table_metadata()
   
    columns = metadata['tables'][0]['columns']
    column_mappings = {col['key']: col['name'] for col in columns}

    all_rows = get_rows()
    all_rows_mapped = map_columns(all_rows, column_mappings)
    with open('allrows.json', 'w') as file:
        json.dump(metadata, file, indent = 4)
    for item in data[0:1]:
        asin = item['ASIN']
        brand = item['Brand']

        # Search for the row by ASIN
        matching_rows = [row for row in all_rows_mapped if row.get('ASIN') == asin]
        print(f" matching row {matching_rows}")
        if matching_rows:
            row_id = matching_rows[0]['_id']
            print(f"row {row_id}")
            update_row(row_id, COLUMN_NAME, NEW_VALUE)

    # for row in all_rows['rows']:
    #     print(f" row {row}")
        # row_id = row['_id']
        # print(f" row {row_id}")
        # update_row(row_id, COLUMN_NAME, NEW_VALUE)
        # print(f'Updated row {row_id} row {row}')

if __name__ == '__main__':
    main()
