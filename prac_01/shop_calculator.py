total_price = 0
number_of_items = int(input('Number of items: '))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input('Price of item: '))
    total_price += item_price

if total_price > 100:
    discount = 0.10 * total_price   # 10% of total price
    total_price = total_price - discount

print("Total price for", number_of_items, 'items is $',
      "{:.2f}".format(total_price))
