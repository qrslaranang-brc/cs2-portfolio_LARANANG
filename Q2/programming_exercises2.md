# Exercise 1
items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[4])

print(items[0])
print(items[4])


# Exercise 2
places = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

for p in places:
    print(p)

print(places[1:4])

s = input("Search: ")
print(s in places)

places[2] = "Iloilo"
print(places)
