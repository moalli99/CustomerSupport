import logging
from src.core.config import settings
import sys
def setup_logging()->None:
    """
    Configure application logging.
    """
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,

    )