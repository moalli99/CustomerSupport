from typing import Literal
from langchain_openai import ChatOpenAI
from src.core.config import settings
import logging
logger=logging.getLogger(__name__)

def get_llm(model_type:Literal["cheap","standard","reasoning"])->ChatOpenAI:
    """
    Create and return llm based on the request type .
    """
    models={
        "cheap":settings.cheap_model,
        "standard":settings.standard_model,
        "reasoning":settings.reasoning_model
    }

    if model_type not in models:
        raise ValueError(
            f"Unknown model type:{model_type}."
            f"Available models:{list(models.keys())}"
        )
    try:
        return ChatOpenAI(
            model=models[model_type],
            api_key=settings.openai_api_key,
            temperature=0
        )
    except Exception as e :
        logger.exception(f"failed to create LLM: {e}")
        raise 



