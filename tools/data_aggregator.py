def aggregate_city_data(citizen_data, traffic_data, env_data):
    # Combine data from all agents into a city dashboard summary.
    dashboard = "=== Smart City Dashboard ===\n\n"
    dashboard += (
        "Citizen Feedback:\n" + citizen_data.get("citizen_feedback", "No data") + "\n\n"
    )

    dashboard += (
        "Traffic Status:\n" + traffic_data.get("traffic_status", "No data") + "\n\n"
    )
    dashboard += (
        "Environment Update:\n" + env_data.get("environment_update", "No data") + "\n"
    )
    return dashboard
