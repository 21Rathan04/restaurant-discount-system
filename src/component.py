def calculate_discount(total, customer_type, coupon_code=None):

    if total < 0:
        raise ValueError("Total cannot be negative")

    valid_customer_types = ["REGULAR", "VIP"]

    if customer_type not in valid_customer_types:
        raise ValueError("Invalid customer type")

    discount = 0

    if customer_type == "VIP":
        discount += 0.20

    if coupon_code == "SAVE10":
        discount += 0.10

    if discount > 0.30:
        discount = 0.30

    final_total = total * (1 - discount)

    return round(final_total, 2)