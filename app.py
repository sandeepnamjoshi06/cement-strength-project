from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/prediction",methods=['POST'])
def predict():
    with open("model.pkl","rb") as file:
        model=pickle.load(file)
    cement=float(request.form["Cement"])
    water=float(request.form["Water"])
    superplasticizer=float(request.form["Superplasticizer"])
    coarse_Aggregate=float(request.form["Coarse Aggregate"])
    fine_Aggregate=float(request.form["Fine Aggregate"])
    age=int(request.form["Age"])
    result=np.around(model.predict([[cement,water,superplasticizer,coarse_Aggregate,fine_Aggregate,age]])[0])
    return render_template("index.html",result1=result)
    

if __name__=="__main__":
    app.run(debug=True)