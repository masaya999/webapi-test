from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
 return {"greeting":"Hello world"}

def calculate_meal_fee(beef_price: int, meal_price: int) -> int:
 total_price: int = beef_price + meal_price
 return total_price
print("Calculated meal fee", calculate_meal_fee(75, 19))