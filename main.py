from hentai import *
import discord
import os
import requests
import ujson
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game('.hentai help for help'))
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

  print('Servers connected to:')
  print(len(client.guilds))




@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msg = msg.lower()
  msg = msg.split()
  user = message.author.id  
  douj = []

  inp = ""
  i = 2
  while i < len(msg):
    inp += str(msg[i])+" "
    i += 1
  
  if len(msg) < 2:
    msg.append("s")

  
  if msg[0] == '.hentai':
    if msg[1] == "tag":
      inp = inp.split()

      for doujin in Utils.search_by_query(msg[1] + ":" + inp[0], sort=Sort.PopularToday):
        douj.append(doujin)
        break

    elif msg[1] == "parody":
      for doujin in Utils.search_by_query(msg[1] + ":" + inp, sort=Sort.PopularToday):
        douj.append(doujin)
        break

    elif msg[1] == "help":
      await message.channel.send("<@" + str(user) + ">")
      embed=discord.Embed(title="info", url="", description="Hi this is the nHentai bot, I will be you best friend at recomending doujinshi from the website NHentai.net. \nMy commands are: \n.hentai help : shows this message \n.hentai tag <tag> : search for most popular doujinshi of the day with the tag <tag> \n.hentai parody <parody> : search for most popular doujinshi of the day with the parody <parody> \n.hentai : gives you a random doujinshi", color=0xeb2754)
      await message.channel.send(embed=embed)
      #await message.channel.send("Hi this is the nHentai bot, I will be you best friend at recomending doujinshi from the website NHentai.net. \nMy commands are: \n.hentai help : shows this message \n.hentai tag <tag> : search for most popular doujinshi of the day with the tag <tag> \n.hentai parody <parody> : search for most popular doujinshi of the day with the parody <parody> \n.hentai : gives you a random doujinshi")
    else:
      x = True
      while x:
        doujin = Hentai(Utils.get_random_id())

        for lang in doujin.language:
          if lang.name == "english":
            douj.append(doujin)
            x = False  

    tags = ""

    print(douj)

    for x in douj:
      name = str(x.title(Format.Pretty))
      ids = str(x.id)
      URL = "https://nhentai.net/g/" + ids
      for tag in x.tag:
        tags += str(tag.name) +", "
      await message.channel.send("<@" + str(user) + ">")
      embed=discord.Embed(title=name, url=URL, description=tags, color=0xeb2754)
      embed.set_thumbnail(url=doujin.image_urls[0])
      await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))