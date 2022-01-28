import discord
from discord.ext  import commands
import os
import asyncio
import pandas as pd
import random
from alive import keep_alive
import praw
import random

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='-', intents=intents)



reddit = praw.Reddit(client_id='ID',
                     client_secret='SECRET',
                     user_agent='NAME',
                     username="USERNAME",
                     password="PASS",
                     check_for_async=False)

@client.event
async def on_ready():
    print('Ready lmao')
    for guild in client.guilds:
      print(guild.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="| Type: -mflake"))
    return

@client.event
async def on_member_join(member: discord.Member):
  if member.guild.id == 825329265934860300:
    #role = discord.utils.get(member.guild.roles, name='Jedi Master')
    #await member.add_roles(role)
    embedVari = discord.Embed(title=f'Henlo <a:pogslide:854214992449503293>', description=f' {member} <a:fireasf:853981488063447040>  **Thank you** for joining at **{member.guild.name}** <a:abelhey:853872414236868618>  enjoy your stay here. <a:welcomein:853872414428233749>', color=0x9b59b6)
    embedVari.add_field(name="You will find several macros and scripts for number of games", value = chr(173), inline=False)
    embedVari.add_field(name ="You'd find macros and scripts for CSGO, Rust, dead by daylight, Rainbow Six Seige, Apex, PUBG and many other FPS games all for **free** <a:rgbcatvibe:853628188978184245>", value=chr(173), inline=False)
    """embedVari.add_field(name="<a:language:853665155480420353> **Important notice:** <a:warningg:853665154356215858>" , value="If you decide to **leave** this server, the *toxic bots* of this server will **ban** your ID for 69 days(perhaps even more) due to policies of this server's owners which do not welcome unwanted trespassers and you will be unable to **rejoin**", inline=False)
    """
    embedVari.add_field(name="Glhf", value="In case you have any queries or questions, feel free to ask in <#825329266777391145>, do not dm any mods <a:sabofast:853628189930815528>" , inline=False)
    embedVari.set_footer(text=f'User joining info: {member.display_name} | ID-{member.id}  ')
    await member.send(embed=embedVari)

@client.command(name='mflake' , brief='Command List', description='Command List')
async def mflake(ctx):
  embedVari = discord.Embed(title="Command List", description=f"Hi {ctx.author.name}, thanks for the shoutout this is the command list of commands that I perform <a:hecc:868143852542910535>", color=0x9b59b6)

  embedVari.add_field(name="<a:partysparkles:857883296036683786> Text Commands <a:partysparkles:857883296036683786>", value="`-humour` *sends humorous text* \n`-joke`  *sends a joke* \n`-inspire` *sends motivational quote*", inline=True)  
  embedVari.add_field(name="<a:sparkles:871393634946281503> Standard Commands <a:sparkles:871393634946281503>", value="`-meme` *sends random meme* \n`-anime` *sends anime image* \n`-news` *sends trending news*", inline=True)

  file = discord.File("line.gif", filename="line.gif")
  embedVari.set_image(url="attachment://line.gif")
  embedVari.set_footer(text=f'Command list for dear {ctx.author.display_name} <3')
  embedVari.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embedVari, file=file)
  return  

data = pd.read_csv("funtweets.csv")
#RANDOM FUNNY TWEETS
@client.command(name='humour' , brief='[Free] Attemps to return email address from roll number', description='Attemps to return email address from roll number')
async def humour(ctx):
  #aaa = client.get_channel(867445266096586773) 
  try:  
    #student=(data.loc[data['ID'].isin([number])])
    #sid = data.loc[data['ID'] == random.choice]
    sid = data.sample(random.randint(2,18503))    
    #sid =  data.loc[data['ID'] == random.choice(sidd)]

    num = sid['Joke'].iloc[0]
    embed = discord.Embed(
            title = f'Humour <a:duck07:868471766174011454>',
            description = f'{num}',
            color = 0xDC143C #crimson
            ) 
    embed.set_footer(text=f'Humour requested by {ctx.author.display_name}')
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    #embed.add_field(name=f'*Fun*', value= f'{num}' , inline=False)
    #aaa = client.get_channel(867445266096586773) 
    a = await ctx.send(embed=embed) 
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")  
    #await a.add_reaction("<a:upvotes:859341695442485270>")      
    #await a.add_reaction("<a:lmaooo:871334469427142676>")
    #await a.add_reaction("<a:leomockin:871334473214615592>")
    #await a.add_reaction("<:kekbruhlmao:871334468949012481>")
    #await a.add_reaction("<a:kekxd:871334472254095371>")
    #await a.add_reaction("<:kekverysad:871334469712359424>")    
    #await a.add_reaction("<a:yenotfunny:853872415045845064>")  
    #await a.add_reaction("<a:elonhigh:859340946017353728>")
    #await a.add_reaction("<a:bidenjam:854224066641788948>")  
    #await a.add_reaction("<a:100rgb:854224425674211328>")          
    #await aaa.send(embed=embed)
    return        
  except:
    await ctx.send(f'{ctx.author.mention}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    #await aaa.send(f'{ctx.author.name}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    return   


data3 = pd.read_csv("Quotes.csv")
#RANDOM FUNNY TWEETS
@client.command(name='inspire' , brief='[Free] Attemps to return isnpirational quote', description='Attemps to return isnpirational quote')
async def inspire(ctx):
  #aaa = client.get_channel(867445266096586773) 
  try:  
    #student=(data.loc[data['ID'].isin([number])])
    #sid = data.loc[data['ID'] == random.choice]
    sid = data3.sample(random.randint(2,1665))    
    #sid =  data.loc[data['ID'] == random.choice(sidd)]

    num = sid['Quote'].iloc[0]
    embed = discord.Embed(
            title = f'Quote <a:100rgb:854224425674211328>',
            description = f'{num}',
            color = 0xDC143C #crimson
            ) 
    embed.set_footer(text=f'Quote requested by {ctx.author.display_name}')
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    #embed.add_field(name=f'*Fun*', value= f'{num}' , inline=False)
    #aaa = client.get_channel(867445266096586773) 
    a = await ctx.send(embed=embed) 
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")      
    #await a.add_reaction("<a:upvotes:859341695442485270>")      
    #await a.add_reaction("<a:lmaooo:871334469427142676>")
    #await a.add_reaction("<a:leomockin:871334473214615592>")
    #await a.add_reaction("<:kekbruhlmao:871334468949012481>")
    #await a.add_reaction("<a:kekxd:871334472254095371>")
    #await a.add_reaction("<:kekverysad:871334469712359424>")    
    #await a.add_reaction("<a:yenotfunny:853872415045845064>")  
    #await a.add_reaction("<a:elonhigh:859340946017353728>")
    #await a.add_reaction("<a:bidenjam:854224066641788948>")  
    #await a.add_reaction("<a:100rgb:854224425674211328>")          
    #await aaa.send(embed=embed) 
    return        
  except:
    await ctx.send(f'{ctx.author.mention}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    #await aaa.send(f'{ctx.author.name}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    return  

data1 = pd.read_csv("reddit-jokes.csv")
#RANDOM FUNNY TWEETS
@client.command(name='joke' , brief='[Free] Attemps to return email address from roll number', description='Attemps to return email address from roll number')
async def joke(ctx):
  #aaa = client.get_channel(867445266096586773) 
  try:  
    #student=(data.loc[data['ID'].isin([number])])
    #sid = data.loc[data['ID'] == random.choice]
    sid = data1.sample(random.randint(2,208108))    
    #sid =  data.loc[data['ID'] == random.choice(sidd)]

    num = sid['Joke'].iloc[0]
    embed = discord.Embed(
            title = f'Joke <a:goooose:857884213571092490>',
            description = f'{num}',
            color = 0xDC143C #crimson
            ) 
    embed.set_footer(text=f'Joke requested by {ctx.author.display_name}')
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    #embed.add_field(name=f'*Fun*', value= f'{num}' , inline=False)
    #aaa = client.get_channel(867445266096586773) 
    a = await ctx.send(embed=embed) 
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")      
    #await a.add_reaction("<a:upvotes:859341695442485270>")      
    #await a.add_reaction("<a:lmaooo:871334469427142676>")
    #await a.add_reaction("<a:leomockin:871334473214615592>")
    #await a.add_reaction("<:kekbruhlmao:871334468949012481>")
    #await a.add_reaction("<a:kekxd:871334472254095371>")
    #await a.add_reaction("<:kekverysad:871334469712359424>")    
    #await a.add_reaction("<a:yenotfunny:853872415045845064>")  
    #await a.add_reaction("<a:elonhigh:859340946017353728>")
    #await a.add_reaction("<a:bidenjam:854224066641788948>")  
    #await a.add_reaction("<a:100rgb:854224425674211328>")          
    #await aaa.send(embed=embed) 
    return        
  except:
    await ctx.send(f'{ctx.author.mention}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    #await aaa.send(f'{ctx.author.name}, Something went wrong, try again this command few moments later <a:peperain:859340940648251432>')
    return  

@client.command()
async def meme(ctx):
  
    #channel = client.get_channel(int(859671257012240435))
    subreddit = reddit.subreddit("memes")

    all_subs = []
    hot = subreddit.hot(limit = 20)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    ups = random_sub.score
    comments = random_sub.num_comments
    link = random_sub.permalink
    url = random_sub.url
    #embed = discord.Embed(title = name, color=discord.Color.gold())
    embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url = url)
    embed.set_footer(text = f"👍{ups} 💬{comments}, post requested by {ctx.author.display_name} | ID-{ctx.author.id}")
    a=await ctx.send(embed=embed)
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")  
    #await rea.add_reaction("randreaction")  
   

@client.command()
async def anime(ctx):
  
    #channel = client.get_channel(int(859671257012240435))
    subreddit = reddit.subreddit("AnimeART")

    all_subs = []
    hot = subreddit.hot(limit = 40)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    ups = random_sub.score
    comments = random_sub.num_comments
    link = random_sub.permalink
    url = random_sub.url
    #embed = discord.Embed(title = name, color=discord.Color.gold())
    embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url = url)
    embed.set_footer(text = f"👍{ups} 💬{comments}, post requested by {ctx.author.display_name} | ID-{ctx.author.id}")
    a=await ctx.send(embed=embed)
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")  
    await a.add_reaction("<a:animelessthan3:868471767876927519>")
    #await rea.add_reaction("randreaction") 

@client.command()
async def news(ctx):

    #channel = client.get_channel(int(859671257012240435))
    subreddit = reddit.subreddit("news")

    all_subs = []
    hot = subreddit.hot(limit = 10)
    for submission in hot:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    ups = random_sub.score
    comments = random_sub.num_comments
    link = random_sub.permalink
    url = random_sub.url
    #embed = discord.Embed(title = name, color=discord.Color.gold())
    embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
    #embed.set_image(url = url)
    embed.set_footer(text = f"👍{ups} 💬{comments}, news requested by {ctx.author.display_name}")
    a=await ctx.send(embed=embed)
    await a.add_reaction("<a:fireasf:853981488063447040>")  
    await a.add_reaction("<:trash:871364464841224262>")  
    #await rea.add_reaction("randreaction")     

async def my_task(ctx):
    while True:
      channel = client.get_channel(int(862279078735511573))
      subreddit = reddit.subreddit("R6Memes")

      all_subs = []
      hot = subreddit.hot(limit = 30)
      for submission in hot:
        all_subs.append(submission)
      random_sub = random.choice(all_subs)
      name = random_sub.title
      ups = random_sub.score
      comments = random_sub.num_comments
      link = random_sub.permalink
      url = random_sub.url
      #embed = discord.Embed(title = name, color=discord.Color.gold())
      embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
      embed.set_image(url = url)
      embed.set_footer(text = f"👍{ups} 💬{comments}")
      await channel.send(embed=embed)
      #await var.add_reaction("<a:upvotered:859709745682317343>")
      await asyncio.sleep(3800)
@client.command()
async def r6stuff(ctx):
    client.loop.create_task(my_task(ctx))


async def my_task1(ctx):
    while True:
      channel = client.get_channel(int(856811827860996096))
      subreddit = reddit.subreddit("memes")
     
      all_subs = []
      hot = subreddit.hot(limit = 50)
      for submission in hot:
        all_subs.append(submission)
      random_sub = random.choice(all_subs)
      name = random_sub.title
      ups = random_sub.score
      comments = random_sub.num_comments
      link = random_sub.permalink
      url = random_sub.url
      #embed = discord.Embed(title = name, color=discord.Color.gold())
      embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
      embed.set_image(url = url)
      embed.set_footer(text = f"👍{ups} 💬{comments}")
      await channel.send(embed=embed)
      #await var.add_reaction("<a:upvotered:859709745682317343>")
      await asyncio.sleep(1800)
@client.command()
async def mflake1(ctx):
    client.loop.create_task(my_task1(ctx))


@client.event
async def on_message(message):

  if message.content.startswith('-meme'):
    await message.add_reaction("<a:catyell:859340946298634300>")
  await client.process_commands(message)      

  """
  channel= client.get_channel(int(859671257012240435))#rekt memes
  if message.channel == message.author.dm_channel: 
    if message.author.id == 415884831805931551:
        embed =  (f'{message.content}')
        #embed.set_footer(text=f'Message sent by {message.author.display_name} | ID-{message.author.id}')
        #embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await channel.send(embed)         
  """

keep_alive()
client.run(os.getenv('token'))
