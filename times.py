import uvicorn
from fastapi import FastAPI
import pickle
from datetime import datetime

app = FastAPI()
pickle_in = open(r"C:\Users\samra\OneDrive\Documents\phython\Session 23&24\Time_series_final\tsmodel.pkl","rb")
model=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to python course'}

@app.post('/predict')
def predict(year:int ,month:int ,day:int):
    prediction = model.predict(datetime(year,month,day))
    
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)