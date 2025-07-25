from pydantic import BaseModel, Field
from typing import Optional

class CalcRequest(BaseModel):
    x: float = Field(..., description="Primul operand (sau n pentru fib/fact)")
    y: Optional[float] = Field(None, description="Al doilea operand (numai pentru pow)")

class CalcResponse(BaseModel):
    operation: str
    x: float
    y: Optional[float]
    result: float
