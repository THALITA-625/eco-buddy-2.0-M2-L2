import discord
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

saved_number = None
 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx, start=1, end=10):
    global saved_number

    saved_number = random.randint(start, end)
    await ctx.send("Guess a number from " + str(start) + " until " + str(end))

@bot.command()
async def answer(ctx, number):
    if int(number) == saved_number:
        await ctx.send("Congrats!!! you win")
    else:
        if int(number) < saved_number:
            await ctx.send("The number is bigger")
        else:
            await ctx.send("The number is smaller")

def get_duck_image_url():    
    url = 'https://youtu.be/CGd3lgxReFE?si=Sf_wg6_PMj2oOo0o' and 'https://youtu.be/dGMtqjYlAbg?si=91gh6Bfj1jXFqYVU' and 'https://youtu.be/DCuHBq58ZOU?si=2jvrXv7EwughORnD'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('video1')
async def video1(ctx):
    url = "https://youtu.be/CGd3lgxReFE?si=Sf_wg6_PMj2oOo0o"
    await ctx.send(url)


@bot.command('video2')
async def video2(ctx):
    url = "https://youtu.be/dGMtqjYlAbg?si=91gh6Bfj1jXFqYVU"
    await ctx.send(url)

@bot.command('video3')
async def video3(ctx):
    url = "https://youtu.be/DCuHBq58ZOU?si=-hMIIugcaMY-jW-0"
    await ctx.send(url)

@bot.command('video4')
async def video4(ctx):
    url = "https://youtu.be/0uxq4ndgLts?si=NvGqDQY9BtSRGJC8"
    await ctx.send(url)

async def tips(ctx):
    tips = [
        "pakai tumbler estetik agar mengurangi sampah botol plastik", 
        "saat belanja atau jalan jalan, bawa totebag agar mengurangi sampah kantong plastik", 
        "harus paham 3R, reduce(mengurangi), reuse(pakai ulang), recycle(daur ulang)", 
        "pakai kertas bekas ulang agar mengurangi sampah kertas",
        "habiskan makanan, karena food waste adalah penyumbang sampah terbesar"
        ]
    await ctx.send(random.choice(tips))

bot.run("TOKEN BOT DISCORD")