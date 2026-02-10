grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]
aisle = 5
new_word = dairy1 + ", " + dairy2 + ", " + bakery1
print(f"We have dairy and bakery items: {new_word} in aisle {aisle}")
