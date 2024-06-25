import discord
import time
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
tkmsonuc = ""
bot = commands.Bot(command_prefix='$', intents=intents)
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

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
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
    
bot.run("TOKEN")