import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


# ---------------------------------------
# STEP 1: Load Environment Variables
# ---------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing!")

if not model_name:
    raise ValueError("MODEL is missing!")


# ---------------------------------------
# STEP 2: Configure the Language Model
# ---------------------------------------

llm = LLM(
    model=model_name,
    temperature=0.3
)


# ---------------------------------------
# STEP 3: Get City Name from User
# ---------------------------------------

city = input("Enter the city you want to visit: ").strip()

if not city:
    raise ValueError("City name cannot be empty!")


# ---------------------------------------
# STEP 4: Create Travel Planner Agent
# ---------------------------------------

travel_planner = Agent(
    role="Experienced Travel Planner",

    goal=(
        "Recommend exactly three interesting places "
        "to visit in the city selected by the user."
    ),

    backstory=(
        "You are an experienced travel consultant who "
        "helps first-time tourists explore new cities. "
        "You specialize in recommending famous landmarks, "
        "cultural attractions, and memorable local experiences. "
        "Your recommendations are practical, informative, "
        "and easy for first-time visitors to understand."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# ---------------------------------------
# STEP 5: Create Travel Planning Task
# ---------------------------------------

travel_task = Task(
    description=(
        f"Recommend exactly 3 places to visit in {city}. "
        "Choose well-known and interesting attractions. "
        "For each place, provide its name and a short "
        "description explaining why it is worth visiting. "
        "Do not recommend more or fewer than 3 places."
    ),

    expected_output=(
        f"A travel recommendation list for {city} "
        "containing exactly 3 numbered places. "
        "Each recommendation must include:\n"
        "1. Place name\n"
        "2. A brief description (1-2 sentences)\n"
        "Do not include additional places or lengthy explanations."
    ),

    agent=travel_planner
)


# ---------------------------------------
# STEP 6: Create Crew
# ---------------------------------------

travel_crew = Crew(
    agents=[travel_planner],
    tasks=[travel_task],
    process=Process.sequential,
    verbose=True
)


# ---------------------------------------
# STEP 7: Execute Crew
# ---------------------------------------

print("\nStarting AI Travel Planner...\n")

result = travel_crew.kickoff()


# ---------------------------------------
# STEP 8: Display Final Output  
# ---------------------------------------

print("\n" + "=" * 60)
print(f"TOP 3 PLACES TO VISIT IN {city.upper()}")
print("=" * 60)

print(result.raw)

print("=" * 60)