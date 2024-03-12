# Assignment 3: Testing & Model Serving

## Due 7 March 2024

- Unit testing:
  - In `score.py`

  ```python
  def score(text:str,
            model:sklearn.estimator, 
            threshold:float) -> prediction:bool, 
            propensity:float
  ```
  
  - [x] wWite a function with the following signature that scores a trained model on a text:
  - In `test.py`,
    - [x] Write a unit test function `test_score(...)` to test the score function.
  - You may reload and use the best model saved during experiments in `train.ipynb` (in joblib/pkl format) for testing the score function.
  - You may consider the following points to construct your test cases:
    - [x] Does the function produce some output without crashing (smoke test)
    - [x] Are the input/output formats/types as expected (format test)
    - [x] Is prediction value 0 or 1?
    - [x] Is propensity score between 0 and 1?
    - [x] If you put the threshold to 0 does the prediction always become 1?
    - [x] If you put the threshold to 1 does the prediction always become 0?
    - [x] On an obvious spam input text is the prediction 1?
    - [x] On an obvious non-spam input text is the prediction 0?
- Flask serving:
  - In `app.py`, create a flask endpoint/score that receives a text as a `POST` request and gives a response in the `json` format consisting of prediction and propensity
  - In `test.py`, write an integration test function `test_flask(...)` that does the following:
    - Launches the flask app using command line (e.g. use os.system)
    - Test the response from the localhost endpoint
    - Closes the flask app using command line
    - In `coverage.txt` produce the coverage report output of the unit test and integration test using `pytest`
