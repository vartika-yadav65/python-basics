try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Bruh you can't divide by zero")
except ValueError:
    print("That's not even a number")
finally:
    print("Program ended")