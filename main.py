# developed by Markus Menner 
# github.com/Markusme2
# twitter.com/mennermarkus
# discord tag = MarkusM#1405
import random
import discord
import os
import sys
import pandas as pd
import requests
from dotenv import load_dotenv
from discord.ext import commands


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
allowed_mentions = discord.AllowedMentions(everyone = True)
load_dotenv(".env")
tenor = os.getenv("TENOR_KEY")
discord = os.getenv("DISCORD_KEY")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

#greetings
@bot.event
async def on_join(member):
    await member.send("Welcome to the server!")

@bot.event
async def on_message(message):
    if message.content == "Hello" or message.content == "hello":
        await message.channel.send("Whats up big guy!")
    await bot.process_commands(message)
    
@bot.listen()
async def on_message(msg):
    if msg.content == "$command":
        await msg.channel.send("Type in $commands for command list")
    
@bot.command()
async def commands(ctx):
    await ctx.send("$randomnumber will display a random number between 1-1,000\n")
    await ctx.send("$random_small_num will display a random number between 1-100\n")
    await ctx.send("$random_big_num will display a random number between 100-1,000,000")
    await ctx.send("$flipcoin will flip a coin and display either heads or tails")
    await ctx.send("$duelist, $sentinel, $controller, $initiator will display a random agent")
    await ctx.send("$poll will create a poll with the question you ask")
#--------------------------------------------------------------------------------------#
#beginning of random number generator
@bot.command()
async def randomnumber(ctx):
    await ctx.send(random.randrange(1,1000))

@bot.command()
async def random_small_num(ctx):
    await ctx.send(random.randint(1,100))

@bot.command()
async def random_big_num(ctx):
    await ctx.send(random.randint(100,1000000))

@bot.command()
async def flipcoin(ctx):
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q=flipcoin&key={tenor}&client_key=my_test_app&limit=8")
    choice = random.randint(1,2)
    if r.status_code == 200:
        index = random.randint(0,8)
        await ctx.send(r.json()['results'][index]['url'])
        await ctx.send("Heads" if choice == 1 else "Tails")
    else:
        await ctx.send("Heads" if choice == 1 else "Tails")
#--------------------------------------------------------------------------------------#
# beginning of random valorant agent generator
# tenor rate limit is 1 request per second 
@bot.command()
async def duelist(ctx):
    agent = random.randint(1,6)
    agent_name = ''
    if agent == 1:
        agent_name = "Reyna"
    elif agent == 2:
        agent_name = "Yoru"
    elif agent == 3:
        agent_name = "Jett"
    elif agent == 4:
        agent_name = "Raze"
    elif agent == 5:
        agent_name = "Phoenix"
    elif agent == 6:
        agent_name = "Neon"
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={agent_name}valorant&key={tenor}&client_key=my_test_app&limit=8")
    if r.status_code == 200:
        await ctx.send(agent_name)
        index = random.randint(0,8)
        await ctx.send(r.json()['results'][index]['url'])
    else:
        await ctx.send(agent_name)
# "Killjoy","Cypher", "Sage", "Chamber"
@bot.command()
async def sentinel(ctx):
    agent = random.randint(1,4)
    agent_name = ''
    if agent == 1:
        agent_name = "Killjoy"
    elif agent == 2:
        agent_name = "Cypher"
    elif agent == 3:
        agent_name = "Sage"
    elif agent == 4:
        agent_name = "Chamber"
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={agent_name}valorant&key={tenor}&client_key=my_test_app&limit=8")
    if r.status_code == 200:
        await ctx.send(agent_name)
        index = random.randint(0,8)
        await ctx.send(r.json()['results'][index]['url'])
    else:
        await ctx.send(agent_name)

@bot.command()
async def controller(ctx):
    agent = random.randint(1,5)
    agent_name = ''
    if agent == 1:
        agent_name = "Omen"
    elif agent == 2:
        agent_name = "Viper"
    elif agent == 3:
        agent_name = "Astra"
    elif agent == 4:
        agent_name = "Brimstone"
    elif agent == 5:
        agent_name = "Harbor"
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={agent_name}valorant&key={tenor}&client_key=my_test_app&limit=8")
    if r.status_code == 200:
        await ctx.send(agent_name)
        index = random.randint(0,8)
        await ctx.send(r.json()['results'][index]['url'])
    else:
        await ctx.send(agent_name)

@bot.command()
async def initiator(ctx):
    agent = random.randint(1,6)
    agent_name = ''
    if agent == 1:
        agent_name = "Skye"
    elif agent == 2:
        agent_name = "Breach"
    elif agent == 3:
        agent_name = "Sova"
    elif agent == 4:
        agent_name = "Kay/0"
    elif agent == 5:
        agent_name = "Gekko"
    elif agent == 6:
        agent_name = "Fade"
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={agent_name}valorant&key={tenor}&client_key=my_test_app&limit=8")
    if r.status_code == 200:
        await ctx.send(agent_name)
        index = random.randint(0,8)
        await ctx.send(r.json()['results'][index]['url'])
    else:
        await ctx.send(agent_name)
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
#beginning of poll command
@bot.command()
async def poll(ctx, *, question):
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"W or L: \n✅ = Yes**\n**❎ = No\n\n{question}")
    await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
    await message.add_reaction('❎')
    await message.add_reaction('✅')
#--------------------------------------------------------------------------------------#
counter = 0
@bot.listen()
async def on_message(msg):
    global counter
    word = msg.content
    file = open(r'counter.txt', 'r') 
    contents = file.read()
    reply = random.randint(1,6)
    if word in contents:
        counter += 1
        if reply == 1:
            await msg.channel.send(f"Thats a no no word {counter}")
        if reply == 2:
            await msg.channel.send(f"FLAG on the play. Number {counter}")
        if reply == 3:
            await msg.channel.send(f"Bro is on a roll. Number {counter}")
        if reply == 4:
            await msg.channel.send(f"Thats a yikes from me. Number {counter}")
        if reply == 5:
            await msg.channel.send(f"Cmon bucko. Number {counter}")
        if reply == 6:
            await msg.channel.send(f"Go Next. Number {counter}")
    file.close()
#--------------------------------------------------------------------------------------#
@bot.command()
async def pokemon(ctx, pokedex):
    pokedex = int(pokedex)
    dataframe = pd.read_csv("pokemon.csv", usecols = [2,4,5,6,7,8,10])
    await ctx.send(dataframe.iloc[[pokedex-1]].to_string(index=False))
    gif = requests.get(f"https://api.tenor.com/v1/search?q=pokemon&key={tenor}&limit=8")
    if gif.status_code == 200:
        index = random.randint(0,5)
        await ctx.send(gif.json()['results'][index]['url'])
    else:
        pass




# @bot.command()
# async def imagine(ctx, image):
#   openai.api_key = os.getenv('openai_key')

#   response = openai.Image.create(
#     prompt= image,
#     n=1,
#     size="512x512"
#   )
#   image_url = response['data'][0]['url']
#   await ctx.send(image_url)

#--------------------------------------------------------------------------------------#

    
    
bot.run(discord)