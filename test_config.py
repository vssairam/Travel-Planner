import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key and model
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")

# Validate configuration
if api_key:
    print("OpenAI API Key: Configured")
else:
    print("OpenAI API Key: Missing")

print("Model:", model)