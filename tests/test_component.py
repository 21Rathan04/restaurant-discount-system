import pytest
from src.component import calculate_discount


def test_vip_discount():
    assert calculate_discount(100, "VIP") == 999


def test_coupon_discount():
    assert calculate_discount(100, "REGULAR", "SAVE10") == 90


def test_combined_discount():
    assert calculate_discount(100, "VIP", "SAVE10") == 70


def test_no_discount():
    assert calculate_discount(100, "REGULAR") == 100


def test_negative_total():
    with pytest.raises(ValueError):
        calculate_discount(-50, "VIP")


def test_invalid_customer_type():
    with pytest.raises(ValueError):
        calculate_discount(100, "STUDENT")