# Currency Converter - Simple Python Project
# Author: Sudip Sharma

# Conversion rates (as of example date)
conversion_rates = {
    "USD": 133.50,   # 1 USD = 133.50 NPR
    "EUR": 145.20,   # 1 EUR = 145.20 NPR
    "INR": 1.60,     # 1 INR = 1.60 NPR
}

print("=== Currency Converter ===")
print("Supported currencies: USD, EUR, INR")

currency = input("Enter currency code: ").upper()
amount = float(input(f"Enter amount in {currency}: "))

if currency in conversion_rates:
    npr_amount = amount * conversion_rates[currency]
    print(f"{amount} {currency} = {npr_amount:.2f} NPR")
else:
    print("Currency not supported.")
