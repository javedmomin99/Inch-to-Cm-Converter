print("Welcome to the Inch to Cm Converter")
inputs = int(input("Please enter your number in Inch\nInch = "))
def numbers(num):
    inch_to_cm = float(num * 2.54)
    return inch_to_cm
a = (numbers(inputs))
print(f"{inputs} Inch = {a} cm")

