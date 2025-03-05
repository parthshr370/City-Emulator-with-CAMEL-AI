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
    def __init__(self, city):
        self.city = city
        self.model = ModelFactory.create(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            api_key=OPEN_ROUTER_API_KEY,
            model_type="google/gemini-2.0-flash-001",
            url="https://openrouter.ai/api/v1",
            model_config_dict={"temperature": 0.4, "max_tokens": 4096},
        )

        sys_msg = BaseMessage.make_assistant_message(
            role_name="Environment Agent",
            content=f"You provide real-time weather and environmental updates for {self.city}.",
        )

        self.weather_tool = WeatherToolWrapper()
        self.agent = ChatAgent(
            system_message=sys_msg,
            model=self.model,
            tools=[self.weather_tool.get_tool()],
        )
        logger.info("Environment Agent initialized for city: %s", self.city)

    def get_environment_update(self):
        prompt = f"Provide the latest weather update and any notable environmental alerts for {self.city}."
        response = self.agent.step(prompt)
        logger.info("Environment update: %s", response)
        return {"environment_update": response}
