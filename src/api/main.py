from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("models/xgboost_model.pkl", "rb"))  # Update model path if need be

# Add this preprocessing function
def preprocess_input(input_df):
    mapping_gender = {'Male': 1, 'Female': 0}
    mapping_partner = {'Yes': 1, 'No': 0}
    mapping_contract = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}

    input_df['gender'] = input_df['gender'].map(mapping_gender)
    input_df['Partner'] = input_df['Partner'].map(mapping_partner)
    input_df['Contract'] = input_df['Contract'].map(mapping_contract)
    return input_df

@app.route("/predict", methods=["POST"])
def predict():
    input_json = request.get_json(force=True)
    input_df = pd.DataFrame([input_json])
    input_df = preprocess_input(input_df)  # Add this preprocessing step
    prediction = model.predict(input_df)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
