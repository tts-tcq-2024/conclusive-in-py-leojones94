import unittest
from temp_breach_classify import classify_temperature_breach
from breach_infer import infer_breach
from check_alert import check_and_alert

class TypewiseTest(unittest.TestCase):
    
    def test_infer_breach(self):
        self.assertEqual(infer_breach(20, 50, 100), 'TOO_LOW')
        self.assertEqual(infer_breach(60, 50, 100), 'TOO_HIGH')
        self.assertEqual(infer_breach(75, 50, 100), 'NORMAL')

    def test_classify_temperature_breach(self):
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 30), 'NORMAL')
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', 46), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', -1), 'TOO_LOW')
        with self.assertRaises(ValueError):
            classify_temperature_breach('UNKNOWN_COOLING', 30)

    def test_check_and_alert(self):
        # Mocking the print function to capture output
        with patch('builtins.print') as mock_print:
            check_and_alert('TO_CONTROLLER', {'coolingType': 'PASSIVE_COOLING'}, 30)
            mock_print.assert_called_once_with('65261, NORMAL')

        with patch('builtins.print') as mock_print:
            check_and_alert('TO_EMAIL', {'coolingType': 'HI_ACTIVE_COOLING'}, 46)
            mock_print.assert_any_call('To: a.b@c.com')
            mock_print.assert_any_call('Hi, the temperature is too high')

    def test_invalid_alert_target(self):
        with self.assertRaises(ValueError):
            check_and_alert('UNKNOWN_TARGET', {'coolingType': 'PASSIVE_COOLING'}, 30)

if __name__ == '__main__':
    unittest.main()
    unittest.main()
