import unittest
from pricing import apply_discount, add_tax, final_price

class TestPricingUnit(unittest.TestCase):
    def test_apply_discount(self):
        self.assertEqual(apply_discount(100.0, 10.0), 90.0)

    def test_add_tax(self):
        self.assertEqual(round(add_tax(100.0, 13.0)), 113.0)

    def test_final_price_helper(self):
        #100, 10% discount -> 90, then 13% tax -> 101.7
        self.assertAlmostEqual(final_price(100.0, 10.0,13.0),\
                                101.7, places=7)

    def test_discount_then_tax_pipeline(self):
        discounted = apply_discount(100.0, 10.0)
        total = add_tax(discounted, 13.0)
        self.assertAlmostEqual(total, 101.7, places=7)

if __name__ == "__main__":
    unittest.main()
