import discord
import aiohttp
import os

# Searches for a image related to the search arg
async def process(search_arg):

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": "290680376069-ngecg2cc2m5km9cap0feanab4fbje78i.apps.googleusercontent.com",
        "cx": "014040594270632678970",
        "searchType": "image",
        "q": search_arg,
        "num": 1,
        "safe": "active",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status == 403:
                return "Limit exceeded"
            data = await resp.json()
            image_url = data["items"][0]["link"]
            return discord.Embed(
                title=f"{search_arg}".capitalize(), image=image_url
            ).set_image(url=image_url)