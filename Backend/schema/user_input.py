from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

class User(BaseModel):
    Gender : Annotated[Literal["Male","Female"],Field(...,description="enter the age of the user")]
    Age : Annotated[int,Field(...,description="age of the user in years",gt=0,lt=120)]
    Height : Annotated[float,Field(...,description="height of the user in cm",gt=0)]
    Weight : Annotated[float,Field(...,description="weight of the user in kgs",gt=0)]
    Duration : Annotated[int,Field(...,description="Duartion of the user in minutes",gt=0)]
    Heart_Rate : Annotated[float,Field(...,description="heart rate of the user in bpm",gt=0)]
    Body_Temp : Annotated[float,Field(...,description="body temperature of the user in celcius",gt=0)]
     
    @computed_field(return_type=int)
    @property
    def Gender_num(self):
        if self.Gender == "Male":
            return 0
        elif self.Gender=="Female":
            return 1
        else:
            return {"content":"enter a valid Gender"}



