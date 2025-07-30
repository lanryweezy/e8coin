import unittest
import os
from ..sdk import SymCoinSDK

class TestSDK(unittest.TestCase):
    def test_load_wasm_module(self):
        # Create a dummy wasm module for testing
        with open("lattice_crypto.wasm", "wb") as f:
            f.write(b"\x00\x61\x73\x6d\x01\x00\x00\x00\x01\x07\x01\x60\x02\x7f\x7f\x01\x7f\x03\x02\x01\x00\x07\x07\x01\x03\x61\x64\x64\x00\x00\x0a\x09\x01\x07\x00\x20\x00\x20\x01\x6a\x0b")

        sdk = SymCoinSDK(network="testnet")
        module = sdk.crypto
        result = module.add(1, 2)
        self.assertEqual(result, 3)
        os.remove("lattice_crypto.wasm")

if __name__ == '__main__':
    unittest.main()
