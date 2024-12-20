import re

# Credit card types based on their number patterns and lengths
card_types = {
    "MasterCard": {
        "prefixes": ["51", "52", "53", "54", "55"],
        "length": 16
    },
    "Visa": {
        "prefixes": ["4"],
        "length": [13, 16]
    },
    "American Express": {
        "prefixes": ["34", "37"],
        "length": 15
    },
    "Diners Club": {
        "prefixes": ["30", "36", "38", "39"],
        "length": 14
    },
    "Discover": {
        "prefixes": ["6011", "622126", "622925", "644", "645", "646", "647", "648", "649", "65"],
        "length": 16
    },
    "EnRoute": {
        "prefixes": ["2014", "2149"],
        "length": 15
    },
    "JCB": {
        "prefixes": ["35"],
        "length": 16
    },
    "Voyager": {
        "prefixes": ["8699"],
        "length": 15
    },
    "Hipercard": {
        "prefixes": ["6062"],
        "length": 16
    },
    "Aura": {
        "prefixes": ["50"],
        "length": 16
    }
}

# Luhn Algorithm to validate card number
def luhn_check(card_number):
    card_number = [int(digit) for digit in str(card_number)]
    checksum = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            checksum += doubled - 9 if doubled > 9 else doubled
        else:
            checksum += digit
    return checksum % 10 == 0

# Function to identify the card type
def identify_card(card_number):
    card_number_str = str(card_number)
    
    # First validate using Luhn algorithm
    if not luhn_check(card_number_str):
        return "Invalid Card Number"
    
    # Check card type by prefix and length
    for card_type, rules in card_types.items():
        valid_lengths = rules["length"] if isinstance(rules["length"], list) else [rules["length"]]
        
        # Check for the correct length
        if len(card_number_str) not in valid_lengths:
            continue
        
        # Check for valid prefixes
        for prefix in rules["prefixes"]:
            if card_number_str.startswith(prefix):
                return card_type
    
    return "Unknown Card Type"

# Test the function with different card numbers
card_numbers = [
    "5105105105105100",  # MasterCard
    "4111111111111111",  # Visa
    "378282246310005",   # American Express
    "30371582913439",    # Diners Club
    "6011514433546201",  # Discover
    "214982557722452",   # EnRoute
    "3530111333300000",  # JCB
    "869926696784160",   # Voyager
    "6062829412390357",  # Hipercard
    "5058004265970469"   # Aura
]

# Output the results
for card in card_numbers:
    card_type = identify_card(card)
    print(f"Card Number: {card} | Card Type: {card_type}")
