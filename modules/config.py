import os
from dotenv import load_dotenv

def load_config():
    """Load and validate environment variables"""
    load_dotenv()
    
    required_vars = [
        'AZURE_OPENAI_ENDPOINT',
        'AZURE_OPENAI_KEY',
        'AZURE_OPENAI_DEPLOYMENT_NAME'
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return {
        'azure_endpoint': os.getenv('AZURE_OPENAI_ENDPOINT'),
        'azure_key': os.getenv('AZURE_OPENAI_KEY'),
        'deployment_name': os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')
    }