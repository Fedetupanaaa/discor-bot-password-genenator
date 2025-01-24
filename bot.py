import discord
from bot_logic import gen_pass
from discord.ext import commands


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



bot.run("Token")
