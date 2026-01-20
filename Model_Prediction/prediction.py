import pickle
import pandas as pd

with open("Model_Prediction/model.pkl","rb") as f:
    model=pickle.load(f)

def predict_output(user_info: dict):
    user_input=pd.DataFrame([user_info])
    prediction=round(model.predict(user_input)[0],2)
    return prediction
