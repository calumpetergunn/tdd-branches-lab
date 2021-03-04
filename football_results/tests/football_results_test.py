import unittest

from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    # def setUp(self):
    #     self.result = result
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_home_win(self):
        result = {    
    "home_score": 2,
    "away_score": 0
        }
        self.assertEqual("Home win", get_result(result))

    def test_away_win(self):
        result = {    
    "home_score": 2,
    "away_score": 4
        }
        self.assertEqual("Away win", get_result(result))

    def test_draw(self):
        result = {    
    "home_score": 2,
    "away_score": 2
        }
        self.assertEqual("Draw", get_result(result))

    def test_get_results(self):
        results_list = ["Home win", "Home win", "Draw", "Away win"]
        self.assertEqual(["Home win", "Home win", "Draw", "Away win"], get_results(results_list))


if __name__ == "__main__":
    unittest.main()
