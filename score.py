from helper import TfidfVectorizer
import pandas as pd

train = pd.read_csv('Data/train.csv',
                       header=0)
train = train.dropna()
msg_train = train['content']

tfidf = TfidfVectorizer(data=msg_train)


def score(text, model, threshold):
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
    
    text_vector = tfidf.tfidf_vector([text])

    # Make the prediction
    propensity = model.predict_proba(text_vector)[0][1]  # Assuming binary classification

    # Apply the threshold
    prediction = bool(propensity > threshold)

    return prediction, propensity