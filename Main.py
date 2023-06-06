import random
import discord
from discord.ext import commands
from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
from io import BytesIO

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
async def gay(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author

  gayPFP = Image.open("GayPfp/gay.png").convert("RGBA")
  r, g, b, alpha = gayPFP.split()

  asset = user.avatar_url_as(size = 128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data).resize(gayPFP.size)

  alpha = alpha.point(lambda i: i>0 and 160)
  result = Image.composite(gayPFP, pfp, alpha)
  result.save("GayPfp/result.png")

  await ctx.send(file = discord.File("GayPfp/result.png"))
  
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


