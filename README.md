# City Emulator with CAMEL AI

## Project Overview

The City Emulator is an AI-powered platform leveraging Camel AI to simulate and aggregate real-time data for smart city management. The system integrates multiple agents to collect, analyze, and summarize city-specific data, including citizen feedback, traffic conditions, and environmental updates.

## Project Structure

```
parthshr370-city-emulator-with-camel-ai/
├── README.md
├── config.py
├── main.py
├── requirements.txt
├── test.ipynb  # Jupyter notebook for testing various modules and functionalities.
├── agents/
│   ├── __init__.py
│   ├── citizen_agent.py
│   ├── environment_agent.py
│   └── traffic_agent.py
├── tools/
│   ├── data_aggregator.py
│   ├── traffic_tool.py
│   └── weather_tool.py
└── utils/
    └── logger.py
```

### Key Files

#### 1. `config.py`

Handles environment variables and API keys:

- `OPEN_ROUTER_API_KEY`: API key for OpenRouter.
- `DAPPIER_API_KEY`: API key for Dappier Toolkit.
- `AGENTOPS_API_KEY`: API key for AgentOps.

#### 2. `main.py`

Entry point of the City Emulator:

- Initializes AgentOps session.
- Instantiates Citizen, Traffic, and Environment agents.
- Collects data from each agent.
- Aggregates data into a city dashboard.

#### 2. `test.ipynb`

A testing environment for individual components:

- Tests logger functionality.
- Tests `TrafficToolWrapper` and `WeatherToolWrapper`.
- Provides quick feedback and debugging.

## Agents

### CitizenAgent (`agents/citizen_agent.py`)

Simulates citizen feedback about urban services and public safety.

- Uses Google Gemini-2.0-flash-001 model via OpenRouter.
- Generates feedback based on simulated citizen concerns.

#### Methods:

- `get_city_feedback()`: Retrieves recent feedback from simulated citizens.

#### Usage:

```python
citizen_agent = CitizenAgent("New York")
feedback = citizen_agent.get_city_feedback()
```

#### 3. `TrafficAgent`

Analyzes current city traffic conditions:

- Uses Gemini model via OpenRouter.
- Integrates with `TrafficToolWrapper` to get real-time traffic data.

#### Methods:

- `get_traffic_status()`: Retrieves current traffic congestion data.

#### Usage:

```python
traffic_agent = TrafficAgent("New York")
traffic_status = traffic_agent.get_traffic_status()
```

#### 3. `EnvironmentAgent`

Provides weather and environmental data:

- Utilizes DappierToolkit via the `WeatherToolWrapper`.
- Queries real-time weather and environmental alerts.

#### Methods:

- `get_environment_update()`: Retrieves latest weather and environmental alerts.

#### Usage:

```python
environment_agent = EnvironmentAgent("New York")
env_update = environment_agent.get_environment_update()
```

### Tools

- **TrafficToolWrapper (`tools/traffic_tool.py`)**: Queries real-time traffic data through the DappierToolkit.
- **WeatherToolWrapper (`tools/weather_tool.py`)**: Queries real-time weather data via the DappierToolkit.

### Utilities

- **Logger (`utils/logger.py`)**: Provides logging functionality with standardized formatting for easier debugging.

### Data Aggregator

`tools/data_aggregator.py`: Combines data from Citizen, Traffic, and Environment agents into a unified city dashboard for presentation.

### Main Script Execution (`main.py`)

Runs the emulator workflow:

1. Initiates AgentOps tracking.
2. Retrieves and aggregates city data.
3. Outputs the aggregated city dashboard to the user.

#### Usage:

```bash
python main.py
```

### Environment Setup

Install dependencies via:

```bash
uv pip install -r requirements.txt
```

### Configuration

Set environment variables in `.env` file:

```dotenv
OPEN_ROUTER_API_KEY=<your-open-router-api-key>
DAPPIER_API_KEY=<your-dappier-api-key>
AGENTOPS_API_KEY=<your-agentops-api-key>
```

## Logging

Uses a centralized logging utility (`utils/logger.py`) for consistent logging.

# Sample Output(NYC):

--- City Dashboard ---

=== Smart City Dashboard ===

Citizen Feedback:
Okay, here's a simulated compilation of recent citizen feedback on city services and public safety in NYC, drawing from the kinds of comments you might find on social media, neighborhood forums, 311 reports, and local news comment sections.  I've organized it by topic for clarity.

**1. Sanitation & Street Cleanliness:**

*   **Upper West Side Resident (via Nextdoor):** "The overflowing trash cans on Amsterdam Avenue are attracting rats again.  It's gotten noticeably worse in the last few weeks.  Can the city increase pickup frequency, especially near the restaurants?"
*   **Bronx Resident (via 311 complaint simulation):** "Missed garbage collection on Tuesday, July 16th on [Street Name]. Still not picked up as of Thursday. Bags are ripped open and garbage is all over the sidewalk. Health hazard!"
*   **Brooklyn Resident (via Twitter):** "Seriously, @NYCSanitation, what's with the piles of uncollected leaves on my block in Park Slope? It's been there for weeks! Makes the neighborhood look terrible."
*   **Queens Resident (via local news comment section):** "They need to bring back street sweeping more often. Since they cut back, the streets are so much dirtier, especially after rain."

**2. Public Transportation (Subway & Buses):**

*   **Manhattan Commuter (via Twitter):** "@MTA another signal delay on the [Line Letter] train this morning!  I'm going to be late for work *again*.  How many more years of this?"
*   **Brooklyn Resident (via Reddit):** "The bus service in my neighborhood (Bushwick) is a joke. Buses are always late, or they just don't show up at all. Makes it impossible to rely on public transit."
*   **Queens Resident (via 311 complaint simulation):** "Elevator out of service at the [Subway Station Name] station for the past three days. This is completely unacceptable for elderly and disabled riders. When will it be fixed?"
*   **Manhattan Resident (via Facebook group):** "The increased police presence in the subway is making me feel safer, but I wish they'd focus more on fare evasion and less on harassing street performers."

**3. Public Safety & Crime:**

*   **Brooklyn Resident (via Citizen app simulation):** "Heard gunshots near [Intersection] in Crown Heights around 10 PM last night.  Police responded quickly, but it's still scary.  Feels like things are getting worse."
*   **Manhattan Resident (via Nextdoor):** "There's been a noticeable increase in package thefts in my building lobby in the East Village.  We need more security cameras or a better system for package delivery."
*   **Bronx Resident (via local news comment section):** "I don't feel safe walking alone at night in my neighborhood (Mott Haven) anymore. There needs to be more police patrols, especially in the parks."
*   **Queens Resident (via Twitter):** "Another hit-and-run in Astoria! Drivers are getting more reckless. Need more traffic enforcement and pedestrian safety measures."
*   **Citywide Resident (via online forum):** "I'm glad to see the city is addressing mental health issues on the subway, but we need more long-term solutions and support for people struggling with homelessness and mental illness."

**4. Parks & Recreation:**

*   **Manhattan Resident (via Yelp review simulation of a park):** "[Park Name] is beautiful, but the bathrooms are always filthy and often locked.  The city needs to invest more in park maintenance."
*   **Brooklyn Resident (via Instagram comment on a Parks Dept. post):** "When are you going to fix the broken playground equipment at [Playground Name] in Prospect Park? It's been like that for months, and kids are getting hurt."
*   **Queens Resident (via 311 complaint simulation):** "Loud music and parties in [Park Name] in Corona are going on until 2 AM every weekend.  It's disturbing the peace and keeping residents awake.  Need more enforcement of park rules."
*   **Bronx Resident (via Facebook group):** "The community garden at [Garden Name] is thriving, but we need more funding for tools and supplies.  It's such a valuable resource for the neighborhood."

**5. Affordable Housing & Homelessness:**

*   **Citywide Resident (via online petition simulation):** "The city needs to do more to address the affordable housing crisis. Rents are skyrocketing, and people are being priced out of their neighborhoods."
*   **Manhattan Resident (via Twitter):** "Saw a large homeless encampment under the [Highway Name] overpass in Midtown.  It's heartbreaking.  We need more shelters and support services."
*   **Brooklyn Resident (via local news comment section):** "Building more luxury condos isn't the answer. We need truly affordable housing for low-income families and seniors."
*   **Queens Resident (via Nextdoor):** "The city's efforts to address homelessness in my neighborhood (Long Island City) are appreciated, but we need a more comprehensive approach that includes mental health care and job training."

**Important Considerations:**

*   **Anecdotal vs. Statistical:** This is simulated feedback and may not reflect the overall statistical trends in crime or service performance.
*   **Geographic Variation:** Experiences vary widely depending on the specific neighborhood.
*   **Bias:** Online feedback tends to be skewed towards negative experiences. People are more likely to complain than to praise.
*   **Real-World Data:** To get a truly accurate picture, you'd need to consult official city data, 311 reports, and conduct surveys.

This compilation is designed to give you a sense of the kinds of concerns that are on the minds of many New Yorkers.  It's a starting point for understanding the challenges and opportunities facing the city.


Traffic Status:
Traffic in NYC is pretty hectic right now! 🚦 Here’s the latest:

- Real-time traffic maps are showing busy conditions, especially around major routes and bridges.
- You can check out the **511NY** site for up-to-the-minute traffic info, including travel times, accidents, and camera feeds.
- Key areas to watch include the **LIE**, bridge and tunnel crossings, and the New Jersey Turnpike.
- There’s ongoing discussion about **congestion pricing** in Manhattan, which could affect traffic patterns in the near future.

Stay safe and plan your route accordingly! 🗽🚗

---
