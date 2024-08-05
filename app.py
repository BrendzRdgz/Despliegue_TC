from flask import Flask, jsonify, request, render_template
import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import numpy as np

# Path settings
csv_path = os.path.join(os.path.dirname(__file__), 'data', 'revenue.csv')
csv_path_retrain = os.path.join(os.path.dirname(__file__), 'data', 'revenue_updated.csv')
model_path = os.path.join(os.path.dirname(__file__), 'ad_model.pkl')

app = Flask(__name__)
app.config['DEBUG'] = True

# Home route
@app.route("/", methods=["GET"])
def hello():
    return render_template("home.html")

# Predict route
@app.route('/api/v1/predict', methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "GET":
        model = pickle.load(open(model_path, 'rb'))
        followers = request.args.get('followers', 0)
        average_views = request.args.get('average_views', 0)
        average_interactions = request.args.get('average_interactions', 0)
        posting_frequency = request.args.get('posting_frequency', 0)

        if followers is not None and average_views is not None and average_interactions is not None and posting_frequency is not None:
            prediction = model.predict([[float(followers), float(average_views), float(average_interactions), float(posting_frequency)]])[0]

    return render_template("predict.html", prediction=round(prediction,2))

# Retrain route
@app.route('/api/v1/retrain', methods=["GET"])
def retrain():
    metrics = None
    if os.path.exists(csv_path_retrain):
        data = pd.read_csv(csv_path_retrain)

        # Using the new columns
        X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['revenue']),
                                                            data['revenue'],
                                                            test_size=0.20,
                                                            random_state=42)

        model = Lasso(alpha=6000)
        model.fit(X_train, y_train)
        rmse = round(np.sqrt(mean_squared_error(y_test, model.predict(X_test))),2)
        mape = round(mean_absolute_percentage_error(y_test, model.predict(X_test)),2)
        model.fit(data.drop(columns=['revenue']), data['revenue'])
        pickle.dump(model, open(model_path, 'wb'))

        metrics = {'rmse': rmse, 'mape': mape}
        
    return render_template("retrain.html", metrics=metrics)

if __name__ == '__main__':
    app.run()

