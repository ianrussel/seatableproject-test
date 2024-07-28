from seatable_api import Base
from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

server_url = os.getenv('server_url')
api_token = os.getenv('api_token')


# Initialize the base
base = Base(api_token, server_url)
base.auth()

def calculate_package_volume(dimensions):
    """
    Calculate the volume of a package given its dimensions in a string format.

    Parameters:
    dimensions (str): The dimensions of the package in the format "length x width x height".

    Returns:
    float: The volume of the package.
    """
    # Extract the dimensions from the string
    length, width, height = map(float, dimensions.split(' x '))
    
    # Calculate the volume
    volume = length * width * height
    return volume

# Table name
table_name = 'Test Analyzer'  # Replace with your actual table name

# Iterate through each row
for row in base.list_rows(table_name):
    row_id = row.get('_id')
    print(f" row id {row_id}")
    package_dimensions = row.get('Package Dimensions')
    if package_dimensions:
        # Calculate the volume
        volume = calculate_package_volume(package_dimensions)
        constant = calculate_package_volume('40 x 48 x 72')
        result = constant / volume
        result = f"{result:,.2f}"
        print(f" volume {volume}")

        # Update the "Units in Pallete" field
        updated_data = {'Units in Pallete': str(result)}
        base.update_row(table_name,row_id,updated_data)

print("Updated Units in Pallete based on Package Dimensions")