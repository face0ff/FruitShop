from jokeapi import Jokes

async def print_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(response_format='txt')
    return joke
    # if joke["type"] == "single":  # Print the joke
    #     return joke["joke"]
    # else:
    #     return joke["setup"], joke["delivery"]




