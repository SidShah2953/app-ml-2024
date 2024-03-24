import unittest
import requests
from score import score
from joblib import load
import os
import json
from coverage import coverage


# Load the best model from train.ipynb
model = load("mlartifacts/260523122208174751/c53d44cc2d7541c3834b9919e49c66b2/artifacts/skl-svc-linear/model.pkl")

class TestScore(unittest.TestCase):
    def test_smoke_test(self):
        """
        Tests if the score function runs without crashing.
        """
        
        text = "This is a test text."
        threshold = 0.5
        prediction, propensity = score(text, model, threshold)
        self.assertIsNotNone(prediction)
        self.assertIsNotNone(propensity)


    def test_format_test(self):
        """
        Tests if input/output formats and types are as expected.
        """
        
        text = "This is a test text."
        threshold = 0.5
        prediction, propensity = score(text, model, threshold)
        self.assertIsInstance(prediction, bool)
        self.assertIsInstance(propensity, float)


    def test_prediction_range(self):
        """
        Tests if the prediction value is 0 or 1.
        """
        
        text = "This is a test text."
        threshold = 0.5
        prediction, _ = score(text, model, threshold)
        
        self.assertIn(prediction, (0, 1))


    def test_propensity_range(self):
        """
        Tests if the propensity score is between 0 and 1.
        """
        
        text = "This is a test text."
        threshold = 0.5
        _, propensity = score(text, model, threshold)
        self.assertGreaterEqual(propensity, 0.0)
        self.assertLessEqual(propensity, 1.0)


    def test_threshold_zero(self):
        """
        Tests if prediction is always 1 with a threshold of 0.
        """
        
        threshold = 0.0
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, threshold)
        self.assertEqual(prediction, True)
        
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, threshold)
        self.assertEqual(prediction, True)


    def test_threshold_one(self):
        """
        Tests if prediction is always 0 with a threshold of 1.
        """
        
        threshold = 1.0
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, threshold)
        self.assertEqual(prediction, False)
        
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, threshold)
        self.assertEqual(prediction, False)


    def test_spam_text(self):
        """
        Tests if the prediction is 1 for obvious spam text.
        """
        
        spam_text = "FREE STOCKS! Click here!"
        prediction, _ = score(spam_text, model, 0.5)
        self.assertTrue(prediction)  # Adjust assertion based on your model


    def test_non_spam_text(self):
        """
        Tests if the prediction is 0 for obvious non-spam text.
        """
        
        non_spam_text = "Thank you for your email. We will get back to you soon."
        prediction, _ = score(non_spam_text, model, 0.5)
        self.assertFalse(prediction)  # Adjust assertion based on your model


    def test_flask(self):
        """
        Integration test to launch the Flask app, send a request, and check the response.
        """
        # Launch the Flask app in a separate process
        run_comm = 'python app.py'
        os.system(run_comm + " &> /dev/null &")
        
        import time
        time.sleep(10)

        # Send a POST request with some text data
        data = json.dumps({"text": "This is some spam text"})
        response = requests.post("http://127.0.0.1:8000/score", json=data)
        
        assert response.status_code == 200

        # Parse response JSON
        data = json.loads(response.text)

        # Check for presence of prediction and propensity keys
        assert "prediction" in data
        assert "propensity" in data

        # Terminate the Flask app process
        os.system("pkill -2 python app.py")
    

    def test_docker(self):
        """
        Integration test to: 
        - Launch the docker container docker build and docker run
        - Send a request to the localhost endpoint `/score` for a sample text
        - Check if the response is as expected
        - Close the docker container
        """
        # Launch the Flask app in a separate process
        docker_file_path =  "/Users/sidshah/Library/Mobile Documents/com~apple~CloudDocs/Projects/Semester 6/AML - Applied Machine Learning/app-ml-2024/DockerFile.txt"
        run_comm = f'docker build -f "{docker_file_path}" -t sidshah2953/aml .'
        os.system(run_comm)
        
        # Runs the docker container in a separate thread
        os.system("docker run -p 8000:8000 -t sidshah2953/aml &> /dev/null &")
        
        # Wait for docker container to start
        import time
        time.sleep(10)
        # Send a POST request with some text data
        data = json.dumps({"text": "This is some spam text"})
        response = requests.post("http://127.0.0.1:8000/score",
                                 json=data)
        
        assert response.status_code == 200

        # Parse response JSON
        data = json.loads(response.text)

        # Check for presence of prediction and propensity keys
        assert "prediction" in data
        assert "propensity" in data
        
        # Stop all docker containers
        os.system("docker stop $(docker ps -a -q)")


if __name__ == "__main__":
    # Initialize coverage
    cov = coverage()

    # Start coverage measurement
    cov.start()

    # Run your tests
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestScore)
    # Add your test cases to the suite
    unittest.TextTestRunner().run(suite)

    # Stop coverage measurement and generate report
    cov.stop()
    output = open('Coverage.txt', 'w')
    cov.report(file=output)