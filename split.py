import pandas as pd

# Read in full dataset
diamonds = pd.read_csv('diamond_prices_2022.csv')

# Create holdout dataset
holdout = diamonds.sample(frac=0.2, random_state=200)

# Remove holdout items from full dataset
for index, diamond in holdout.iterrows():
   diamonds.drop(index=index, inplace=True)

# Reset indices
holdout.reset_index()
diamonds.reset_index()

# Validate shapes
print(holdout.shape)
print(diamonds.shape)

# Write to csv
holdout.to_csv('diamond_holdout.csv', index=False)
diamonds.to_csv('diamonds_without_holdout.csv', index=False)