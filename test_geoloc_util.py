import unittest
from geoloc_util import fetch_location_data

class TestGeoLocUtil(unittest.TestCase):
    def test_valid_city(self):
        """Test fetching data for a valid city."""
        result = fetch_location_data("Madison, WI")
        self.assertIsNotNone(result)  # Ensure we get a result
        self.assertEqual(result['name'], 'Madison')  # Check the name

    def test_valid_zip(self):
        """Test fetching data for a valid zip code."""
        result = fetch_location_data("12345")
        self.assertIsNotNone(result)  # Ensure we get a result
        self.assertEqual(result['name'], 'Schenectady')  # Check the name

    def test_invalid_location(self):
        """Test fetching data for an invalid location."""
        result = fetch_location_data("InvalidLocation")
        self.assertIsNone(result)  # Ensure we get None for invalid input

if __name__ == '__main__':
    unittest.main()  # Run the tests