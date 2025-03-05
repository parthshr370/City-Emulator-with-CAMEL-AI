from camel.toolkits import DappierToolkit, FunctionTool
from utils.logger import get_logger

logger = get_logger(__name__)

class TrafficToolWrapper:
    def __init__(self):
        self.toolkit = DappierToolkit()
        logger.info("Traffic Tool initialized")
    
    def get_tool(self):
        return FunctionTool(self.search_traffic)

    def search_traffic(self, query: str, city: str):
        full_query = f"{query} in {city}"
        logger.debug("TrafficTool query: %s", full_query)
        try:
            response = self.toolkit.search_real_time_data(query=full_query)
            logger.debug("TrafficTool response: %s", response)
            return response
        except Exception as e:
            logger.error("TrafficTool error: %s", str(e))
            return "Error retrieving traffic data."
