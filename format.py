import pandas as pd
import re

def clean_ingredients(ingredients):
    # Condition 1: Neglecting parts containing word followed by ":"
    match = re.match(r'\b\w+:\s*', ingredients)
    if match:
        ingredients = ingredients[len(match.group(0)):]

    # Condition 2: Neglecting content inside brackets
    ingredients = re.sub(r'\([^)]*\)', '', ingredients)

    # Condition 3: Handling numbers and commas
    ingredients = re.sub(r'(\d),(\d)', r'\1\2', ingredients)

    # Condition 4: Handling extra white spaces
    ingredients = re.split(r',(?![0-9])', ingredients)
    ingredients = [re.sub(r'\s+', ' ', ingredient.strip()) for ingredient in ingredients]

    # Remove empty strings
    ingredients = [ingredient for ingredient in ingredients if ingredient]

    return ingredients

def format_data(input_csv_files, output_csv):
    formatted_data = pd.DataFrame(columns=['Name', 'Price', 'Ingredients', 'Product_Link', 'Category'])

    for csv_file in input_csv_files:
        df = pd.read_excel(csv_file)

        # Check if 'Ingredients' column exists in the DataFrame
        if 'Ingredients' in df.columns:
            # Drop rows where 'Ingredients' column is empty
            df = df.dropna(subset=['Ingredients'])

            for index, row in df.iterrows():
                cleaned_ingredients = clean_ingredients(row['Ingredients'])

                for ingredient in cleaned_ingredients:
                    temp_df = pd.DataFrame({
                        'Name': [row['Name']],
                        'Price': [row['Price']],
                        'Ingredients': [ingredient],
                        'Product_Link': [row['Product_Link']],
                        'Category': [row['Category']],
                    })

                    formatted_data = pd.concat([formatted_data, temp_df], ignore_index=True)

        else:
            print(f"'Ingredients' column not found in {csv_file}")

    formatted_data.to_csv(output_csv, index=False)
    print(f'Data successfully written to {output_csv}')

input_csv_files = ['product.xlsx']
output_csv_file = 'formatted_data_2.csv'
format_data(input_csv_files, output_csv_file)