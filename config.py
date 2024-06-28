import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Accessing variables
bot_token = os.getenv('API_TOKEN')