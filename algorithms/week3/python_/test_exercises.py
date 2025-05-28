import unittest
from exercises import order_price

class TestOrderPrice (unittest.TestCase):
  def test_zero_bananas(self):
    self.assertEqual(order_price(0), 499)

  def test_one_banana(self):
     self.assertEqual(order_price(1), 799)

  def test_three_bananas(self):
     self.assertEqual(order_price(3), 1399)

  def test_twelve_bananas(self):
     self.assertEqual(order_price(12), 4099)

  # This one passes 50 breakpoint where
  # 1.50 reduction is required.
  def test_twenty_bananas(self):
     self.assertEqual(order_price(20), 6349)
if __name__ == '__main__':
    unittest.main()