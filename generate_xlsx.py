import pandas as pd
import json

output_file = "extracted_product_details.xlsx"

writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

df = pd.read_json('extracted_product_details.json')
data = df.to_dict(orient='records')
# Iterate through each page and create a sheet for each
for page in data:
    sheet_name = page["page"]
    contents = page["contents"]
    df = pd.DataFrame(contents)
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the excel file
writer.close()