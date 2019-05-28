import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
client = discord.Client()


@bot.command()
async def test(ctx):
    await ctx.send("I heard you! {0}".format(ctx.author))


@bot.command()
async def on_message(message):
    if message.content.startswith("$greet"):
        await client.send_message(message.channel, '":smiley: :wave: Hello, there!"')
        # await client.send_typing('":smiley: :wave: Hello, there!"')
        msg = await client.wait_for_message(author=message.author, content="hello")
        await client.send_message(message.channel, "Hello. I,m Hakuna Matata.")

    if message.content.startswith("welcome"):
        await client.send_message(message.channel, " :ok_hand: :wave: Thanks")

    if message.content.startswith("help"):
        await client.send_message(
            message.channel, ' "$greet" , "welcome" and "help" are only available'
        )


bot.run("NTc5MzgzNjE5OTMyNTIwNDU4.XOUtnA.DkCX2WxYKtpuaTDwoI2ORbCmKuo")
