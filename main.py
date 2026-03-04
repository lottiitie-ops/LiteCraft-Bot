import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")
    
token = os.getenv("TOKEN")
if token:
    bot.run(token)
else:
    print("❌ Error: No se encontró la variable de entorno TOKEN en Railway")
