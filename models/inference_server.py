from fastapi import FastAPI
import mlflow.pyfunc


app = FastAPI()
model = mlflow.pyfunc.load_model('models:/SimpleModel/1')


@app.post('/predict')
async def predict(payload: dict):
# payload: {"features": [[...]]}
df = payload['features']
preds = model.predict(df)
return {"predictions": preds.tolist()}
