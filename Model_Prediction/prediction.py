import pickle
import pandas as pd

with open("Model_prediction/model.pkl","rb") as f:
    model=pickle.load(f)

def predict_output(user_info: dict):
    user_input=pd.DataFrame([user_info])
    print(user_input)
    prediction=model.predict(user_input)[0]
    return prediction
