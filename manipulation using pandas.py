import pandas as pd

# 1. Create a "DataFrame" (a table) from scratch
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 18, 45, 29],
    'City': ['New York', 'London', 'London', 'Paris', 'New York'],
    'Sales': [250, 400, 150, 600, 300]
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# 2. Filtering: Get only the people from London
london_team = df[df['City'] == 'London']
print("\n--- London Team Only ---")
print(london_team)

# 3. Sorting: Sort by Age (youngest to oldest)
sorted_df = df.sort_values(by='Age')
print("\n--- Sorted by Age ---")
print(sorted_df)

# 4. Aggregation: Find the total sales per city
city_sales = df.groupby('City')['Sales'].sum()
print("\n--- Total Sales by City ---")
print(city_sales)

# 5. Adding a Column: Add a 'Bonus' (10% of sales)
df['Bonus'] = df['Sales'] * 0.10
print("\n--- Data with Bonus Column ---")
print(df)
