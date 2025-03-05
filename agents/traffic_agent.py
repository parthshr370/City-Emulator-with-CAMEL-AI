from camel.agents.chat_agent import ChatAgent
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType

from config import OPEN_ROUTER_API_KEY
from tools.traffic_tool import TrafficToolWrapper
from utils.logger import get_logger

logger = get_logger(__name__)


class TrafficAgent:
    def __init__(self):
        self.model = ModelFactory(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            api_key=OPEN_ROUTER_API_KEY,
            model_type="google/gemini-2.0-flash-001",
            url="https://openrouter.ai/api/v1",
            model_config_dict={"temperature": 0.4, "max_tokens": 4096},
        )

        sys_msg = BaseMessage.make_assistant_message(
            role_name="Traffic Agent",
            content="You analyze current traffic conditions and congestion in the city.",
        )

        self.traffic_tool = TrafficToolWrapper()
        self.agent = ChatAgent(
            system_message=sys_msg,
            model=self.model,
            tools=[self.traffic_tool.get_tool()],
        )

    def get_traffic_status(self):
        prompt = "What is the current traffic congestion status in the main downtown corridors?"
        response = self.agent.send_and_await_response(prompt)
        logger.info("TrafficAgent response: %s", response)
        return {"traffic_status": response}
