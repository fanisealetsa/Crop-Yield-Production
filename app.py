
from flask import Flask, render_template, request, jsonify
from prediction_model import predict_yield

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        pesticides = data['pesticides']
        temperature = data['temperature']
        rainfall = data['rainfall']

        predicted_yield, lower, upper, interpretation, improvements = predict_yield(pesticides, temperature, rainfall)

        return jsonify({
            "predicted_yield": predicted_yield,
            "lower": lower,
            "upper": upper,
            "interpretation": interpretation,
            "improvements": improvements
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
