from fastapi import FastAPI
import uvicorn
import pickle as pkl

app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

@app.get("/")
def home():
    return {'text':'Loan Prediction'}

@app.post("/predict")
def predict(Employed: int, BankBalance:int, AnnualSalary: int):
    model = pkl.load(open("model.pkl","rb"))
    prediction = model.predict([[Employed, BankBalance, AnnualSalary]])
    output = round(prediction[0])

    return {"The Loan Status is : {}".format(output)}


if __name__ == "__main__":
    uvicorn.run(app)

