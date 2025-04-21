import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

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

    def respond(self, input):
        response = gameMasterClient.models.generate_content(
            model = self.model,
            contents = input,
            config = self.config
        )
        return response.candidates[0].content.parts[0].text