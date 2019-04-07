from pyzomato import Pyzomato
import numpy as np
import pandas as pd
import json

#list of categories from Zomato
categories = {'categories': [{'categories': {'id': 1, 'name': 'Delivery'}}, {'categories': {'id': 2, 'name': 'Dine-out'}}, {'categories': {'id': 3, 'name': 'Nightlife'}}, {'categories': {'id': 4, 'name': 'Catching-up'}}, {'categories': {'id': 5, 'name': 'Takeaway'}}, {'categories': {'id': 6, 'name': 'Cafes'}}, {'categories': {'id': 7, 'name': 'Daily Menus'}}, {'categories': {'id': 8, 'name': 'Breakfast'}}, {'categories': {'id': 9, 'name': 'Lunch'}}, {'categories': {'id': 10, 'name': 'Dinner'}}, {'categories': {'id': 11, 'name': 'Pubs & Bars'}}, {'categories': {'id': 13, 'name': 'Pocket Friendly Delivery'}}, {'categories': {'id': 14, 'name': 'Clubs & Lounges'}}]}


print(categories)
#Convert it into a nice dataframe format
cat = categories['categories']
print(type(cat))
print(cat)
columns = ['id','name']
df = pd.DataFrame()

for i in cat:
    print(i['categories'])
    df = df.append(i['categories'], ignore_index=True)

print(df)

