import os
from dotenv import load_dotenv

load_dotenv()

def get_llm_config():
    return {
        "config_list": [{
            "model": os.environ.get("OPENAI_DEPLOYMENT_NAME"),
            "api_key": os.environ.get("OPENAI_API_KEY"),
            "base_url": os.environ.get("OPENAI_ENDPOINT"),
            "api_version": os.environ.get("OPENAI_API_VERSION"),
            "api_type": "azure"
        }]
    }

