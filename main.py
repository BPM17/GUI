from fastapi import FastAPI
from pydantic  import BaseModel
from typing import Optional

global vehicleList
vehicleList = []

fenix = FastAPI()

class Vehicle(BaseModel):
    vin : str
    brand : str
    year : Optional[int]
    
    def __str__(self):
        return __dict__
    
@fenix.get("/")
def index():
    return("this is a test")

@fenix.get("/commandId/{commandId}")
def commandId(commandId):
    return {"commandId": commandId}

@fenix.post("/vehicle")
def  add_vehicle(vehicle: Vehicle):
    global vehicleList
    vehicleList.append(Vehicle)
    return("Message added correctly")

@fenix.get("/vehicle/{vin}")
def  get_vehicle(vin):
    return vehicleList
    for i in range (len(vehicleList)):
        if vehicleList[i].vin == vin:
            return  vehicleList [i]