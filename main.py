import agentops
from utils.logger import get_logger
from agents.citizen_agent import CitizenAgent
from agents.traffic_agent import TrafficAgent
from agents.environment_agent import EnvironmentAgent
from tools.data_aggregator import aggregate_city_data

logger = get_logger(__name__)

def main():
    agentops.init(default_tags=["City Emulator"])
    logger.info("Starting City Emulator")
    
    city = input("Enter the city for which you want to retrieve data (default: NYC): ") or "NYC"
    
    logger.info("Instantiating agents...")
    citizen_agent = CitizenAgent(city)
    traffic_agent = TrafficAgent(city)
    environment_agent = EnvironmentAgent(city)
    
    logger.info("Collecting citizen feedback...")
    citizen_data = citizen_agent.get_city_feedback()

    logger.info("Collecting traffic data...")
    traffic_data = traffic_agent.get_traffic_status()

    logger.info("Collecting environmental updates...")
    env_data = environment_agent.get_environment_update()

    logger.info("Aggregating city data...")
    dashboard = aggregate_city_data(citizen_data, traffic_data, env_data)
    print("\n--- City Dashboard ---\n")
    print(dashboard)

    agentops.end_session("Success")
    logger.info("AgentOps session ended successfully.")

if __name__ == "__main__":
    main()
