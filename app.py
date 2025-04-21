import panel as pn
from time import sleep
from game_master import GameMaster as GM

pn.extension()

def get_user_response(contents, gamemaster):
    response = gamemaster.respond(contents)
    sleep(1)
    for index in range(len(response)):
        yield response[0:index+1]
        sleep(0.3)


def start_chat():
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

    chat = pn.chat.ChatInterface(callback = Dave.respond,
                                 max_height = 5000,
                                 show_rerun = False,
                                 show_undo = False,
                                 show_clear = False,
                                 show_button_name = False,
                                 avatar = None)
    chat.servable(target = "chat_block")

    """
    chat.send(
        "Hi, I'm Dave!",
        respond = True
    )
    """

start_chat()