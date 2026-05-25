from pydantic import BaseModel

class PaymentsSchema(BaseModel):
    order_id: int
    payment_id: str
    payment_status: str
    amount:float