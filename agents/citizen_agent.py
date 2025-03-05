from camel.agents.chat_agent import ChatAgent
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from config import OPEN_ROUTER_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

class CitizenAgent:
    def __init__(self, city):
        self.city = city
        self.model = ModelFactory.create(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            model_type="google/gemini-2.0-flash-001",
            api_key=OPEN_ROUTER_API_KEY,
            url="https://openrouter.ai/api/v1",
            model_config_dict={"temperature": 0.4, "max_tokens": 4096},
        )

        sys_msg = BaseMessage.make_assistant_message(
            role_name="Citizen Agent",
            content=f"You simulate citizen feedback on urban issues (e.g., public events, safety, local services) in {self.city}.",
        )

        self.agent = ChatAgent(system_message=sys_msg, model=self.model)
        logger.info("Citizen Agent initialized for city: %s", self.city)

    def get_city_feedback(self):
        prompt = f"Provide recent citizen feedback on city services and public safety in {self.city}."
        response = self.agent.step(prompt)
        logger.info("City feedback: %s", response)
        return {"citizen_feedback": response}
