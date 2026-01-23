# Calories Burnt Prediction System :

  A full-stack machine learning web application that predicts calories burnt based on user inputs. <br>
The system uses a FastAPI backend for model inference and a Streamlit frontend for user interaction.

---

## Live URL :
   - **Swagger API Docs**  
  https://calories-burnt-prediction-backend.onrender.com/docs
---

## Project Overview:

1.Model training with scikit-learn <br>
2.Model serialization using pickle <br>
3.RESTful inference API with FastAPI <br>
4.Interactive UI built with Streamlit <br>
5.Dockerized services for reproducibility <br>

---

## How to run:
  - **local** :
    1.install the git <br>
    2.clone the project <br>
    3.install the required dependencies <br>
    4.run the backend code using the below command <br>
    - **CMD**
      uvicorn app:app --reload <br>
    5.run the frontend code using the below command<br>
    -**CMD**
      [Important:Replace the "http://backend:8000/predict" in ui.py with "http://127.0.0.1:8000/predict"]<br>

      streamlit run u.py<br>

    -**docker**:
      1.install the docker<br>
      2.build the docker image using below command:
     -**CMD**:
        docker compose build up
  





