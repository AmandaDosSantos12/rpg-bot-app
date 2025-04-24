import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from secret import get_project_api_key

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = get_project_api_key()

gameMasterClient = genai.client.Client(
    api_key = GOOGLE_API_KEY
)

class GameMaster():
    def __init__(self, prompt, model, temperature = 0.5, top_k = 40,
                 max_output_tokens = 8192):
        self.model = model
        self.config = types.GenerateContentConfig(
            temperature = temperature,
            top_k = top_k,
            max_output_tokens = max_output_tokens,
            system_instruction = prompt
        )

    def respond(self, input, history):
        #history is a gradio dictionary that gets passed in by default
        #not currently using it here
        response = gameMasterClient.models.generate_content(
            model = self.model,
            contents = input,
            config = self.config
        )
        return response.candidates[0].content.parts[0].text