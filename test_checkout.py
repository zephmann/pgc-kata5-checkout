# :coding: utf-8

import os
import os.path

import pytest

import checkout

PRICING_CONFIG = os.path.join(os.getcwd(), "price_config.json")


@pytest.fixture
def co():
    return checkout.Checkout(PRICING_CONFIG)


@pytest.mark.parametrize("items_string, total", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),
    ("AAAB",160),
    ("AAABB", 175),
    ("AAABBD", 190),
    ("DABABA", 190),
])
def test_totals(co, items_string, total):
    for item in items_string:
        co.scan(item)

    assert co.total == total
