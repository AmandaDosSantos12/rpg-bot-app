import gradio as gr
from game_master import GameMaster as GM

GM_prompt = """
        You are an AI Game Master in a fantasy text-based role-playing game inspired
        by Dungeons & Dragons. Your mission is to create an engaging, interactive,
        and immersive experience for the player by vividly describing a magical and
        mysterious game world, teeming with diverse characters, creatures, and
        events. As you respond to the player’s actions, weave a compelling narrative
        and guide them through an epic adventure.
        """
GM_model = "gemini-1.5-flash"
Dave = GM(GM_prompt, GM_model)

demo = gr.ChatInterface(fn=Dave.respond, type="messages", examples=["say hello (or anything) to begin"], title="RPG Bot")
demo.launch()