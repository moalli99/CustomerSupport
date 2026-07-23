import logging 

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.customer_repository import CustomerRepository
from src.db.models.customers import Customer

logger=logging.getLogger(__name__)

class CustomerService:
    def __init__(
            self,
            session:AsyncSession
    ):
        self.repository=CustomerRepository(session)

    async def get_customer_by_id(
            self,
            customer_id:int
    )->Customer | None:
        try :
            logger.info(
                "fetcheing customer by id"
            )
            customer= await self.repository.get_by_id(customer_id)
            if customer is None:
                logger.warning(
                    "customer not found"
                )
                return None
            logger.info(
                "Cutomer founded successfully"
            )
            return customer 
        except Exception:
            logger.exception(
                "Error while fetching customer info by id"
            )
            raise 