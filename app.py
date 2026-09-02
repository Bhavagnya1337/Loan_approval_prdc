from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():



    name = request.form['applicant_name']
    phone = request.form['applicant_phnnumber']
    income = float(request.form['income'])
    loan_amount = float(request.form['loan_amount'])
    lt = float(request.form['loan_time'])
    loan_time = int(request.form['loan_time'])

    area = request.form['area']

    if area == "Rural":
        area = 0
    elif area == "Semiurban":
        area = 1
    else:
        area = 2

    prediction = model.predict(
        [[income, loan_amount, loan_time, area]]
    )

    if prediction[0] == 1:
        result_text = "✅ Loan Approved"
    else:
        result_text = "❌ Loan Rejected"

    

    return render_template(
        'result.html',
        name=name,
        phone=phone,
        income=income,
        loan_amount=loan_amount,
        loan_time=loan_time,
        area=area,
        prediction=result_text
    )

if __name__ == "__main__":
    app.run(debug=True)