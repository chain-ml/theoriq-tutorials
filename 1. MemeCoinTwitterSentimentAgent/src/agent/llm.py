import os
import logging
from typing import List, Any

from openai import OpenAI

import constants
from . import prompts

logger = logging.getLogger(__name__)

class OpenAILLM:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.system_message = prompts.SYSTEM_MESSAGE
        self.client = OpenAI(api_key=self.api_key)

    def _build_messages(self, prompt: str) -> List[Any]:
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": [{"type": "text", "text": prompt}]},
        ]
        return messages

    def completions(self, memecoin, context):
        try:
            prompt = prompts.PROMPT_TEMPLATE.format(
                memecoin=memecoin,
                tweets=context
            )
            
            logger.info(f"Calling {constants.OPENAI_MODEL_NAME} ...")
            response = self.client.chat.completions.create(
                model=constants.OPENAI_MODEL_NAME,
                messages=self._build_messages(prompt=prompt),
                temperature=constants.TEMPERATURE
            )

            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling {constants.OPENAI_MODEL_NAME}: {e}")
            raise e
    
        
