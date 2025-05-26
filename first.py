import discord
from app import get_password
from discord.ext import commands
intents= discord.Intents.default()
intents.message_content = True
bot= commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print("El bot esta en linea")
@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy un bot de prueba")
@bot.command()
async def adios(ctx):
    await ctx.send("Adios, hasta luego")
@bot.command()
async def password(ctx):
    await ctx.send("Ingres la logitud de la contraseña ")
    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    longitud = await bot.wait_for('message',check=verificar, timeout=40)
    longitud =int(longitud.content)
@bot.command()
async def password(ctx):
    await ctx.send("Ingres la logitud de la contraseña ")

    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    longitud = await bot.wait_for('message',check=verificar, timeout=40)

    longitud =int(longitud.content)

    password =get_password(longitud)
    await ctx.send(f"Tu contraseña es: {password}")

@bot.command()
async def meme(ctx):
    with open("./img/meme1.jpeg","rb") as f: 
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")    
