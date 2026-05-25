from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.payment.dtos import PaymentsSchema
from src.payment import controller


payment_routes = APIRouter(prefix="/payments")

@payment_routes.post("/create")
def payment_create(body:PaymentsSchema,db:Session=Depends(get_db)):
    return controller.create_payment(body,db)


@payment_routes.get("/status/{order_id}")
def payment_status(order_id: int, db: Session = Depends(get_db)):
    return controller.get_payment_status(order_id, db)



@payment_routes.get("/history/{user_id}")
def payment_history(user_id: int, db: Session = Depends(get_db)):
    return controller.get_payment_history(user_id, db)