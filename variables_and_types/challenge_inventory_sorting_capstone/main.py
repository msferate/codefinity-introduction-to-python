# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[:11]
category2 = categories[13:]

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have " + candy1.lower().capitalize() + " for " + bubblegum_price + " in the " + category1.lower())
print("We have " + candy2.lower().capitalize() + " for " + chocolate_price + " in the " + category1.lower())
print("We have " + dry_goods.lower().capitalize() + " for " + pasta_price + " in the " + category2.lower())