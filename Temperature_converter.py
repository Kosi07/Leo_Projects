#Converting between °F and °C
while True:
 conversion = input(f"(type 'exit' to quit) Celsius OR Fahrenheit (C/F)?: ")

 if conversion.lower() == "exit":
    break

 elif conversion.lower() == "c":
    temp = float(input(f"Enter the temperature: "))

    result = (temp * 1.8) + 32
    print(f"This equals {round(result, 2)}°F")

 elif conversion.lower() == "f":
    temp = float(input(f"Enter the temperature: "))

    result = (temp - 32) / 1.8
    print(f"This equals {round(result, 2)}°C")

 else:
    print(f"Sorry, {conversion} seems to be invalid :(")