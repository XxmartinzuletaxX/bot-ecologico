import discord
import random
from bot_logic import gen_pass
from discord.ext import commands
import os
import requests

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="*",intents=intents)
flores = ["🌹","🌷","🌺","🌼","🌸"]
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('Hola, aqui podras aprender sobre')
    await ctx.send('*bolsas = Como podemos reutilizar las bolsas.') 
    await ctx.send('*aire_arboles = Cuales son los mejores arboles para purificar tu ambiente.') 
    await ctx.send('*habitos = Habitos sencillos para reducir la contaminacion.') 
    await ctx.send('*anticontaminantes = Materiales que ayudan a evitar la contaminacion')
    await ctx.send('*flor = Te enseña una flor de cinco') 

@bot.command()
async def bolsas(ctx):
    await ctx.send(f'Las bolsas de plastico pueden llegar a ser muy malas para el medio ambiente pero si sabemos como reutilizarlas podemos evitar este problema, para esto podriamos tener algo asi como una colecta de bolsas, que usariamos cuando mas lo necesitemos, como por ejemplo cuando salimos de compras y necesitamos bolsas, en vez de usar las de supermercado y comntaminar usamos nuestras bolsas para las compras o tambien una bolsas reutilizables que se degradan rapuido evitando asi la contaminacion por exeso de basura ')

@bot.command()
async def aire_arboles(ctx):
    await ctx.send('Si quieren aprender mas de el como purificar el arie de su entorno algunos de los mejores arboles para esto son: el Espatifilo, la Sanseviera y la Ficus robusta, estas son algunas de lasplantas que por medio de su proceso natural ayudan al medio amobiente eliminando la mayoria de gases afectantes para la capa de ozono y ayudando con la contaminacion y el calentamiento global ')

@bot.command()
async def habitos(ctx):
    await ctx.send('Ademas algunos de los habitos que mas ayudan al medio ambinete son: Reciclar la basura, usar productos que puedan reutilizarse, Apagar las luces, consumir productos ecológicos y locales, evitar dejar los aparatos enchufados, cerrar los grifos correctamente, utilizar el termostato, moverte en transporte público.')

@bot.command()
async def anticontaminantes(ctx):
    await ctx.send('Por ultimo algunos de los materiales mas anticontaminantees son por ejemplo la materiales de la medicina casera como hierbas y planatas medicinales y no solo alli las podemos encontrar sino tambien los materiales de contrucion como el metal ya que no produce ningun gas peligroso para el medio ambiente pero se puede demorar en descomponer pero su ventaja es la resistencia, aunque no solo hay materiales de este tipo en las grandes empresas, tambien desde el hogar podemos hacer una gran diferencia usando la anteriormente mencionadas bolsas biodegradables y dandole una segunda vida a las cosas volviendo las menos contaminantes ')

@bot.command()
async def flor(ctx):
    fe = random.choice(flores)
    await ctx.send(fe)
