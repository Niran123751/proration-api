from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    old_price: float
    new_price: float
    days_remaining: float
    days_in_actual_month: float
    spec: str

@app.post("/")
def calculate(data: Request):
    spec = data.spec.strip().lower()
    difference = data.new_price - data.old_price

    if spec == "v1":
        charge = difference * (data.days_remaining / 30.0)
    elif spec == "v2":
        charge = difference * (
            data.days_remaining / data.days_in_actual_month
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid spec")

    return {"charge": charge}
