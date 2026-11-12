# 🌍 AI Travel Planner Using CrewAI

## 1. Project Overview

The AI Travel Planner is a Python application built using the CrewAI framework and an OpenAI language model.

The application allows users to enter a city name and receive recommendations for exactly three places to visit.

This project demonstrates how to create and execute a single AI agent using CrewAI.

## 2. Problem Statement

Build a CrewAI Travel Planner agent that:

- Accepts a city name from the user.
- Recommends exactly three tourist attractions.
- Provides a brief description of each attraction.
- Uses one Agent, one Task, and one Crew.
- Executes the workflow using `crew.kickoff()`.
- Displays the final recommendations in the terminal.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| CrewAI | AI agent orchestration |
| OpenAI | Language model |
| python-dotenv | Environment variable management |
| GitHub | Source code management |

**LLM:** `openai/gpt-4o-mini`

## 4. Application Architecture

```text
             START
               |
               v
       Enter City Name
               |
               v
        Python input()
               |
               v
      Travel Planner Agent
               |
               v
       Travel Planning Task
               |
               v
          CrewAI Crew
               |
               v
        crew.kickoff()
               |
               v
       Top 3 Attractions
               |
               v
        Display Results
               |
               v
              END
```

## 5. Agent Configuration

### Agent Role

Experienced Travel Planner

### Agent Goal

Recommend exactly three interesting places to visit in the city selected by the user.

### Agent Backstory

The agent acts as an experienced travel consultant who helps first-time tourists explore new cities.

It specializes in recommending famous landmarks, cultural attractions, and memorable local experiences.

The backstory guides the agent to produce practical, informative, and easy-to-understand recommendations.

## 6. Task Configuration

The Travel Planner agent receives one task.

**Task Description:**

Recommend exactly three places to visit in the city entered by the user.

Each recommendation should contain:

1. Attraction name.
2. Brief description explaining why the attraction is worth visiting.

**Expected Output:**

A numbered list containing exactly three tourist attractions, with a short description for each.

## 7. Project Structure

```text
Travel_Planner/
│
├── travel_planner.py
├── test_config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
└── .env              # Local only; excluded from Git
```

## 8. Installation and Setup

### Step 1: Clone the Repository

Clone the repository from GitHub and open the project folder.

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file inside the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
MODEL=openai/gpt-4o-mini
```

Never commit the `.env` file to GitHub.

## 9. Running the Application

Execute:

```powershell
python travel_planner.py
```

Enter a city name when prompted.

Example:

```text
Enter the city you want to visit: Chennai
```

The CrewAI agent processes the request and generates three travel recommendations.

## 10. Sample Output

**Input:**

```text
Chennai
```

**Output:**

```text
TOP 3 PLACES TO VISIT IN CHENNAI

1. Marina Beach
   A popular coastal attraction known for its
   long shoreline and lively atmosphere.

2. Kapaleeshwarar Temple
   A historic temple famous for its
   traditional Dravidian architecture.

3. Fort St. George
   A historic landmark that provides
   insights into Chennai's colonial history.
```

## 11. Supported Cities

The application dynamically accepts city names.

Examples include:

- Chennai
- Bengaluru
- Mumbai
- Hyderabad
- Delhi
- Kolkata

The application is not restricted to these cities.

## 12. Key CrewAI Concepts Demonstrated

**Agent:** Defines the Travel Planner's role, goal, and backstory.

**Task:** Specifies the travel recommendation requirement and expected output.

**Crew:** Combines the agent and task into an executable workflow.

**Sequential Process:** Executes the task in the configured order.

**Kickoff:** Starts the CrewAI workflow using `crew.kickoff()`.

## 13. Limitations

The application uses the language model's existing knowledge and does not perform real-time internet searches.

Therefore, it does not verify current ticket prices, opening hours, or attraction availability.

## 14. Conclusion

The AI Travel Planner demonstrates the fundamental building blocks of CrewAI through a simple single-agent application.

It successfully integrates Python, CrewAI, and an OpenAI language model to generate city-specific travel recommendations.

The project provides a foundation for developing more advanced multi-agent travel planning applications.