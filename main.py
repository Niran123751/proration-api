from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    old_price: float
    new_price: float
    days_remaining: int
    days_in_actual_month: int
    spec: str


@app.post("/")
def calculate(data: Request):
    difference = data.new_price - data.old_price

    if data.spec == "v1":
        charge = difference * (data.days_remaining / 30)
    elif data.spec == "v2":
        charge = difference * (
            data.days_remaining / data.days_in_actual_month
        )
    else:
        return {"error": "Invalid spec"}

    return {"charge": charge}
