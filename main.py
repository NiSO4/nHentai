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



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg = msg.lower()
    msg = msg.split()
    user = message.author.id  

    inp = ""
    i = 2
    while i < len(msg):
      inp += str(msg[i])+" "
      i += 1

    try:
      if msg[0] == '.hentai':
        if msg[1] == "tag":
          inp = inp.split()

          for doujin in Utils.search_by_query(msg[1] + ":" + inp[0], sort=Sort.PopularToday):
            await message.channel.send("<@" + str(user) + ">")
            await message.channel.send("https://nhentai.net/g/" + str(doujin.id))
            break

        elif msg[1] == "parody":
          for doujin in Utils.search_by_query(msg[1] + ":" + inp, sort=Sort.PopularToday):
            await message.channel.send("<@" + str(user) + ">")
            await message.channel.send("https://nhentai.net/g/" + str(doujin.id))
            break

        elif msg[1] == "help":
          await message.channel.send("<@" + str(user) + ">")
          embed=discord.Embed(title="info", url="", description="Hi this is the nHentai bot, I will be you best friend at recomending doujinshi from the website NHentai.net. \nMy commands are: \n.hentai help : shows this message \n.hentai tag <tag> : search for most popular doujinshi of the day with the tag <tag> \n.hentai parody <parody> : search for most popular doujinshi of the day with the parody <parody> \n.hentai : gives you a random doujinshi", color=0x7C0A02)
          await message.channel.send(embed=embed)
          #await message.channel.send("Hi this is the nHentai bot, I will be you best friend at recomending doujinshi from the website NHentai.net. \nMy commands are: \n.hentai help : shows this message \n.hentai tag <tag> : search for most popular doujinshi of the day with the tag <tag> \n.hentai parody <parody> : search for most popular doujinshi of the day with the parody <parody> \n.hentai : gives you a random doujinshi")
        
    except:
      x = True
      while x:
        doujin = Hentai(Utils.get_random_id())

        for lang in doujin.language:
          if lang.name == "english":
            await message.channel.send("<@" + str(user) + ">")
            await message.channel.send("https://nhentai.net/g/" + str(doujin.id))
            x = False
            break

keep_alive()
client.run(os.getenv('TOKEN'))