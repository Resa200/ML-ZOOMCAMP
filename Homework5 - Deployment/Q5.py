
import pickle
import numpy as np
from flask import Flask, request, jsonify



# unpickling the model and the dictvectorizer

with open('model2.bin','rb') as f_real:
    model = pickle.load(f_real)

with open('dv.bin','rb') as dv_real:
    dv = pickle.load(dv_real)


app = Flask('card')

@app.route('/predict',methods=['POST'])
 
def predict():

    client = request.get_json()

    X_client = dv.transform([client])
    y_pred = model.predict_proba(X_client)[:,1][0]
    y_pred = np.round(y_pred,3)

    result = {
        "card probability": float(y_pred)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0', port=9696)

