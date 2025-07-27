import unittest
from ..ai_security_layer import ThreatDetector, AISecurityLayer

class MockTransaction:
    def __init__(self, amount):
        self.amount = amount

class TestAISecurity(unittest.TestCase):
    def test_analyze(self):
        detector = ThreatDetector()
        transactions = [MockTransaction(1000), MockTransaction(2000)]
        risk_report = detector.analyze(transactions)
        self.assertIsInstance(risk_report.quantum_risk, float)
        self.assertGreater(risk_report.quantum_risk, 0)
        self.assertLess(risk_report.quantum_risk, 1)

    def test_shield_mode(self):
        security_layer = AISecurityLayer()
        transactions = [MockTransaction(100000)]
        # This should trigger the shield mode
        security_layer.monitor_network(transactions)

if __name__ == '__main__':
    unittest.main()
