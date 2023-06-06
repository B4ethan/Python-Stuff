import random
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.watching, name="you from the walls"))
  print(f"{client.user} is ready")


@client.command()
async def porn(ctx):
  photos = open('photo.txt').readlines()

  await ctx.send(random.choice(photos))


@client.command()
async def nitro(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author

  await user.send(
    f"{ctx.author.mention} שלח לך ניטרו בחינם: https://dis.cord.gifts/c/8ar1CZdfMNTqL0ze")
  
@client.command()
async def help(ctx):
  await ctx.send("what the fuck do you want?? i am not going to help you")

@client.event
async def on_message(msg):
  await client.process_commands(msg)

  if msg.author == client.user:
    return

  if msg.content.startswith("hello"):
    await msg.channel.send("shut the fuck up")

  if msg.content.startswith("give me a slap"):
    await msg.channel.send("oh yeah baby")


client.run(
  "MTExNDgyNTUwMTA2OTAxNzExOA.GrWiZJ.QS9pPOVAehb-_4CcqSt_oW3qm1idjHe_L4Dndg")


