from sqlalchemy.orm import Session
from . import models, schemas

def log_request(db: Session, req: schemas.CalcRequest, operation: str, result: float):
    db_obj = models.RequestLog(
        operation=operation,
        operand1=req.x,
        operand2=req.y,
        result=result
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
