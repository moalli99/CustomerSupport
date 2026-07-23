from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.orders import Order

class OrderRepository:
    def __init__(
            self,
            session:AsyncSession
    ):
        self.session=session

    async def get_by_id(
            self,
            order_id:int
    )->Order | None:
        result=await self.session.execute(
            select(Order).where(
                Order.id==order_id
            )
        )
        return result.scalar_one_or_none()

    async def get_by_customer_id(
            self,
            customer_id:int
    )->list[Order]:
        result=await self.session.execute(
            select(Order).where(
                Order.customer_id==customer_id
            )
        )
        return list(result.scalars().all())
            