def aggregate_city_data(citizen_data, traffic_data, env_data):
    # Helper function to convert ChatAgentResponse to string
    def response_to_text(response):
        # Check if response has 'msgs' attribute and join their content
        if hasattr(response, "msgs") and response.msgs:
            return "\n".join(msg.content for msg in response.msgs)
        else:
            return str(response)
    
    dashboard = "=== Smart City Dashboard ===\n\n"
    dashboard += "Citizen Feedback:\n" + response_to_text(citizen_data.get("citizen_feedback", "No data")) + "\n\n"
    dashboard += "Traffic Status:\n" + response_to_text(traffic_data.get("traffic_status", "No data")) + "\n\n"
    dashboard += "Environment Update:\n" + response_to_text(env_data.get("environment_update", "No data")) + "\n"
    
    return dashboard
