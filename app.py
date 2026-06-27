from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load pipeline model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return "🚗 Automobile Prediction API is Live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # ✅ Directly convert input to DataFrame
        input_df = pd.DataFrame([data])

        # ✅ Pipeline handles everything
        prediction = model.predict(input_df)

        return jsonify({
            'status': 'success',
            'predicted_price': round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)