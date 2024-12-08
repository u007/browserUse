import openai
from dotenv import load_dotenv
import os
from openai import OpenAIError, AuthenticationError

def test_openai_key():
    try:
        # Load environment variables from .env file
        load_dotenv()
        
        # Get the API key from the environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API Key not found. Make sure it's set in the .env file.")
        
        # Set the OpenAI API key
        openai.api_key = api_key
        
        # Make a test API call (list available models)
        client = openai.OpenAI()
        response = client.models.list()
        
        # If successful, print the available models
        print("API Key is working!")
        print("Available models:")
        for model in response:
            print(f"- {model.id}")
            
    except AuthenticationError:
        print("Invalid API Key. Please check your key and try again.", api_key)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_openai_key()
