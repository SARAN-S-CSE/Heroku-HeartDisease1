from flask import Flask,request,render_template
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open("model3.pkl","rb"))
@app.route("/")
def home():
    return render_template(("index.html"))
@app.route("/submit",methods=["POST"])
def predict():
    if request.method=="POST":
         fea=[int(x) for x in request.form.values()]
         features=[np.array(fea)]
         print(features)
         prediction=model.predict(features)
         return render_template("submit.html",prediction=prediction)


if __name__=="__main__":
    app.run(debug=True)