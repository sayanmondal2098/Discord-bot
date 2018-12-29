#CLIENT ID = 528244648720859136
#CLIENT_SECCRET = dQgBlL4wJwXy5Su8ZZVCfHgFlCR5kUTv
# token = NTI4MjQ0NjQ4NzIwODU5MTM2.Dwfl-Q.RNoYQDB-hP8bqXsOWaz5AJ9u9Gk
# PERMISSION_INTEGER = 67648
# https://discordapp.com/api/oauth2/authorize?client_id=528244648720859136&permissions=337984&scope=bot

import discord
from discord.ext import commands

client = discord.Client()
# discord.client()
# bot = commands.Bot(command_prefix='$', description='Just A Rather Very Intelligent System, now on Discord!')

@client.event
async def on_user_info():
    print(f"We have loged in as {client.user}")
    print(client.get_user_info)

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        await client.send_message(message.channel, '":smiley: :wave: Hello, there!"')
        # await client.send_typing('":smiley: :wave: Hello, there!"')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello. I,m Hakuna Matata.')
    
    if message.content.startswith('welcome'):
        await client.send_message(message.channel, ' :ok_hand: :wave: Thanks')

    if message.content.startswith('help'):
        await client.send_message(message.channel, ' "$greet" , "welcome" and "help" are only available')
        
# NTI4MjQ0NjQ4NzIwODU5MTM2.DwfurQ.Nrq1DxGYnGpbiH1fwYlZNFGXlQk
client.run("NTI4MjQ0NjQ4NzIwODU5MTM2.DwfurQ.Nrq1DxGYnGpbiH1fwYlZNFGXlQk")
on_user_info()
