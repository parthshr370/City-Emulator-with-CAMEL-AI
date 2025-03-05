from camel.agents.chat_agent import ChatAgent
from camel.configs import ChatGPTConfig
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

from config import OPEN_ROUTER_API_KEY
from tools.weather_tool import WeatherToolWrapper
from utils.logger import get_logger

logger = get_logger(__name__)


class EnvironmentAgent:
    def __init__(self):
        self.model = ModelFactory(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            model_type=ModelType.GPT3,
            api_key=OPEN_ROUTER_API_KEY,
            url="https://openrouter.ai/api/v1",
            model_config=ChatGPTConfig(temperature=0.4, max_tokens=4096),
        )

        sys_msg = BaseMessage.make_assistant_message(
            role_name="Environment Agent",
            content="You provide real-time weather and enviornmental updates.",
        )

        self.weather_tool = WeatherToolWrapper()
        self.agent = ChatAgent(
            system_message=sys_msg,
            model=self.model,
            tools=[self.weather_tool.get_tool()],
        )
        logger.info("EnvironmentAgent initialized.")

    def get_weather_update(self):
        prompt = "Provide the latest weather update and any notable environmental alerts for the city with the best possible accuracy."
        response = self.agent.send_and_await_response(prompt)
        logger.info(f"EnvironmentAgent response: {response}")

        return {"weather_update": response}
