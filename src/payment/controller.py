from fastapi import HTTPException
from src.order.models import OrderModel
from src.payment.dtos import PaymentsSchema
from src.payment.models import PaymentModel
from sqlalchemy.orm import Session
from src.utils.db import get_db


def create_payment(body:PaymentsSchema,db:Session):
    order = db.query(OrderModel).filter(OrderModel.id == body.order_id).first()
    if not order:
        raise HTTPException(status_code=404,detail="Order not found")
    if order.status == "paid":
        return {"message": "Order already paid"}
         
 
    if order.total_amount != body.amount:
        raise HTTPException(
            status_code=400,
            detail="Amount not match"
        ) 
        
    payment =  PaymentModel(order_id=body.order_id,
                            payment_id=body.payment_id,
                            amount= body.amount,
                            payment_status="success") 
    db.add(payment) 
    order.status = "paid"
        
    db.commit()
    db.refresh(payment)

    return {
        "message": "Payment created successfully",
        "payment_id": payment.payment_id,
        "status": payment.payment_status
    }
         
           
def get_payment_status(order_id: int, db:Session):
    payment = db.query(PaymentModel).filter(PaymentModel.order_id == order_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {
        "order_id": payment.order_id,
        "payment_id": payment.payment_id,
        "amount": payment.amount,
        "payment_status": payment.payment_status
    }     
    
    

def get_payment_history(user_id: int, db: Session):
    payments = db.query(PaymentModel).join(OrderModel).filter(OrderModel.user_id == user_id ).all()
    if not payments:
        raise HTTPException(status_code=404, detail="No payments found")
    return [
        {
            "order_id": payment.order_id,
            "payment_id": payment.payment_id,
            "amount": payment.amount,
            "payment_status": payment.payment_status
        }
        for payment in payments
    ]            