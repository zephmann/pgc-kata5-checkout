# :coding: utf-8

import bisect
import json


class Checkout:

    def __init__(self, pricing_config):
        self.total = 0
        self._items = []
        
        with open(pricing_config, "r") as f:
            self._pricing_rules = json.load(f)

    def reset(self):
        """Reset the items list and total cost."""
        self.total = 0
        self._items = []

    def scan(self, item):
        """Scan a new item."""
        # insert in order
        bisect.insort(self._items, item)
        
        self.calc_total()

    def calc_total(self):
        """Calculate the total cost for the items."""
        self.total = 0
        item_string = "".join(self._items)
        for rule, cost in self._pricing_rules.items():
            parts = item_string.split(rule)
            
            count = len(parts) - 1
            self.total += count * cost

            item_string = "".join(parts)

        assert not item_string
