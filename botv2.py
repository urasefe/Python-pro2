import discord
import time
import random
import requests
from discord.ext import commands
from tokenpy import token
import os
intents = discord.Intents.default()
intents.message_content = True
tkmsonuc = ""
bot = commands.Bot(command_prefix='kuki ', intents=intents)
liste = ["taş","kağıt","makas"]
def tkmf(tkmarg):
    global tkmsonuc
    if tkmarg == "taş" and random.choice(liste) == "taş":
        tkmsonuc = "Rakibin de taş dedi berabere"
    elif tkmarg == "taş" and random.choice(liste) == "kağıt":
        tkmsonuc = "Rakibin kağıt dedi kaybettin"
    elif tkmarg == "taş" and random.choice(liste) == "makas":
        tkmsonuc = "Rakibin makas dedi kazandın"
    elif tkmarg == "kağıt" and random.choice(liste) == "taş":
        tkmsonuc = "Rakibin taş dedi kazandın"
    elif tkmarg == "kağıt" and random.choice(liste) == "kağıt":
        tkmsonuc = "Rakibin kağıt dedi berabere"
    elif tkmarg == "kağıt" and random.choice(liste) == "makas":
        tkmsonuc = "Rakibin makas dedi kaybettin"
    elif tkmarg == "makas" and random.choice(liste) == "taş":
        tkmsonuc = "Rakibin taş dedi kaybettin"
    elif tkmarg == "makas" and random.choice(liste) == "kağıt":
        tkmsonuc = "Rakibin kağıt dedi kazandın"
    elif tkmarg == "makas" and random.choice(liste) == "makas":
        tkmsonuc = "Rakibin makas dedi berabere"
ordeklist = []



def duckhuntimg():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def tkm(ctx, tkmdeger):

    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    tkmf(tkmdeger)
    await ctx.send(tkmsonuc)

@bot.command()
async def mem(ctx):
    memlist = os.listdir("memler")
    secilenmem = ""
    if random.randint(1,100) == 1:
        secilenmem = "memler\mem4.jpg"
    else:
        secilenmem = random.choice(memlist)
    
    with open(f'memler/{secilenmem}', 'rb') as f:
            picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command("duckhunt")
async def duckhunt(ctx, sayibil):
    image_url = duckhuntimg()
    await ctx.send(image_url)
    rs = random.randint(1,10)
    await ctx.send(rs)
    if int(sayibil) == rs:
        await ctx.send("ördeği yakaladın!")
        ordeklist.append(image_url)
    else:
        await ctx.send("yakalayamadın :(")
@bot.command()
async def duckscaught(ctx):
    await ctx.send(len(ordeklist))

@bot.command()
async def helpme(ctx):
    await ctx.send("Spotify oynatma listem için /playlisy|Github discord örnekler için /dcrep|Ana github repositoryim için /gitmrep|Ördek avı için /duckhunt|Ördek koleksiyonu için /duckscaught|taş kağıt makas için /tkm ,oynanacak şey|Rastgele meme için /mem|")
@bot.command()
async def oyun(ctx):
    os.startfile("https://play.unity.com/en/games/687d91ef-b3bf-4eb0-a451-91a4b2f4c343/webgl-builds")



bot.run(token)
