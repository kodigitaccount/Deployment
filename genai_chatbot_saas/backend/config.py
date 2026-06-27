import os
from dotenv import load_dotenv

# Load local environment variables if available
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    
    @staticmethod
    def validate():
        if not Config.GEMINI_API_KEY:
            raise ValueError("Missing GEMINI_API_KEY! Please set it in your environment variables.")