import discord
from bot_logic import gen_pass
from bot_logic import gen_emoji
from bot_logic import coin_flip
import random
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'entramos como: {bot.user}')

@bot.command()
async def gen(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(10)}")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def emoji(ctx):
    await ctx.send(f" {gen_emoji()}")

@bot.command()
async def numero(ctx):
    numero_aleatorio = random.randint(1, 10)
    await ctx.send(f'El número aleatorio es: {numero_aleatorio}')
    

@bot.command()
async def coinflip(ctx):
    await ctx.send(f"la moneda dice: {coin_flip()}")    






bot.run("Token")
