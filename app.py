from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict_note_authentication():
    if request.method == "POST":
        variance = request.form.get("variance")
        skewness = request.form.get("skewness")
        curtosis = request.form.get("curtosis")
        entropy = request.form.get("entropy")
        prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
        return render_template('index.html', prediction_text="The predicted class is {}".format(prediction[0]))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
