import pandas as pd
import re
import logging

logging.basicConfig(level=logging.INFO)

def clean_ingredients(ingredients):
    try:
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
    except Exception as e:
        logging.error(f"Error cleaning ingredients: {e}")
        return None

def format_data(input_csv_files, output_csv):
    try:
        formatted_data = pd.DataFrame(columns=['Name', 'Price', 'Ingredients', 'Product_Link', 'Category','Rating','Total_Reviews'])

        # Mapping from file names to category names
        category_mapping = {
            'Pro1.csv': 'Moisturisers',
            'Pro2.csv': 'Cleansers',
            'Pro3.csv': 'Suncare',
            'Pro4.csv': 'Eye Creams',
            'Pro5.csv': 'Face Serums',
            'Pro6.csv': 'Face Mist',
            'Pro7.csv': 'Face Masks',
            'Pro8.csv': 'Toners',
            'Pro9.csv': 'Exfoliators',
            'Pro10.csv': 'Face Oils',
            'Pro11.csv': 'Water Mist',
        }

        for csv_file in input_csv_files:
            # Extract category from file name using the mapping
            category = category_mapping.get(csv_file, 'Unknown')  # Default to 'Unknown' if file name is not in the mapping

            df = pd.read_csv(csv_file)
            df['Category'] = category  # Add category column

            # Drop rows where 'Ingredients' column is empty
            df = df.dropna(subset=['Ingredients'])

            for index, row in df.iterrows():
                cleaned_ingredients = clean_ingredients(row['Ingredients'])

                if cleaned_ingredients is None:
                    continue

                for ingredient in cleaned_ingredients:
                    temp_df = pd.DataFrame({
                        'Name': [row['Name']],
                        'Price': [row['Price']],
                        'Ingredients': [ingredient],
                        'Product_Link': [row['Product_Link']],
                        'Category': [category],
                        'Rating': [row['Rating']],
                        'Total_Reviews': [row['Total_Reviews']],
                    })

                    formatted_data = pd.concat([formatted_data, temp_df], ignore_index=True)

        formatted_data.to_csv(output_csv, index=False)
        logging.info(f'Data successfully written to {output_csv}')
    except Exception as e:
        logging.error(f"Error formatting data: {e}")

# List of input CSV files
input_csv_files = ['Pro1.csv', 'Pro2.csv', 'Pro3.csv', 'Pro4.csv', 'Pro5.csv', 'Pro6.csv',
                   'Pro7.csv', 'Pro8.csv', 'Pro9.csv', 'Pro10.csv', 'Pro11.csv']
output_csv_file = 'merged_data.csv'

format_data(input_csv_files, output_csv_file)