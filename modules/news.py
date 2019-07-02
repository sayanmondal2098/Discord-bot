import os
import requests
from random import randint
import discord

NEWS_API_TOKEN = 'a3b6770420a8435bb81c79c3d4f7ea71'


def top_headlines():
    """
    Gets top headlines from NewsAPI
    :return: <dict> discord.Embed message
    """
    source = "google-news-in"  # TODO: Add option to choose source
    try:
        r = requests.get("https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + NEWS_API_TOKEN)
        data = r.json()
        # TODO: Find a way to include multiple articles instead of a random one
        article = data['articles'][randint(0, len(data['articles']) - 1)]
        imageurl = article['urlToImage'].replace('\\', '')
        embed = discord.Embed(
            title=article['title'],
            description=article['description'],
            url=article['url'],
            image_url=imageurl
        )
        embed.set_image(url=imageurl)
        # embed.set_footer(text="Powered by NewsAPI! (newsapi.org)")
        return embed
    except Exception as e:
        print(e)
        return discord.Embed(title="Something went wrong")
