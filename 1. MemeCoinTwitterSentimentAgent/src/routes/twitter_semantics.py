import logging
from time import time

import setup
from routes import update_endpoint_metrics
from agent import MemecoinTwitterAgent

from theoriq.execute import ExecuteContext, ExecuteResponse
from theoriq.schemas import ExecuteRequestBody, TextItemBlock
from theoriq.types import SourceType

from . import routes

logger = logging.getLogger(__name__)


def memecoin_twitter(
    context: ExecuteContext, req: ExecuteRequestBody
) -> ExecuteResponse:
    endpoint = "/api/v1alpha1/execute"
    logger.info(f'message="Received {endpoint} request"')
    logger.info(f"request_id: {context.request_id}")
    start_time = time()

    if not setup.is_ready:
        update_endpoint_metrics(
            method="post", endpoint=endpoint, status=503, start_time=start_time
        )
        raise Exception(
            "The agent deployment is not finished! Please try again in a few minutes. "
            "If the problem persists, contact the agent developer!"
        )
    try:
        last_block = req.last_item_from(SourceType.User).blocks[0]
        memecoin = last_block.data.text
        logger.info(f"USER_INPUT={memecoin}")

        agent = MemecoinTwitterAgent()
        answer = agent.sentiment_analysis(memecoin)
        logger.info(f"AGENT_OUTPUT={answer}")
        logger.info("=============================================")

    except Exception as e:
        update_endpoint_metrics(
            method="post", endpoint=endpoint, status=500, start_time=start_time
        )
        logging.warning(f'message="Error during {endpoint} request" error="{e}"')
        raise e
    else:
        update_endpoint_metrics(
            method="post", endpoint=endpoint, status=200, start_time=start_time
        )
        logging.info(f'message="returning {endpoint} response"')

    return context.new_free_response(
        blocks=[
            TextItemBlock(text=answer),
        ]
    )
