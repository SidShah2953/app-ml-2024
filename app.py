from flask import Flask, request, jsonify
from score import score
from joblib import load

model = load("mlartifacts/260523122208174751/c53d44cc2d7541c3834b9919e49c66b2/artifacts/skl-svc-linear/model.pkl")
app = Flask(__name__)

@app.route("/score", methods=["POST"])
def flask_score():
    """
    This endpoint receives a text as a POST request and returns a JSON with prediction and propensity.
    """
    # Replace with your logic to process the text and get prediction and propensity
    req_text = request.get_json()[1:-1].replace('"', "").split(': ')
    req_dict = {req_text[0]: req_text[1]}
    text = req_dict['text']
    threshold = 0.5
    prediction, propensity = score(text, model, threshold)
    response = {"prediction": prediction, "propensity": propensity}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=8000)