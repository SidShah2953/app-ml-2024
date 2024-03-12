import unittest
from score import score
from joblib import load

# Load the best model from train.ipynb
model = load("mlartifacts/260523122208174751/c53d44cc2d7541c3834b9919e49c66b2/artifacts/skl-svc-linear/model.pkl")

class TestScore(unittest.TestCase):

    def test_smoke_test(self):
        """Tests if the score function runs without crashing."""
        text = "This is a test text."
        threshold = 0.5
        prediction, propensity = score(text, model, threshold)
        self.assertIsNotNone(prediction)
        self.assertIsNotNone(propensity)

    def test_format_test(self):
        """Tests if input/output formats and types are as expected."""
        text = "This is a test text."
        threshold = 0.5
        prediction, propensity = score(text, model, threshold)
        self.assertIsInstance(prediction, bool)
        self.assertIsInstance(propensity, float)

    def test_prediction_range(self):
        """Tests if the prediction value is 0 or 1."""
        text = "This is a test text."
        threshold = 0.5
        prediction, _ = score(text, model, threshold)
        self.assertIn(prediction, (0, 1))

    def test_propensity_range(self):
        """Tests if the propensity score is between 0 and 1."""
        text = "This is a test text."
        threshold = 0.5
        _, propensity = score(text, model, threshold)
        self.assertGreaterEqual(propensity, 0.0)
        self.assertLessEqual(propensity, 1.0)

    def test_threshold_zero(self):
        """Tests if prediction is always 1 with a threshold of 0."""
        threshold = 0.0
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, threshold)
        self.assertEqual(prediction, True)
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, threshold)
        self.assertEqual(prediction, True)

    def test_threshold_one(self):
        """Tests if prediction is always 0 with a threshold of 1."""
        threshold = 1.0
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, threshold)
        self.assertEqual(prediction, False)
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, threshold)
        self.assertEqual(prediction, False)

    def test_spam_text(self):
        """Tests if the prediction is 1 for obvious spam text."""
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, 0.5)
        self.assertTrue(prediction)  # Adjust assertion based on your model

    def test_non_spam_text(self):
        """Tests if the prediction is 0 for obvious non-spam text."""
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, 0.5)
        self.assertFalse(prediction)  # Adjust assertion based on your model

if __name__ == "__main__":
    unittest.main()