import discord
from discord.ext import commands
import os
import time

token = os.getenv("TOKEN") #Gets the token from the .env
bot = commands.Bot(command_prefix='b-') #Defines the prefix of the bot

div = '--------------------------------' #Purely to divide everything.
ownerid = 'YOUR-ID-HERE' #Put your own id here. it just looks fancy :)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep.")) #Changes activity to watching
    print(div)
    print("Bot username: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    print(div)
    print("Bot owner ID: " + ownerid)
    print(div)

@bot.command()
@commands.guild_only() #makes it so the command can only be used in servers, not in groups or DMs.
async def test(ctx):
  success = ('Success!') #end message
  msg = await ctx.send("Hold on...") #The first message send.
  time.sleep(3) #Lets the bot rest for 3 seconds before continuing 
  await msg.edit(content=success) #Edits the message to 'success'

bot.run(token) #Runs the bot
