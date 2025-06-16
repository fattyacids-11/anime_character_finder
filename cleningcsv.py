import pandas as pd
import numpy as np
import re
from datetime import datetime


# df= pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\merged_anime_character_traits.csv')

# # print(df.head())
# # print(df)

# ####removing duplicates
# # Check for duplicates based on character name
# duplicates = df[df.duplicated(subset=['character name'])]
# # print(f"Number of duplicate rows: {duplicates.shape[0]}")

# # Display the duplicates (optional, to inspect them before removal)
# # print(duplicates)

# # Remove duplicates based on character name
# df_cleaned = df.drop_duplicates(subset=['character name'], keep='first')

# # Verify the number of rows after removing duplicates
# # print(f"Number of rows after duplicate removal: {df_cleaned.shape[0]}")


# ############  order the rows
# # Add a temporary column to count non-null values per row
# df_cleaned['filled_count'] = df_cleaned.notnull().sum(axis=1)

# # Sort rows by 'filled_count' in descending order
# df_cleaned = df_cleaned.sort_values(by='filled_count', ascending=False)

# # Drop the 'filled_count' column after sorting
# df_cleaned = df_cleaned.drop(columns='filled_count').reset_index(drop=True)

# # Display the first few rows to confirm sorting
# # print(df_cleaned.head())


# ##### check unique valuesw and make them consistent

# # Check unique values in 'Hair Color'
# # unique_hair_colors = df_cleaned['Hair color'].unique()
# # print("Unique values in 'Hair Color':", unique_hair_colors)
# unique_hair_colors = df_cleaned['Hair color'].unique()
# # print("Unique values in 'Hair Color':", unique_hair_colors)




# # Save the cleaned data to a new CSV file
# # df_cleaned.to_csv('cleaned_data.csv', index=False)

# desired_hair_colors = [
#     'Black', 'Brown', 'Red', 'Gray', 'Red Hair', 'Grey Hair', 'White', 
#     'Brown Hair', 'Blonde Hair', 'Blue Hair', 'Black Hair', 'White Hair', 
#     'Orange Hair', 'Magenta Hair', 'Multicolored Hair', 'Blonde',
#     'Green Hair', 'Turquoise Hair', 'Purple Hair', 'Grey', 'Pink Hair', 
#     'Purple', 'Blue', 'Multicolored'
# ]

# # Convert NaN values to 'Unknown' or any other placeholder if necessary
# df_cleaned['Hair color'] = df_cleaned['Hair color'].fillna('Unknown')

# # Filter 'Hair Color' column to keep only values that match the list
# df_cleaned['Hair color'] = df_cleaned['Hair color'].apply(lambda x: x if x in desired_hair_colors else 'Other')

# # Display the cleaned 'Hair Color' column to verify results
# # print(df['Hair color'].unique())


# colors_to_replace = ["Black", "Brown", "Red", "Gray", "White", "Blonde", "Orange", "Green", "Blue", "Grey", "Pink", "Purple", "Multicolored"]

# # Apply the replacement to the 'Hair Color' column
# df_cleaned['Hair color'] = df_cleaned['Hair color'].apply(lambda x: f"{x} Hair" if x in colors_to_replace else x)

# # Display the modified column to verify results
# # print(df['Hair color'].unique())



# # Check unique values in 'Eye Color'
# unique_eye_colors = df_cleaned['Eye color'].unique()
# # print("Unique values in 'Eye Color':", unique_eye_colors)


# df_cleaned['Hair color'] = df_cleaned['Hair color'].str.title()
# df_cleaned['Gender'] = df_cleaned['Gender'].str.capitalize()


# blood_groups = ['A', 'B', 'O', 'AB']

# # Fill missing values in the 'Blood Group' column with random choices
# df_cleaned['Blood Type'] = df_cleaned['Blood Type'].apply(lambda x: x if pd.notna(x) else np.random.choice(blood_groups))


# # df_cleaned.to_csv('cleaned_data.csv', index=False)
# import ast
# def convert_to_list(tag_string):
#     if pd.notnull(tag_string):
#         try:
#             # If it's already a list (e.g., "['tag1', 'tag2']")
#             tag_list = ast.literal_eval(tag_string)
#             if isinstance(tag_list, list):
#                 return tag_list
#         except (ValueError, SyntaxError):
#             pass  # Not in a list format, handle below

#         # Split by commas for non-list strings
#         tags = [tag.strip() for tag in tag_string.split(',')]
#         return tags
#     return []  # For null values, return an empty list

# # Apply the function to the 'tags' column
# df_cleaned['tags'] = df_cleaned['tags'].apply(convert_to_list)

# # Print the updated DataFrame
# print(df_cleaned)

# # Count rows where 'tags' is not null
# # non_null_count = df_cleaned['tags'].notnull().sum()

# # print(f"Number of rows with non-null tags: {non_null_count}")
# # Count rows where 'tags' is an empty list
# # empty_tags_count = df_cleaned['tags'].apply(lambda x: isinstance(x, list) and len(x) == 0).sum()

# # print(f"Number of rows with empty tags: {empty_tags_count}")

# # Drop rows where 'tags' is an empty list
# df_cleaned = df_cleaned[~df_cleaned['tags'].apply(lambda x: isinstance(x, list) and len(x) == 0)]

# # Reset the index if needed
# df_cleaned.reset_index(drop=True, inplace=True)

# print(f"Number of rows remaining: {len(df_cleaned)}")


# # import re

# # def is_anime_name(tag_list):
# #     """
# #     Determines if the given tag list is likely an anime name.
# #     """
# #     if isinstance(tag_list, list) and len(tag_list) == 1:
# #         entry = tag_list[0]
        
# #         # Check for multiple spaces or absence of commas
# #         if re.search(r'\s{2,}', entry) or ',' not in entry:
# #             return True
        
# #         # Check for only one set of quotes in the entire string
# #         if re.match(r'^[\'\"].*[\'\"]$', entry) and entry.count('\'') + entry.count('\"') == 2:
# #             return True
    
# #     return False

# # # Apply the function and filter out anime names
# # df_cleaned = df_cleaned[~df_cleaned['tags'].apply(is_anime_name)]

# # # Reset index
# # df_cleaned.reset_index(drop=True, inplace=True)

# # print(f"Number of rows after removing anime names: {len(df_cleaned)}")



# def contains_multiple_spaces(tag_list):
#     """
#     Checks if any tag in the list contains more than one space.
#     """
#     for tag in tag_list:
#         if tag.count(" ") > 1:  # More than one space in a tag
#             return True
#     return False

# # Filter out rows where any tag has more than one space
# df_cleaned = df_cleaned[~df_cleaned['tags'].apply(contains_multiple_spaces)].reset_index(drop=True)




# # Flatten the list of lists and extract unique tags
# #####################
# # unique_tags = set(tag for tag_list in df_cleaned['tags'] for tag in tag_list)

# # # Print the unique tags
# # print("Unique tags:", unique_tags)
# ###############################
# # Drop rows where the 'anime' column is empty
# df_cleaned = df_cleaned[df_cleaned['Anime'].notnull() & (df_cleaned['Anime'].str.strip() != '')]

# # Reset the index for the resulting DataFrame
# df_cleaned.reset_index(drop=True, inplace=True)

# # Check the updated DataFrame
# # print(df_cleaned)


# # df_cleaned.to_csv('cleaned_data.csv', index=False)


# unique_tags = set(tag for tag_list in df_cleaned['tags'] for tag in tag_list)

# Print the unique tags
# print("Unique tags:", unique_tags)

manga_df = pd.read_csv(r"D:\sem 3\pai\PAI PROJECT\archive (1)\manga.csv")


manga_df = manga_df.dropna(subset=["published_from"])

manga_df.to_csv(r'D:\sem 3\pai\PAI PROJECT\archive (1)\manga.csv')







