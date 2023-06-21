import random
import discord
from discord.ext import commands, tasks
from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
from io import BytesIO
import requests
from gtts import gTTS

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.watching, name="you from the walls"))
  print(f"{client.user} is ready")


@client.command()
async def copyText(ctx, *, msg = None):
  if msg == None:
    msg = "none"

  await ctx.send(msg)


@client.command()
async def say(ctx, *, text =None):
  if text == None:
    text = "you peace of shit write someting, done leave it empty"

  speech = gTTS(text = text, lang = "en")
  speech.save("sayCommand/result.mp3")

  await ctx.send(file = discord.File("sayCommand/result.mp3"))


def searchGif(keyWord):
  #generating a random gif based on the give keyword
  apiKey = "6AF20RsShIhtPx2YFuJtIU4h5ZzlEHXK"
  endPoint = "https://api.giphy.com/v1/gifs/random"
  params = {
    "apiKey": apiKey, "tag": keyWord
  }

  response = requests.get(endPoint, params=params)
  data = response.json()

  if response.status_code == 200:
    if data["data"]:
      gifURL = data["data"]["images"]["original"]["url"]
      return gifURL
    else:
      return None
  else:
    return None


@client.command()
async def gif(ctx, keyWord = None):
  if keyWord == None:
    keyWord = "random"

  gifURL = searchGif(keyWord)

  if gifURL:
    await ctx.send(f"here is your fucking gif {gifURL}")
  else:
    await ctx.send("if found nothing you little shit")


@client.command()
async def porn(ctx):
  photos = open('photo.txt').readlines()

  await ctx.send(random.choice(photos))


@client.command()
async def gay(ctx, user: discord.Member = None):
  if user is None:
     user = ctx.author

  gayPFP = Image.open('gayPfp/gay.png').convert("RGBA")
  r, g, b, alpha = gayPFP.split()

  if user.avatar is None:
    await ctx.send(f"The user {user.mention} doesnt have a profile picture you peace of shit!")
    return
  
  avatar_bytes = await user.avatar.with_format("png").read()
  pfp = Image.open(BytesIO(avatar_bytes)).resize(gayPFP.size)

  alpha = alpha.point(lambda i: i > 0 and 160)
  result = Image.composite(gayPFP, pfp, alpha)
  result.save('gayPfp/result.png')

  await ctx.send(file=discord.File("gayPfp/result.png"))
  
@client.event
async def on_message(msg):
  await client.process_commands(msg)

  if msg.author == client.user:
    return

  if msg.content.startswith("hello") or msg.content.startswith("Hello"):
    await msg.channel.send("shut the fuck up")

  if msg.content.startswith("give me a slap") or msg.content.startswith("Give me a slap"):
    await msg.channel.send("oh yeah baby")

  if msg.content.startswith("Hoshen") or msg.content.startswith("hoshen") or msg.content.startswith("חשן"):
    await msg.channel.send("אמא שלך")


client.run(
  "MTExNDgyNTUwMTA2OTAxNzExOA.GrWiZJ.QS9pPOVAehb-_4CcqSt_oW3qm1idjHe_L4Dndg")


