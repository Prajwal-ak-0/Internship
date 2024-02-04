import pandas as pd
import re

def clean_ingredients(ingredients):
    ingredients = re.sub(r'\([^)]*\)', '', ingredients)

    ingredients = re.split(r',(?![0-9])', ingredients)

    ingredients = [ingredient.strip() for ingredient in ingredients]

    ingredients = [ingredient for ingredient in ingredients if ':' not in ingredient]

    return ingredients


def format_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    formatted_data = pd.DataFrame(columns=['Name', 'Price', 'Ingredients'])

    for index, row in df.iterrows():
        cleaned_ingredients = clean_ingredients(row['Ingredients'])

        temp_df = pd.DataFrame({
            'Name': [row['Name']] * len(cleaned_ingredients),
            'Price': [row['Price']] * len(cleaned_ingredients),
            'Ingredients': cleaned_ingredients
        })

        formatted_data = pd.concat([formatted_data, temp_df])

    formatted_data.to_csv(output_csv, index=False)
    print(f'Data successfully written to {output_csv}')

input_csv_file = 'products_data.csv'
output_csv_file = 'formatted_products_data.csv'

format_data(input_csv_file, output_csv_file)
