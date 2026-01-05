from pydantic import BaseModel #base parameters is a zenml class used to define step configuration

class ModelNameConfig(BaseModel):
    model_name: str = "LinearRegression"