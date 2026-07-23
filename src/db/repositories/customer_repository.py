from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.customers import Customer


class CustomerRepository:
    def __init__(
            self,
            session:AsyncSession
    ):
        self.session=session

  

    async def get_by_id(
            self,
            customer_id:int
            )->Customer|None:
        result=await self.session.execute(
            select(Customer).where(
                Customer.id==customer_id
            )
        )
        return result.scalar_one_or_none()
    

