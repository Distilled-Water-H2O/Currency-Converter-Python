def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another.
    
    Args:
        amount (float): The amount to be converted
        from_currency (str): The currency code of the input amount
        to_currency (str): The currency code to convert to
        rates (dict): A dictionary containing currency exchange rates
    
    Returns:
        float: The converted amount
    """
    if from_currency not in rates or to_currency not in rates:
        return "Invalid currency code!"
    
    # Convert the amount to USD first
    amount_in_usd = amount / rates[from_currency]
    
    # Convert the USD amount to the target currency
    converted_amount = amount_in_usd * rates[to_currency]
    
    return round(converted_amount, 2)

# Sample exchange rates (1 USD = x currency)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.81,
    "JPY": 133.65,
    "AUD": 1.48,
    "CAD": 1.35,
    "CHF": 0.92,
    "CNY": 6.51,
    "HKD": 7.85,
    "NZD": 1.58,
    "INR": 83.45
}

print("Currency Converter")

while True:
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency code of the input amount: ").upper()
    to_currency = input("Enter the currency code to convert to: ").upper()
    
    result = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} = {result} {to_currency}")