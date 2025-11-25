from flask import Flask, render_template, request, flash
import numpy as np
import pickle
import os
app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret"  # needed for flash messages

# ---- Load your model once, at startup ----
# Recommended: save your model as a scikit-learn Pipeline in model.pkl
# so it already includes any preprocessing (scaling, etc.)
HERE = os.path.abspath(os.path.dirname(__file__))
MODEL_PATH = os.path.join(HERE, "model.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("[INFO] Model loaded successfully.")
except Exception as e:
    model = None
    print(f"[ERROR] Could not load model from {MODEL_PATH}: {e}")

# Optional: simple health check
@app.route("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}, 200

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        flash("Model failed to load. Ensure model.pkl exists and is a valid scikit-learn pickle.")
        return render_template("index.html")

    try:
        # ----- Read inputs -----
        gender_raw  = request.form.get("gender", "").strip().lower()
        age         = float(request.form.get("age", "").strip())
        height      = float(request.form.get("height", "").strip())
        duration    = float(request.form.get("duration", "").strip())
        heart_rate  = float(request.form.get("heart_rate", "").strip())
        body_temp   = float(request.form.get("body_temp", "").strip())

        # ----- Encode gender -> numeric -----
        # Adjust mapping to match your trained model!
        # Example: male=0, female=1, other/unspecified=2 (if model supports it)
        
        if gender_raw in ("male", "m", "0"):
          gender = 0.0
        elif gender_raw in ("female", "f", "1"):
          gender = 1.0
        else:
          flash("Please select a valid gender.")
          return render_template("index.html")
        
        # ----- Build feature vector in the EXACT order your model expects -----
        # Here we assume the model expects: [gender, age, height, heart_rate, body_temp]
        X = np.array([[gender, age, height, duration, heart_rate, body_temp]], dtype=float)

        # ----- Predict -----
        y_pred = model.predict(X)
        value = float(y_pred[0])

        return render_template("index.html", prediction=value, last_inputs={
            "gender": gender_raw,
            "age": age,
            "height": height,
            "duration": duration,
            "heart_rate": heart_rate,
            "body_temp": body_temp
        })

    except ValueError:
        flash("Please enter valid numeric values in all fields.")
        return render_template("index.html")
    except Exception as e:
        flash(f"Something went wrong while predicting: {e}")
        return render_template("index.html")
    

if __name__ == "__main__":
    # If you’re in Docker/WSL, host="0.0.0.0". Otherwise default is fine.
    app.run(debug=True, host="127.0.0.1", port=5000)
