""""

This uses a model and dict vectorizer provided to predict if a client will get a credit card

"""

#loading libraries
import pickle
import numpy as np


# unpickling the model and the dictvectorizer
with open('model1.bin','rb') as f_real:
    model = pickle.load(f_real)

with open('dv.bin','rb') as dv_real:
    dv = pickle.load(dv_real)


client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

#getting the prediction probability for a client 
def predict(client):

    X_client = dv.transform([client])
    y_pred = model.predict_proba(X_client)[:,1][0]
    y_pred = np.round(y_pred,3)

    print(y_pred)

predict(client)