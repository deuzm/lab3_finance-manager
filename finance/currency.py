def get_currency_rate(from_label, to_label):

    rates = {
        "USD": 1,
        "RUB": 90,
        "BYN": 2.5
    }

    return rates[to_label] / rates[from_label]
