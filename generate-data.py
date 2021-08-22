import pandas as pd
import numpy as np
import datetime
import random
import calendar

products = {
  # Product: [Price, weight]
  'iPhone': [700, 10],
  'Google Phone': [600, 8],
  'Vareebadd Phone': [400, 3],
  '20in Monitor': [109.99, 6],
  '34in Ultrawide Monitor': [379.99, 9],
  '27in 4K Gaming Monitor': [389.99, 9],
  '27in FHD Monitor': [149.99, 11],
  'Flatscreen TV': [300, 7],
  'Macbook Pro Laptop': [1700, 7],
  'ThinkPad Laptop': [999.99, 6],
  'AA Batteries (4-pack)': [3.84, 30],
  'AAA Batteries (4-pack)': [2.99, 30],
  'USB-C Charging Cable': [11.95, 30],
  'Lightning Charging Cable': [14.95, 30],
  'Wired Headphones': [11.99, 26],
  'Bose SoundSport Headphones': [99.99, 19],
  'Apple Airpods Headphones': [150, 22],
  'LG Washing Machine': [600.00, 1],
  'LG Dryer': [600.00, 1]
}

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']

# Make the data frames
df = pd.DataFrame(columns=columns)

order_id = 143253

product_list = [product for product in products]
weights = [products[product][1] for product in products]

for i in range(1, 13):
    if i <= 10:
        order_amount = int(np.random.normal(loc=12000, scale=4000))

    if i == 11:
        #   make slightly higher
        order_amount = int(np.random.normal(loc=20000, scale=3000))

    if i == 12:
        #   make high value
        order_amount = int(np.random.normal(loc=26000, scale=3000))

    for j in range(order_amount):
        product = random.choices(product_list, weights=weights)[0]
        price = products[product][0]
        df.loc[j] = [order_id, product, 1, price, "NA", "NA"]
        order_id += 1

    month_value = calendar.month_name[i]
    df.to_csv(f"{month_value}_data.csv", index=False)
    break
