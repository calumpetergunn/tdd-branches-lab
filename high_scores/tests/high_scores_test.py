import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.high_scores_list = [25, 120, 35, 44, 980, 325]

    def test_latest_score(self):
        self.assertEqual(325, latest(self.high_scores_list))
   
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(980, personal_best(self.high_scores_list))
    # Test top three from list of scores

    def test_top_three(self):
        self.assertEqual([120, 325, 980], personal_top_three(self.high_scores_list))
    # Test ordered from highest tp lowest

    def test_ordered_list(self):
        self.assertEqual([25, 35, 44, 120, 325, 980,], sorted(self.high_scores_list))
    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
