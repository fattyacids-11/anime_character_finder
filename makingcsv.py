import pandas as pd

# Load all datasets
dataset_1 = pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\character\anime_heights.csv')  # Change path to your file
dataset_2 = pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\character\Anime_Triats.csv')  # Change path
dataset_3 = pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\character\characters_metadata.csv')  # Change path
dataset_4 = pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\character\characters.csv')  # Change path
# dataset_5 = pd.read_csv(r'D:\sem 3\pai\PAI PROJECT\character\top_anime_characters_cleaned.csv')  # Change path

# Inspect datasets to identify the common columns (e.g., character name or id)
# We'll use 'character_name' for this example, adjust based on your datasets.
datasets = [dataset_1, dataset_2, dataset_3, dataset_4]

# Merge datasets on the 'character_name' column (you might need to adjust column names)
merged_data = datasets[0]
for df in datasets[1:]:
    merged_data = pd.merge(merged_data, df, on='character name', how='outer')

# Optionally, remove duplicate characters, if any
merged_data.drop_duplicates(subset='character name', keep='first', inplace=True)

# Fill missing values with NaN (if you want to keep them empty)
# You can also use 'N/A' or 'Unknown' if you prefer
merged_data.fillna(value=pd.NA, inplace=True)

# Save the merged dataset to a new CSV file
merged_data.to_csv('merged_anime_character_traits.csv', index=False)

print("Merged dataset created successfully!")
