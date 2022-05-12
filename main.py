import os
import time
import random
import discord
import datetime
import keep_alive
from discord.utils import get
from asyncio import sleep
from itertools import cycle
from datetime import datetime
from discord_slash import SlashCommand
from discord.ext import commands, tasks


color = (0, 0xffffff)
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', intents=intents.all())
slash = SlashCommand(bot, sync_commands=True)


#Says if the bot is connected and who its connected to. Status swap makes the bots status change
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  print("Arsonist is fueled and ready to burn!")
  status_swap.start()

status = cycle([
  'Watching Chats',
  'beep boop',
  'Bot by LAB-W',
  '/help for cmds (BETA)',
  'I wanna flamethrower',
  'ha ha bot goes brr',
  'I love forest fires',
  'Smokey the bear hides from me',
	'made with .py if you were wondering',
  'got a custom firetruck ;)',
	'let it burn',
  'BETA TESTING IS STILL HAPENING!!!',
  'VERSION 8.7 OUT NOW!!!'
])

#loops the status
@tasks.loop(seconds=10)
async def status_swap():
  await bot.change_presence(activity=discord.Game(next(status)))

#Help command (looks like s#!t cause its basic) "/help"

#soon...

#b


#Invite command "Invite"
@slash.slash(name= 'Invite', description='Invite the bot to your own server!')
async def invite(ctx):
  embed=discord.Embed(
  title="Invite Me!", url="https://discord.com/api/oauth2/authorize?client_id=797181865630629938&permissions=4228902135&scope=applications.commands%20bot", description="Click above to invite me to your own server!", 
  color=0xFF5733)
  await ctx.send(embed=embed)

#Ping command "/ping".
@slash.slash(name='Ping', description='Tells you the bot latency')
async def ping(ctx):
  await ctx.send(f'Pong! Bot Speed is - {round(bot.latency * 1000)}ms')

#Nuke command "/molotov"
@slash.slash(name='Molotov', description= 'Mass burns 500 the messages in the channel.')
@commands.has_permissions(manage_messages=True)
async def molotov(ctx, amount=501):
  await ctx.channel.purge(limit=amount)
  await ctx.send('Channel has been hit with a molotov!')

#Purge command "/burn"
@slash.slash(name='Burn', description= 'Burns a specific amount of messages in the channel BETA')



#Logging, automaticly logs messages from "/burn" and "/molotov"


#Errors will go below this. They are here so the bot doesn't shut down by a bad command.

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry but that isn't in my copy of 'The arsonists handbook'.")

@bot.event
async def on_missing_access(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry but I can't do anything in that channel.")

@bot.event
async def on_missing_permissions(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("You need a higher power for that.")


#"KEY" is the name I gave my token in the Secrets page.
#keep_alive connects to my keep_alive file makeing a server for my uptime robot to connect to which keeps it active 99% of the time besides minor outages.

keep_alive.keep_alive()

my_secret = os.environ['KEY']

bot.run(my_secret)