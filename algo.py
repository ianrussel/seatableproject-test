import pandas as pd
""" percentage if no competitor"""
max_price_percent_nc = 0.010  # in percent if no competitot
min_price_percent_nc = 0.05  # in percent if no competitor

"""percentage if theres a competitor"""
max_price_percent = 0.02
min_price_percent = 0.02


lower_percentage = 0.02  # just an example to lower our min price verson our competitor
higher_percentage = 0.05  # just an example to add price more than our competitor


def get_sales_price(referral_fee, buy_cost, fba_fee, lowest_fba):
    """
    Calculate the selling price based on the referral fee percentage, buy cost, and FBA fee.

    Parameters:
    referral_fee (float): The referral fee as a percentage.
    buy_cost (float): The buy cost of the item.
    fba_fee (float): The FBA fee for the item.

    Returns:
    float: The calculated selling price.
    """
    referral_fee_amount = buy_cost * referral_fee
    max_price = 0
    min_price = 0
    scale = 5  # default to sells as fastest

    # Calculate the Selling Price
    selling_price = buy_cost + referral_fee_amount + fba_fee
    if pd.isna(lowest_fba):
        """ 
        theres no competitor
        set the max price
        """
        max_price = selling_price * (1 + max_price_percent_nc)
        min_price = selling_price * (1 + min_price_percent_nc)
        scale = 1  # maximise profit as we  have no compititor
    else:
        if lowest_fba > selling_price:
            """ our competitor is more pricey than our product based on floor price, s"""

            min_price = lowest_fba * (1 - min_price_percent)

            max_price = lowest_fba * (1 + max_price_percent)
        else:
            """ our competitor has lower price, no need to complete"""

            max_price = selling_price * (1 + higher_percentage)
            min_price = selling_price * (1 + lower_percentage)

    return selling_price, scale, max_price, min_price


# Load the uploaded Excel file
file_path = 'Sales Report.xlsx'
excel_data = pd.ExcelFile(file_path)
df = pd.read_excel(file_path, sheet_name='Main Report_Default View')

# Apply the updated function to the DataFrame
df[['Floor Selling Price', 'Soft - Strong Scale', 'New Max', 'New Min']] = df.apply(
    lambda row: get_sales_price(row['Referral Fee'], row['Buy Cost'], row['FBA Fee'], row['Lowest FBA']), axis=1, result_type='expand'
)
df['Floor Selling Price'] = df['Floor Selling Price'].round(2)
df['New Max'] = df['New Max'].round(2)
df['New Min'] = df['New Min'].round(2)
column_order = df.columns.tolist()
asin_index = column_order.index('ASIN')
new_column_order = column_order[:asin_index + 1] + ['Floor Selling Price'] + \
    column_order[asin_index + 1:-3] + \
    ['Soft - Strong Scale', 'New Max', 'New Min']

# Reorder the DataFrame columns
df = df[new_column_order]
# Save the updated DataFrame back to an Excel file with a different filename
output_file_path_function = 'Sales_Report_Updated.xlsx'
df.to_excel(output_file_path_function,
            sheet_name='Updated Report', index=False)
