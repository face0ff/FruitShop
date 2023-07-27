from jokeapi import Jokes  # Import the Jokes class
import asyncio

from chat.models import Chat


async def print_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke()
    if joke["type"] == "single":  # Print the joke
        return joke["joke"]
    else:
        return joke["setup"], joke["delivery"]




