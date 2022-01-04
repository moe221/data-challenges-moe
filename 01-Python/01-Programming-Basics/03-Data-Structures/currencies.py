# pylint: disable=missing-docstring

dict_keys = ["USDEUR", "GBPEUR", "CHFEUR", "EURGBP"]
ditc_values = [0.85, 1.13, 0.86, 0.885]
RATES = dict(zip(dict_keys, ditc_values))

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    rate = RATES.get(f"{amount[1]}{currency}", None)
    if rate is None:
        return None
    return round(rate * amount[0])
