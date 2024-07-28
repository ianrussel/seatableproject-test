from seatable_api import Base
import os
import sys
from dotenv import load_dotenv
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
script_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=dotenv_path, override=True)



from main import generate_data

data = generate_data()
server_url = os.getenv('server_url')
api_token =os.getenv('api_token')
print(f" api token {api_token}")

# Initialize the base
base = Base(api_token, server_url)
base.auth()

# Table name
table_name = 'Test Analyzer'  # Replace with your actual table name
all_rows = base.list_rows(table_name)
# Iterate through the JSON data
for item in data:
    asin = item['ASIN']
    brand = item['Brand']

    # Search for the row by ASIN
    matching_rows = [row for row in all_rows if row.get('ASIN') == asin]

    if matching_rows:
        row_id = matching_rows[0]['_id']
        print(f" row id {row_id}")

        # Update the row with new Price and Number
        base.update_row(table_name, row_id, {
            'Brand': brand,
            'Package Quantity': item['Package Quantity'],
            'Unit Cost': '',
            'Category': item['Category'],
            'Est Sales': item['Est Sales'],
            'Buy Box Landed': item['Buy Box Landed'],
            'Lowest FBA': item['Lowest FBA'],
            'Lowest FBM': item['Lowest FBM'],
            'Sell Price': item['Sell Price'],
            'Referral Fee': item['Referral Fee'],
            'Fulfillment Subtotal': item['Fulfillment Subtotal'],
            'Package Dimensions': item['Package Dimensions'],
            'Package Weight': item['Package Weight'],
            'BuyBox Contention': item['BuyBox Contention'],
            'Avg Sales Rank 30d': item['Avg Sales Rank 30d'],
            'Avg Sales Rank 90d': item['Avg Sales Rank 90d'],
            'Avg Sales Rank 180d': item['Avg Sales Rank 180d'],
            'Avg Buybox 30d': item['Avg Buybox 30d'],
            'Avg Buybox 90d': item['Avg Buybox 90d'],
            'Avg Buybox 180d': item['Avg Buybox 180d'],
            'Amazon Seller InStock Rate 30d': item['Amazon Seller InStock Rate 30d'],
            'Amazon Seller InStock Rate 90d': item['Amazon Seller InStock Rate 90d'],
            'Amazon Seller InStock Rate 180d': item['Amazon Seller InStock Rate 180d'],
            'Variation Count': item['Variation Count'],
            'Is Top Level Category': int(item['Is Top Level Category']),
            'Is Hazmat': int(item['Is Hazmat']),
        })
        print(f"Updated row with ASIN {asin}: Brand={brand}")
    else:
        print(f"No row found with ASIN {asin}")

print("Update process completed.")
