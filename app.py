from fastapi import FastAPI
from schema.user_input import User
from Model_Prediction.prediction import predict_output
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Customer Calories Burnt Prediction"}

@app.post("/predict")
def Predict(user_data:User):
    user_info ={
        "Gender":user_data.Gender_num,
        "Age":user_data.Age,
        "Height":user_data.Height,
        "Duration":user_data.Duration,
        "Heart_Rate":user_data.Heart_Rate,
        "Body_Temp":user_data.Body_Temp
    }
    output=predict_output(user_info)
    return JSONResponse(status_code=203,content={"response":f"CALORIES BURNT BY YOU  {output} In (kcal)"})

