def calculate_total(base_price, is_student=False):
    if base_price < 0:
        raise ValueError("base_price must be non-negative")

    tax_rate = 0.08
    total = base_price * (1 + tax_rate)
    return round(total, 2)
