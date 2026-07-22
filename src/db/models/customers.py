from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base_model import BaseModel


if TYPE_CHECKING:
    from .orders import Order


class Customer(BaseModel):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer",
    )
  