def calculate_total(base_price, is_student=False):
    if base_price < 0:
        raise ValueError("base_price must be non-negative")

    return base_price
