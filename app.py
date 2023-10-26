# Misha Jain, 220001045

from flask import Flask, render_template, request
import joblib
model = joblib.load('models/model1.pkl')
word_dict = joblib.load('models/word_dict1.pkl')

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":

        inp = request.form.get("inp")

        features = []
        feature = []
        f = inp
        blob = f.split()

        for i in word_dict:
            feature.append(blob.count(i[0]))
        features.append(feature)

        label = model.predict(features)

        if label == 1:
            return render_template('home.html', message="Spam Email⚠️⚠️")

        elif label == 0:
            return render_template('home.html', message="Not a Spam Email✅✅")

    return render_template('home.html')

# To run, please write "flask run" in the terminal
