fruits = ["apple", "banana", "mango", "grapes"]

fruits.append("orange")
fruits.remove("banana")

print(fruits)
print("Total fruits:", len(fruits))

for f in fruits:
    print("I like", f)