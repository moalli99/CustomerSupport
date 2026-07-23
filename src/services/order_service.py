import logging 

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.order_repository import OrderRepository
from src.db.models.orders import Order

logger=logging.getLogger(__name__)

class OrderService:
    def __init__(
            self,
            session:AsyncSession
    ):
        self.repository=OrderRepository(session)

    async def get_order_by_id(
            self,
            order_id:int
    )->Order | None:
        try:
            logger.info(
                "fetching order by id"
            )
            order= await self.repository.get_by_id(order_id)
            if not order:
                logger.warning(
                    "no orders with this id"
                )
                return None
            logger.info(
                "order returned successfully"
            )
            return order
        except Exception:
            logger.exception(
                "Error while fetching order by order_id"
            )
            raise 
    async def get_order_by_customer_id(
            self,
            customer_id:int
        )->list[Order] :
            try:
                logger.info(
                     "fetching order by customer_id"
                )
                orders=await self.repository.get_by_customer_id(customer_id)

                if not orders:
                     logger.warning(
                          "no orders for this customer"
                     )
                     return []
                logger.info(
                     "orders returned successfully for this customer"
                )
                return orders
            except Exception:
                 logger.exception(
                      "Error while fetching order by customer_id"
                 )
                 raise 
            
                

    