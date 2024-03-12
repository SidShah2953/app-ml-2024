import sklearn
from sklearn.preprocessing import TextVectorizer


def score(text: str,
          model: sklearn.estimator,
          threshold: float):
    """Scores a text using the given model and returns prediction and propensity.

    Arguements:
        text: The text to score. (str)
        model: The trained model (sklearn.estimator)
        threshold: The classification threshold. (float)

    Returns:
        A tuple containing:
            prediction: True if the score is above the threshold, False otherwise. (bool)
            propensity: The model's score for the text. (float)
    """
    
    # Preprocess the text
    vectorizer = TextVectorizer()
    text_vector = vectorizer.fit_transform([text])

    # Make the prediction
    propensity = model.predict_proba(text_vector)[0][1]  # Assuming binary classification

    # Apply the threshold
    prediction = propensity > threshold

    return prediction, propensity