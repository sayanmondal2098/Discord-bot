import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():
    print("Ready when you are!")
    print("I am running on " + client.user.name)
    print("With the iD: " + client.user.id)


@client.command(pass_context=True)
async def hey(ctx):
    await client.get_channe("Hello Hooman!")


client.run("NTc5MzgzNjE5OTMyNTIwNDU4.XOUtnA.DkCX2WxYKtpuaTDwoI2ORbCmKuo")
