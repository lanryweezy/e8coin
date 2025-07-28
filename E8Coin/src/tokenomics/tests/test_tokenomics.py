import unittest
import os
from ..economics import SymCoinEconomics

class TestTokenomics(unittest.TestCase):
    def test_predict_economy(self):
        economics = SymCoinEconomics()
        economics.simulate_market(years=10)
        self.assertTrue(os.path.exists("token_supply.png"))

if __name__ == '__main__':
    unittest.main()
