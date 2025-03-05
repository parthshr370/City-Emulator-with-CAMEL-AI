import agentops

from agents.citizen_agent import CitizenAgent
from agents.environment_agent import EnvironmentAgent
from agents.traffic_agent import TrafficAgent
from tools.data_aggregator import aggregate_city_data
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    agentops.init(default_tags=["City Emulator"])
    logger.info("Starting City Emulator")

    # Create agents
    logger.info("Instantiating agents...")

    citizen_agent = CitizenAgent()
    traffic_agent = TrafficAgent()
    environment_agent = EnvironmentAgent()

    # Run each agent to collect data and log progress
    logger.info("Collecting citizen feedback...")
    citizen_data = citizen_agent.get_city_feedback()

    logger.info("Collecting traffic data...")
    traffic_data = traffic_agent.get_traffic_status()

    logger.info("Collecting environmental updates...")
    env_data = environment_agent.get_environment_update()

    # Aggregate data from all agents
    logger.info("Aggregating city data...")
    dashboard = aggregate_city_data(citizen_data, traffic_data, env_data)
    print("\n--- City Dashboard ---\n")
    print(dashboard)

    # End AgentOps session
    agentops.end_session("Success")
    logger.info("AgentOps session ended successfully.")


if __name__ == "__main__":
    main()
