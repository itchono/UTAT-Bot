import discord # basic libraries
from discord.ext import commands # allows us to have a bot that can take commands

import random

# stores the bot token
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN') # Secret Bot Password

client = commands.Bot(command_prefix="!")


@client.command()
async def test(ctx: commands.Context):
    await ctx.send("Yo yeet")

@client.command()
async def thread(ctx:commands.Context, threadName, members: commands.Greedy[discord.Member]):
    '''
    Creates a new thread with a certain name. Mention members to give them access to the thread.
    '''
    group = ctx.guild.get_channel(737829694359076924)
    chn = await group.create_text_channel(threadName)

    await ctx.message.add_reaction("👍")
    await ctx.send(f"Thread has been created at {chn.mention}")

    people = [ctx.author] + members

    m = await chn.send(f"This thread was created by {' '.join([p.mention for p in people])}\nLink to original message: {ctx.message.jump_url}")
    await m.pin()


@client.event
async def on_ready():
    print("Bot is ready!")

    game = discord.Game("Beep beep")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message: discord.Message):
    # TODO can put stuff here
    
    await client.process_commands(message)
    

# ==============================
client.run(TOKEN)
