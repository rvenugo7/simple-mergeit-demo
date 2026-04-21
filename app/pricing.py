def calculate_total(base_price, is_student=False):
    if base_price < 0:
        raise ValueError("base_price must be non-negative")

    total = base_price

    if is_student:
        total *= 0.9

    return total
