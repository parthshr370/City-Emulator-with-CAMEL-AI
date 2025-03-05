from camel.agents.chat_agent import ChatAgent
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType

from config import OPEN_ROUTER_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)


class CitizenAgent:
    def __init__(self):
        self.agent = ModelFactory(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            api_key=OPEN_ROUTER_API_KEY,
            model_type="google/gemini-2.0-flash-001",
            url="https://openrouter.ai/api/v1",
            model_config_dict={"temperature": 0.4, "max_tokens": 4096},
        )

        sys_msg = BaseMessage.make_assistant_message(
            role_name="Citizen Agent",
            content="You simulate citizen feedback on urban issues (e.g., public events, safety, local services).",
        )

        self.agent = ChatAgent(system_message=sys_msg, model=self.model)
        logger.info("Citizen Agent initialized")

    def get_city_feedback(self):
        prompt = "provide recent citzen feedback on city services and public  safety in downtown area"
        response = self.agent.send_and_await_response(prompt)
        logger.info(f"City feedback: {response}")
        return {"citizen_feedback": response}
