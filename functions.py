def add(a, b):
    return a + b

def greet(name="stranger"):
    print(f"Hello {name}, welcome!")

result = add(10, 15)
print("Sum is", result)

greet()
greet("Priya")