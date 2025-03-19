from enum import Enum
from pydantic import BaseModel, field_validator

class SexEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class StudentModel(BaseModel):
    name:str
    roll_no:str
    standard:int
    sex:SexEnum

    @field_validator("sex", mode="before")
    @classmethod
    def check_sex(cls, value):
        allowed_values = {"male", "female", "other"}
        value_lower = value.lower()
        if value_lower not in allowed_values:
            raise ValueError(f"Invalid sex: {value}. Must be one of {allowed_values}.")
        return value_lower  # Normalize to lowercase