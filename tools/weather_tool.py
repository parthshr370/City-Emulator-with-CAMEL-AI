from camel.toolkits import DappierToolkit, FunctionTool

from utils.logger import get_logger

logger = get_logger(__name__)


class WeatherToolWrapper:
    def __init__(self):
        self.toolkit = DappierToolkit()
        logger.info("Weather Tool initialized")

    def get_tool(self):
        return FunctionTool(self.search_weather)

    def search_weather(self, query: str, city: str):
        full_query = f"{query} in {city}"
        logger.debug("WeatherTool query: %s", full_query)
        try:
            response = self.toolkit.search_real_time_data(query=query)
            logger.debug("WeatherTool response: %s", response)
            return response
        except Exception as e:
            logger.error("WeatherTool error: %s", str(e))
            return "Error retrieving weather data."
