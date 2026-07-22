from __future__ import annotations 

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,ForeignKey,Enum


from src.db.enums.order_status import OrderStatus
from src.db.base_model import BaseModel

if TYPE_CHECKING:
    from .customers import Customer

class Order(BaseModel):
    __tablename__="orders"
    status:Mapped[OrderStatus]=mapped_column(
        Enum(OrderStatus),
        nullable=False,
        default=OrderStatus.PENDING
    )
    customer:Mapped["Customer"]=relationship(
        back_populates="orders"
    )
    customer_id: Mapped[int] = mapped_column(
    ForeignKey("customers.id"),
    nullable=False
)

