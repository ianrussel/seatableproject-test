import pandas as pd
import json
import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
script_dir = os.path.dirname(os.path.abspath(__file__))

def generate_data():
    file_path = os.path.join(script_dir, 'Analyzer Test Task.xlsx')
    df = pd.read_excel(file_path)

    # Convert NaN values to None
    df = df.replace("", None)
    df = df.replace(r'^\s*$', "", regex=True)
    df = df.where(pd.notnull(df), None)
    df = df.drop(columns=['Column 1'])

    # Convert the DataFrame to a list of dictionaries (records)
    json_data = df.to_dict(orient='records')
    for record in json_data:
        for key, value in record.items():
            if pd.isna(value):
                record[key] = None


    # Convert the list of dictionaries to a JSON string with indentation
    json_str = json.dumps(json_data, indent=4)

    print(json_data)
    return json_data
